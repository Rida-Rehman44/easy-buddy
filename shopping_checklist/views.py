from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from shopping_checklist.forms import CreateForm
from shopping_checklist.models import ShoppingChecklist


def home(request):
    sl = ShoppingChecklist.objects.all()
    return render(request, 'home.html', {'shopping_checklists': sl})


class CreateView(View):
    form_class = CreateForm
    initial = {'key': 'value'}
    template_name = 'create.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the create page while not logged in
        if not request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(CreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            item_name = form.cleaned_data.get('item_name')
            messages.success(request, f'Check list created {item_name}')

            return redirect(to='/shopping_checklist')

        return render(request, self.template_name, {'form': form})