from django.views.generic import *
from .models import Post
from .forms import CreateForm


class IndexView(TemplateView):
    template_name = 'core/index.html'


class PostsView(TemplateView):
    template_name = 'core/posts.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        ctx['results'] = [
            (
                p,
                p.like_set.filter(status=True).count(),
                p.like_set.filter(status=False).count()
            )
            for p in posts
        ]
        return ctx


class PostDetailView(DetailView):
    model = Post
    template_name = "core/post_detail.html"
    context_object_name = "post"

    def get_slug_field(self, **kwargs):
        ctx = super().get_slug_field(**kwargs)
        return ctx


class PostCreateView(CreateView):
    model = Post
    form_class = CreateForm
    template_name = 'core/post_create.html'
    success_url = '/posts'

    #TODO: user_id, slug:
    # user_id = request.user
    # slug = slugify('title')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'core/post_update.html'
    fields = ['title',
              'content',
              'image',
              ]
    template_name_suffix = '_update_form'
    success_url = '/posts'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'core/post_delete.html'
    success_url = '/posts'
