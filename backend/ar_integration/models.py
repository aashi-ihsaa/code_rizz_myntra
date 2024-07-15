from django.db import models

class ARSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id
