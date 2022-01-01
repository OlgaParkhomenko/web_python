from django.views.generic import TemplateView
from .models import Post


class PostsView(TemplateView):
    template_name = 'core/posts.html'

    def get_context_data(self, **kwargs):
        #Post = get_user_model()
        ctx = super().get_context_data(**kwargs)
        ctx['posts'] = Post.objects.all()
        return ctx


class IndexView(TemplateView):
    template_name = 'core/index.html'