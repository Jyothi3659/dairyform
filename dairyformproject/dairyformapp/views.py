from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import FarmerForm

class FarmerFormView(View):
    form_class =FarmerForm
    initial = {'key': 'value'}
    template_name = 'dairyformapp/index.html'

    def get(self, request, *args, **kwargs):

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
