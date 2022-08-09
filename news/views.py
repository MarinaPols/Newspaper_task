from django.shortcuts import render, reverse, redirect
from django.views import View
from .models import Post, Author, Category, CategorySubscribers
import datetime
from .filters import PostFilter
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm, SubscriberForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.views.generic import TemplateView
from django.contrib.auth.models import User



class NewsList(ListView):
    model = Post
    title_news = 'name'
    ordering = 'dateCreation'

    template_name = 'news.html'

    context_object_name = 'news'
    paginate_by = 10

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

class NewsDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Post

    template_name = 'new.html'

    context_object_name = 'new'
    permission_required = (
        'news.view_post',
    )

class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'
    permission_required = ('news.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        post.author = Author.objects.get(authorUser=self.request.user)
        return super().form_valid(form)

    def post(self, *args, **kwargs):
        posts = Post.objects.all().order_by('-dateCreation')[0]
        send_mail(
            subject=Post.title,
            message=Post.text,
            from_email='Marichka.Polska@yandex.ru',
            recipient_list=['funnygreenfox@gmail.com']
        )

class NewsEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'
    permission_required = ('news.change_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        post.author = Author.objects.get(authorUser=self.request.user)
        return super().form_valid(form)

class NewsDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

class ArticleCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'
    permission_required = ('news.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(authorUser=self.request.user)
        return super().form_valid(form)

class ArticleEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'
    permission_required = ('news.change_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(authorUser=self.request.user)
        return super().form_valid(form)

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

class CategoryList(CreateView):

    form_class = SubscriberForm
    model = Category
    template_name = 'categories.html'
    #success_url = reverse_lazy('news_list')
    context_object_name = 'categories'
    queryset = Category.objects.order_by('name')
    #def get(self, request, *args, **kwargs):
        #return render(request, 'news.html', {})

    def post(self, request, *args, **kwargs):  # функция подписки на категорию и связи юзера с категорией
        form = SubscriberForm(request.POST) #было Post

        if form.is_valid():
            category_subscribers = form.save(commit=False)
            category_subscribers.user = request.user
            category_subscribers.save()
            return HttpResponseRedirect(reverse_lazy('news_list'))
        return render(request, 'categories.html', {})

@login_required
def add_subscribe(request, pk):
    #current user
    user = request.user
    #id = request.META.get('HTTP_REFERER')[-2]
    cat = Category.objects.get(id=pk)
    is_subscribed = cat.subscribers.filter(id=user.id).exists()
    if not is_subscribed:
        cat.subscribers.add(user)
        #cat = f'{cat}'
        #email = f'{user.email}'
        #send_mail(
            #subject=f'{cat}',
            #message=f'Вы{request.user.first_name} подписались на обнолвения новостей категрии {cat}',
            #from_email=DEFAULT_FROM_EMAIL,
            #recipient_list=[email, ],

        #)
        #send_mail(
            #'subject here',
            #'message',
            #'Marichka.Polska@yandex.ru',
            #['funnygreenfox@gmail.com'],
            #fail_silently=False,
        #)
        #return redirect(request.META.get('HTTP_REFERER'))
    return render('news.html', {
        'form': form,})







