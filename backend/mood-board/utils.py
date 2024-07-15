import requests
from PIL import Image
from io import BytesIO

def validate_image_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        Image.open(BytesIO(response.content))
        return True
    except Exception:
        return False

def create_default_mood_board(user):
    from .models import MoodBoard
    mood_board = MoodBoard.objects.create(user=user, name="Default Mood Board")
    return mood_board
