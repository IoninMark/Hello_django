# from django.shortcuts import render


# def index(request):
#    return render(request, 'index.html', context={
#        'who': 'World',
#    })

from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request):
        return redirect('calc', a=40, b=2)


    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['who'] = 'World'
        #return context
