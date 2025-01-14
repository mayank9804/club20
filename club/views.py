from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from .models import SuccessfullEvents,UpcomingEvents,ContactSection
from .forms import ContactForm
from django.http import HttpResponseRedirect
# Create your views here.

class IndexView(TemplateView,FormView):
    template_name = 'index.html'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context['form'].is_valid():
            context['form'].save()
            return HttpResponseRedirect('/index')
        return super(IndexView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        form = ContactForm(self.request.POST or None)  # instance= None
        context['form'] = form
        context['xyz'] = UpcomingEvents.objects.all()
        context['abc'] = SuccessfullEvents.objects.all()
        return context



class RegisterView(TemplateView):
    template_name = 'broadregister.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['xyz'] = UpcomingEvents.objects.all()
        return context
