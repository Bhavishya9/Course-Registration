from django.views.generic import ListView
from django.views.generic import DetailView
from App.forms import *


class professorview(ListView):
    model=Catelogue
    def get_context_data(self, **kwargs):
        context = super(professorview, self).get_context_data(**kwargs)
        return context

class catelogueDetailView(DetailView):
    model=Catelogue
    context_object_name = "cat_detail"
    def get_object(self, queryset=None):
        name=self.kwargs.get('name')
        if name:
            return Catelogue.objects.get(name=name)
        else:
            return Catelogue.objects.get(pk=self.kwargs["pk"])
