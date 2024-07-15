from django.db import models
from django.contrib.auth.models import User

class GenZUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='genz_profile')
    virtual_closet = models.ManyToManyField('FashionItem', related_name='closets', blank=True)
    mood_boards = models.ManyToManyField('MoodBoard', related_name='boards', blank=True)
    # Add more fields as needed for Gen-Z specific features

    def __str__(self):
        return self.user.username
