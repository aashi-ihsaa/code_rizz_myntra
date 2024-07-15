from django.db import models
from django.contrib.auth.models import User

class MoodBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mood_boards')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MoodBoardItem(models.Model):
    mood_board = models.ForeignKey(MoodBoard, on_delete=models.CASCADE, related_name='items')
    image_url = models.URLField(max_length=200)
    description = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mood_board.name} - {self.id}"
