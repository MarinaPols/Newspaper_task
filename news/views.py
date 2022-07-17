#from django.shortcuts import render
#D3
from .models import Post, Author
import datetime
from .filters import PostFilter
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib.auth.models import User



class NewsList(ListView):
    model = Post
    title_news = 'name'
    ordering = 'dateCreation'

    template_name = 'news.html'

    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        # Получаем обычный запрос

        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime
        context['next_news'] = None
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = Post

    template_name = 'new.html'

    context_object_name = 'new'

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    #def form_valid(self, form):
        #post = form.save(commit=False)
        #post.categoryType = 'NW'
        #post.author = Author.objects.get(authorUser=self.request.user)
        #return super().form_valid(form)

class NewsEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    #def form_valid(self, form):
        #post = form.save(commit=False)
        #post.categoryType = 'NW'
        #post.post.author = Author.objects.get(authorUser=self.request.user)
        #return super().form_valid(form)

class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

class ArticleEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

