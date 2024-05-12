from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from events.models import Event
from .forms import ShoppingItemFormSet, ChecklistForm
from .models import ShoppingChecklist


def home(request):
    event_id = request.GET.get('event_id')
    if event_id:
        shopping_checklists = ShoppingChecklist.objects.filter(
            Q(user=request.user) |
            Q(event__in=Event.objects.filter(id=event_id))
        ).order_by('-date_time_created').all()
    else:
        shopping_checklists = ShoppingChecklist.objects.filter(
            Q(user=request.user) |
            Q(event__in=Event.objects.filter(group__in=request.user.groups.all()))
        ).order_by('-date_time_created').all()

    return render(request, 'home.html', {'shopping_checklists': shopping_checklists, 'event_id': event_id})


class CreateView(LoginRequiredMixin, View):
    formset_class = ShoppingItemFormSet  # Use the formset instead of single form
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        formset = self.formset_class()  # Instantiate formset
        event_id = request.GET.get('event_id')
        if event_id:
            events = Event.objects.filter(id=event_id)
        else:
            events = Event.objects.filter(group__in=request.user.groups.all())

        return render(request, self.template_name, {'formset': formset, 'events': events})

    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST)
        if formset.is_valid():
            checklist = ShoppingChecklist.objects.create(user=request.user)
            name = request.POST.get('name')
            checklist.name = name
            event_id = request.POST.get('event_id')
            if event_id:
                event = Event.objects.get(id=event_id)
                checklist.event = event
            checklist.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.checklist = checklist
                instance.save()

            messages.success(request, 'Checklist created successfully')
            return redirect(to='/shopping_checklist/')

        return render(request, self.template_name, {'formset': formset})


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
            return redirect('/shopping_checklist/')  # Redirect to home screen after editing
        return render(request, self.template_name,
                      {'checklist_form': checklist_form, 'item_formset': item_formset, 'checklist': checklist})


class DeleteView(LoginRequiredMixin, View):
    def get(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        return redirect('/shopping_checklist/')  # Redirect to home screen after editing


    def post(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        checklist.delete()
        return redirect('/shopping_checklist/')  # Redirect to home screen after editing