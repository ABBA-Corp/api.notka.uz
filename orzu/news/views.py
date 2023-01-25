from rest_framework import viewsets

from .models import News
from .serializers import NewsSerializer, NewsListSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    list_serializer_class = NewsListSerializer
    serializer_class = NewsSerializer
    http_method_names = ["get"]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return self.serializer_class
