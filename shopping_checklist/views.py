from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from trip.models import Trip
from .forms import ShoppingItemFormSet, ChecklistForm
from .models import ShoppingChecklist

@login_required
def list_home(request):
    trip_id = request.GET.get('trip_id')
    if trip_id:
        shopping_checklists = ShoppingChecklist.objects.filter(
            Q(user=request.user) |
            Q(trip_id=trip_id)
        ).order_by('-date_time_created')
    else:
        shopping_checklists = ShoppingChecklist.objects.filter(
            Q(user=request.user) |
            Q(trip__members=request.user)
        ).order_by('-date_time_created')

    return render(request, 'list_home.html', {'shopping_checklists': shopping_checklists, 'trip_id': trip_id})



class CreateView(LoginRequiredMixin, View):
    formset_class = ShoppingItemFormSet  # Use the formset instead of single form
    template_name = 'create_list.html'

    def get(self, request, *args, **kwargs):
        formset = self.formset_class()  # Instantiate formset
        trip_id = request.GET.get('trip_id')
        if trip_id:
            trips = Trip.objects.filter(id=trip_id)
        else:
            trips = Trip.objects.filter(members=request.user)

        return render(request, self.template_name, {'formset': formset, 'trips': trips})

    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST)
        if formset.is_valid():
            checklist = ShoppingChecklist.objects.create(user=request.user)
            name = request.POST.get('name')
            checklist.name = name
            trip_id = request.POST.get('trip_id')
            if trip_id:
                trip = Trip.objects.get(id=trip_id)
                checklist.trip = trip
            checklist.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.checklist = checklist
                instance.save()

            messages.success(request, 'Checklist created successfully')
            return redirect(f'/list_home/?trip_id={trip_id}')

        trips = Trip.objects.filter(members=request.user)  # Ensure trips are available in case of invalid form
        return render(request, self.template_name, {'formset': formset, 'trips': trips})


class EditView(LoginRequiredMixin, View):
    checklist_form_class = ChecklistForm
    item_formset_class = ShoppingItemFormSet
    template_name = 'edit_checklist.html'

    def get(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        checklist_form = self.checklist_form_class(instance=checklist)
        item_formset = self.item_formset_class(instance=checklist)

        return render(request, self.template_name,
                      {'checklist_form': checklist_form, 'item_formset': item_formset, 'checklist': checklist})

    def post(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        checklist_form = self.checklist_form_class(request.POST, instance=checklist)
        item_formset = self.item_formset_class(request.POST, instance=checklist)
        if checklist_form.is_valid() and item_formset.is_valid():
            checklist_form.save()
            item_formset.save()
            return redirect('/list_home/')  # Redirect to home screen after editing
        return render(request, self.template_name,
                      {'checklist_form': checklist_form, 'item_formset': item_formset, 'checklist': checklist})


class DeleteView(LoginRequiredMixin, View):
    def get(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        return redirect('/list_home/')  # Redirect to home screen after editing


    def post(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        checklist.delete()
        return redirect('/list_home/')  # Redirect to home screen after editing