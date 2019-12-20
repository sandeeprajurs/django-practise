from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course
from .forms import CourseForm

# Create your views here.
class CourseObjectMixin(View):
    model = Course
    lookup = 'id'

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id = id)
        return obj

class CourseDetailView(CourseObjectMixin, View):
    template_name = "courses/course_detail_view.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id != None:
            # obj = get_object_or_404(Course, id = id)
            obj = self.get_object()
            context = { 'object': obj }
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = "courses/course_list_view.html"
    queryset = Course.objects.all()

    def get_query_set(self):
        return self.queryset

    def get(self, request):
        context = { 'object': self.get_query_set() }
        return render(request, self.template_name, context)

# class MyCourseList(CourseListView):
#     queryset = Course.objects.filter(id=1)

class CourseCreateView(View):
    template_name = "courses/course_create_view.html"
    
    def get(self, request):
        contactForm = CourseForm(request.GET)
        context = { 'form': contactForm }
        return render(request, self.template_name, context)

    def post(self, request):
        contactForm = CourseForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
        form = CourseForm()
        context = { 'form':  form }
        return render(request, self.template_name, context)
    
class CourseUpdateView(View):
    template_name = "courses/course_create_view.html"

    def get(self, request, id=None):
        contactForm = {}
        if id != None:
            obj = Course.objects.get(id=id)
            contactForm = CourseForm(request.GET or None, instance=obj)
        context = { 'form': contactForm }
        return render(request, self.template_name, context)

    def post(self, request, id=None):
        obj = Course.objects.get(id=id)
        contactForm = CourseForm(request.POST or None, instance= obj)
        if contactForm.is_valid():
            contactForm.save()
        context = { 'form':  contactForm }
        return render(request, self.template_name, context)

