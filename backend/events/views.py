from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response

from events.filters import EventFilter
from events.models import Event, MeetupData
from events.serializers import ShortEventSerializer, EventSerializer, EventPhotoSerializer, EventPhotoWriterSerializer


class CalendarViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['get', ]
    queryset = Event.objects.filter()
    serializer_class = ShortEventSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_class = EventFilter


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['get', ]
    queryset = Event.objects.filter()
    serializer_class = EventSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_class = EventFilter


class PhotoCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = EventPhotoWriterSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save()
            serializer = EventPhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoCreate(LoginRequiredMixin, ListView):
    template_name = 'events/photo_create.html'
    queryset = Event.objects.order_by('created_at')
    model = Event


class MeetupViewSet(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = [AllowAny, ]
    http_method_names = ['get']

    @staticmethod
    def list(request):
        data = MeetupData.get_solo()
        results = {
            'amount_of_members': data.amount_of_members
        }

        return Response(results, status=status.HTTP_200_OK)
