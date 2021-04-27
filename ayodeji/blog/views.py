from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from blog.models import Post, Comment
from .forms import CommentForm




# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'homepage.html'
    context_object_name = 'all_blogs_list'

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

# def BlogDetailView(request,pk):
#     post =get_object_or_404(Post, pk= pk)
#     comments = post.comments.all()
#     new_comment = None
#     template_name = 'blog_details.html'
#     if request.method =='POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment=comment_form.save(commit= False)
#             new_comment.post = posts
#             new_comment.save()
#             return redirect('blog_detail', pk)
#     else:
#         template_name= 'blog_details.html'
#     context = {"post":posts,"comment_form":comment_form, "comments": comments,"new_comment":new_comment}
#     return render(request, template_name, context )

class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author', 'body']

class BlogUpdateView(UpdateView): 
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

