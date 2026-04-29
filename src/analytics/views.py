from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from order.models import Order

class SalesView(LoginRequiredMixin,TemplateView):
    template_name = "analytics/sales.html"

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return HttpResponse("No permitido", status=401)
        return super(SalesView,self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        context= super(SalesView,self).get_context_data(*args, **kwargs)
        qs = Order.objects.all()
        context["orders"] = qs
        context["recent_orders"] = qs.recent().not_refunded()[:5]
        context["shipped_orders"] = qs.recent().not_refunded().by_status("shipped")[:5]
        context["paid_orders"] = qs.recent().not_refunded().by_status("paid")[:5]
        print(context)
        return context