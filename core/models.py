from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Base(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Base):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(null=True)

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(**kwargs)

    def __str__(self):
        return f'{self.title}'


class Like(Base):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True, default=None)

    def __str__(self):
        if self.status:
            return 'Like'
        elif self.status == 0:
            return 'Dislike'
        else:
            return 'Deleted'
