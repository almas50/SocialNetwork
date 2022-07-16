from logging import getLogger


from rest_framework import viewsets
from rest_framework.response import Response

from .models import Page
from .serializers import PageListSerializer, PageRetrieveSerializer
from .tasks import update_page_visitors_counter


logger = getLogger('pages')


class PageViewSet(viewsets.ModelViewSet):
    http_method_names = ('get',)
    serializer_class = PageListSerializer
    queryset = Page.objects.all()

    def get_serializer_class(self):
        request = {
            'list': PageListSerializer,
            'retrieve': PageRetrieveSerializer,
        }
        return request.get(self.action)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        update_page_visitors_counter.delay(instance.pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
