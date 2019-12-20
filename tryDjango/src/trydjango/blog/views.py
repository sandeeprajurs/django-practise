from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleModelForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # <app_name>/<model_name>_list.html

class ArticleDetailView(DetailView):
    template_name = 'articles/detail_view.html'
    # queryset = Article.objects.all()

    # in order to us id rather than pk
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    success_url = "/"
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_update.html'
    form_class = ArticleModelForm
    success_url = "/"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    form_class = ArticleModelForm
    success_url = "/"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)