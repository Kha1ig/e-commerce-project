from rest_framework import serializers

class BlogSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    short_description = serializers.CharField(max_length=200)
    
