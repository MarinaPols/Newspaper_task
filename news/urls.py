from django.urls import path

# Импортируем созданное нами представление
#from .views import NewsList, NewsDetail, NewsCreate
from .views import (NewsList, NewsDetail, NewsCreate,
                    ArticleCreate, NewsEdit, ArticleEdit, NewsDelete,
                    ArticleDelete, CategoryList, add_subscribe,)

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete', NewsDelete.as_view(), name='news_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit', ArticleEdit.as_view(), name='article_edit'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
    path('sub/', CategoryList.as_view(), name='categories'),
    path('add_sub/category/<int:pk>', add_subscribe, name='add_sub'),


]