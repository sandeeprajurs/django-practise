from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from django.urls import path

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    # path('<int:pk>', ArticleDetailView.as_view(), name='articles_detail_view'),
    path('<int:id>', ArticleDetailView.as_view(), name='articles_detail_view'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='articles_update_view'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='articles_delete_view'),
    path('create/', ArticleCreateView.as_view(), name='article_create_view'),
]