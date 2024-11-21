from django.shortcuts import render

from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.


class renderhtml(TemplateView):
    template_name='renderhtml.html'

    
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='kavitha'
        ECDO['age']='22'
        ECDO['ESFO']=SchoolForm()
        return ECDO
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data is inserted')
        
class SchoolFv(FormView):
    template_name='SchoolFv.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('done')