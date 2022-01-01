from django.views.generic import TemplateView
from django.contrib.auth import get_user_model


class UserView(TemplateView):
    template_name = 'users/users.html'

    def get_context_data(self, **kwargs):
        User = get_user_model()
        ctx = super().get_context_data(**kwargs)
        ctx['users'] = User.objects.all()
        return ctx
