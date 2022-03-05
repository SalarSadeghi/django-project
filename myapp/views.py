from dataclasses import fields
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from myapp.models import Article, Coment
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# Create your views here.
# class ComentCreateView(CreateView):
#     model = Coment
#     template_name = 'add_comment.html'
#     fields = ("comment",)
#     def form_valid(self,form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ("title","body",)
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ["title","body"]
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user