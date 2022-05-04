# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from hello_django.calc.models import History

# def index(request):
#    return HttpResponse('calc')

#class IndexView(View):

    #def get(self, request, *args, **kwargs):
    #    a = int(kwargs['a'])
    #    b = int(kwargs['b'])
    #    result = f'{a} + {b} = {a + b}'
    #    return HttpResponse(result)


class CalcPageView(TemplateView):

    template_name = "calc/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = int(kwargs['a'])
        b = int(kwargs['b'])
        sum = a + b

        h = History()
        h.value = sum
        h.save()

        context['a'] = a
        context['b'] = b
        context['sum'] = sum
        return context


class HistoryPageView(TemplateView):

    template_name = "calc/history.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = History.objects.reverse()[:10]
        return context
