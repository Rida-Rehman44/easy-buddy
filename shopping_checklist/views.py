from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .forms import ShoppingItemFormSet, ChecklistForm  # Import the formset
from .models import ShoppingChecklist


def home(request):
    shopping_checklists = ShoppingChecklist.objects.order_by('-date_time_created').all()
    return render(request, 'home.html', {'shopping_checklists': shopping_checklists})


class CreateView(View):
    formset_class = ShoppingItemFormSet  # Use the formset instead of single form
    template_name = 'create.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(to='/')
        return super(CreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        formset = self.formset_class()  # Instantiate formset
        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST)
        if formset.is_valid():
            checklist = ShoppingChecklist.objects.create(user=request.user)
            instances = formset.save(commit=False)
            for instance in instances:
                # Here you can associate instances with the checklist if needed
                instance.checklist = checklist
                instance.save()

            messages.success(request, 'Checklist created successfully')
            return redirect(to='/shopping_checklist/')

        return render(request, self.template_name, {'formset': formset})

class EditView(View):
    checklist_form_class = ChecklistForm
    item_formset_class = ShoppingItemFormSet
    template_name = 'edit_checklist.html'

    def get(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        checklist_form = self.checklist_form_class(instance=checklist)
        item_formset = self.item_formset_class(instance=checklist)
        return render(request, self.template_name, {'checklist_form': checklist_form, 'item_formset': item_formset, 'checklist': checklist})

    def post(self, request, checklist_id):
        checklist = get_object_or_404(ShoppingChecklist, pk=checklist_id)
        checklist_form = self.checklist_form_class(request.POST, instance=checklist)
        item_formset = self.item_formset_class(request.POST, instance=checklist)
        if checklist_form.is_valid() and item_formset.is_valid():
            checklist_form.save()
            item_formset.save()
            return redirect('/shopping_checklist/')  # Redirect to home screen after editing
        return render(request, self.template_name, {'checklist_form': checklist_form, 'item_formset': item_formset, 'checklist': checklist})