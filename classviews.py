from django.template import RequestContext
from django.views.generic import ListView
from django.views.generic import DetailView
from App.forms import *
from django.shortcuts import render,render_to_response

class professorview(ListView):
    model=Catelogue
    def get_context_data(self, **kwargs):
        context = super(professorview, self).get_context_data(**kwargs)
        return context

# class catelogueDetailView(DetailView):
#     model=Catelogue
#     context_object_name = "cat_detail"
#     def get_object(self, queryset=None):
#         name=self.kwargs.get('name')
#         if name:
#             return Catelogue.objects.get(name=name)
#         else:
#             return Catelogue.objects.get(pk=self.kwargs["pk"])

def catelogueDetailView(request,pk):
    cat=Catelogue.objects.get(id=pk)
    course=cat.course_set.all().order_by('id')
    return render_to_response('app/catelogue_detail.html',{'cat':cat,'courses':course},context_instance = RequestContext(request))

class studentCatelogueDetailView(DetailView):
    model=Catelogue
    context_object_name = "cat_detail"
    template_name = 'app/student_view_of_catelogue.html'
    def get_object(self, queryset=None):
        name=self.kwargs.get('name')
        if name:
            return Catelogue.objects.get(name=name)
        else:
            return Catelogue.objects.get(pk=self.kwargs["pk"])
