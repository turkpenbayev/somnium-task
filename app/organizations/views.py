from django.db.models import Prefetch

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.views import ActionSerializerViewSetMixin
from .models import *
from .serializers import *
from .tasks import notify_personal


class OrganizationViewSet(ActionSerializerViewSetMixin,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    serializer_classes = {
        ('list', 'retrieve'): ListOrganizationSerializer,
        'create': CreateOrganizationSerializer,
        ('update', 'partial_update'): UpdateOrganizationSerializer,
    }
    pagination_class = None

    def get_queryset(self):
        return Organization.objects.all()


class PositionViewSet(ActionSerializerViewSetMixin,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_classes = {
        ('list', 'retrieve'): ListPositionSerializer,
        'create': CreatePositionSerializer,
        ('update', 'partial_update'): UpdatePositionSerializer,
    }
    filterset_fields = ('organization', )
    filter_backends = [DjangoFilterBackend]
    pagination_class = None

    def get_queryset(self):
        return Position.objects.all()


class PersonalViewSet(ActionSerializerViewSetMixin,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_classes = {
        ('list', 'retrieve'): ListPersonalSerializer,
        'create': CreatePersonalSerializer,
        ('update', 'partial_update'): UpdatePersonalSerializer,
    }
    filterset_fields = ('organization', )
    filter_backends = [DjangoFilterBackend]
    pagination_class = None

    def get_queryset(self):
        return Personal.objects.all()


class DepartmentViewSet(ActionSerializerViewSetMixin,
                        mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_classes = {
        ('list', 'retrieve'): ListDepartmentSerializer,
        'create': CreateDepartmentSerializer,
        ('update', 'partial_update'): UpdateDepartmentSerializer,
    }
    filterset_fields = ('organization', 'parent')
    filter_backends = [DjangoFilterBackend]
    pagination_class = None

    def get_queryset(self):
        parent = self.request.query_params.get('parent')
        queryset = Department.objects.select_related(
            'supervisor'
        ).prefetch_related(
            'sub_departments',
            Prefetch(
                'personals', DepartmentPersonalPostion.objects.select_related(
                    'personal', 'position'
                )
            )
        ).all()
        if parent is None:
            queryset = queryset.filter(parent__isnull=True)
        return queryset


class DepartmentPersonalPostionViewSet(ActionSerializerViewSetMixin,
                                       mixins.CreateModelMixin,
                                       mixins.ListModelMixin,
                                       mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       viewsets.GenericViewSet):
    serializer_classes = {
        ('list', 'retrieve'): ListDepartmentPersonalPostionSerializer,
        'create': CreateDepartmentPersonalPostionSerializer,
        ('update', 'partial_update'): UpdateDepartmentPersonalPostionSerializer,
    }
    filterset_fields = ('department', )
    filter_backends = [DjangoFilterBackend]
    pagination_class = None

    def get_queryset(self):
        return DepartmentPersonalPostion.objects.all()


class PersonalTaskViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = CreateTaskSerializer
    queryset = PersonalTask.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        notify_personal.apply_async(
            args=(task.pk, ),
            eta=task.notify_at
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
