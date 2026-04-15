from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

class SalesView(LoginRequiredMixin,TemplateView):
    template_name = "analytics/sales.html"

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return HttpResponse("No permitido", status=401)
        return super(SalesView,self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        return super(SalesView,self).get_context_data(*args, **kwargs)