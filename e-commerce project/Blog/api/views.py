from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Blog.api.serializers import BlogSerializers
from Blog.models import Blog

@api_view(['GET', 'POST'])
def blog_api_view(request):
    blog = Blog.objects.all()
    serializer = BlogSerializers(blog, many=True)
    return Response(serializer.data)

