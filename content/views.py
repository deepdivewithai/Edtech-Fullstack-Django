
from rest_framework import generics
from content.models import Content
from content.serializers import ContentSerializer

class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentDetailView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
