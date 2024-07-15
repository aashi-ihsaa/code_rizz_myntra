from rest_framework import serializers
from .models import MoodBoard, MoodBoardItem

class MoodBoardItemSerializer(serializers.ModelSerializer):
    """
    Serializer for MoodBoardItem model.
    
    Fields:
        id (int): The unique identifier for the mood board item.
        mood_board (int): The ID of the associated mood board.
        image_url (str): The URL of the image associated with this item.
        description (str): A text description of the item.
        added_at (datetime): The timestamp when the item was added.
    
    This serializer converts a MoodBoardItem instance into JSON representation and validates data during deserialization.
    """
    
    class Meta:
        model = MoodBoardItem
        fields = ['id', 'mood_board', 'image_url', 'description', 'added_at']
        read_only_fields = ['id', 'added_at']
    
    def validate_image_url(self, value):
        """
        Validate the image URL to ensure it's a valid image URL.
        
        Args:
            value (str): The URL to validate.
        
        Returns:
            str: The validated URL.
        
        Raises:
            serializers.ValidationError: If the URL is not valid.
        """
        from .utils import validate_image_url
        if not validate_image_url(value):
            raise serializers.ValidationError("Invalid image URL.")
        return value

class MoodBoardSerializer(serializers.ModelSerializer):
    """
    Serializer for MoodBoard model.
    
    Fields:
        id (int): The unique identifier for the mood board.
        user (int): The ID of the user who owns the mood board.
        name (str): The name of the mood board.
        created_at (datetime): The timestamp when the mood board was created.
        updated_at (datetime): The timestamp when the mood board was last updated.
        items (list): A list of MoodBoardItem instances associated with this mood board.
    
    This serializer converts a MoodBoard instance into JSON representation and validates data during deserialization.
    """
    
    items = MoodBoardItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = MoodBoard
        fields = ['id', 'user', 'name', 'created_at', 'updated_at', 'items']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Create a new MoodBoard instance.
        
        Args:
            validated_data (dict): The validated data.
        
        Returns:
            MoodBoard: The created MoodBoard instance.
        """
        user = self.context['request'].user
        mood_board = MoodBoard.objects.create(user=user, **validated_data)
        return mood_board
    
    def update(self, instance, validated_data):
        """
        Update an existing MoodBoard instance.
        
        Args:
            instance (MoodBoard): The MoodBoard instance to update.
            validated_data (dict): The validated data.
        
        Returns:
            MoodBoard: The updated MoodBoard instance.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class MoodBoardItemCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating MoodBoardItem instances.
    
    Fields:
        mood_board (int): The ID of the associated mood board.
        image_url (str): The URL of the image associated with this item.
        description (str): A text description of the item.
    
    This serializer is used specifically for creating and updating mood board items.
    """
    
    class Meta:
        model = MoodBoardItem
        fields = ['mood_board', 'image_url', 'description']
    
    def validate_image_url(self, value):
        """
        Validate the image URL to ensure it's a valid image URL.
        
        Args:
            value (str): The URL to validate.
        
        Returns:
            str: The validated URL.
        
        Raises:
            serializers.ValidationError: If the URL is not valid.
        """
        from .utils import validate_image_url
        if not validate_image_url(value):
            raise serializers.ValidationError("Invalid image URL.")
        return value
