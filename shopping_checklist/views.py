from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import ShoppingItemFormSet  # Import the formset
from .models import ShoppingChecklist


def home(request):
    shopping_checklists = ShoppingChecklist.objects.all()
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
