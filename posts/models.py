from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AuthorModel(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='authors')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class PostTagModel(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class PostModel(models.Model):
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to='posts')
    banner = models.ImageField(upload_to='post_banners')
    content = RichTextUploadingField()
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(PostTagModel, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
