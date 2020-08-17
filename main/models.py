from django.db import models

class BlogPost(models.Model):
    """Main unit of blog"""

    title = models.CharField(max_length=256)

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.title
