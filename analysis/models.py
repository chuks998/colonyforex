from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Count

class Analysis(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = DateTimeField(default=timezone.now)
    image = models.ImageField(verbose_name='image', upload_to= 'uploads', null=True, blank=True)
    post_title = models.CharField(max_length=200, null=True, blank=True)
    post_subject = models.CharField(max_length=500, null=True, blank=True)
    post_body = models.TextField(max_length=2200, null=True, blank=True, verbose_name='your analysis')
    likes = models.ManyToManyField(User, related_name='analysis_like')
    dis_likes = models.ManyToManyField(User, related_name='analysis_dislike')

    class Meta:
        verbose_name_plural = 'Create Analysis'

    def __str__(self):
        return self.post_title

    def total_likes(self):
        return self.likes.count()
    
    def total_dis_likes(self):
        return self.dis_likes.count()

    
    def get_absolute_url(self):
        return reverse('profile')