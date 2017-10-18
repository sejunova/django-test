from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='post')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title