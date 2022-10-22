from rest_framework import serializers

from .models import *


class ListOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name')
        read_only_fields = fields


class CreateOrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'name')
        read_only_fields = ('id',)


class UpdateOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ListDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'organization', 'supervisor')
        read_only_fields = fields


class CreateDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name', 'organization', 'supervisor')
        read_only_fields = ('id',)


class UpdateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'organization', 'supervisor')
        read_only_fields = ('id',)


class ListPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name', 'organization')
        read_only_fields = fields


class CreatePositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('id', 'name', 'organization')
        read_only_fields = ('id',)


class UpdatePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name', 'organization')
        read_only_fields = ('id',)


class ListPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ('id', 'organization', 'full_name', 'code', 'email')
        read_only_fields = fields


class CreatePersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personal
        fields = ('id', 'organization', 'full_name', 'code', 'email')
        read_only_fields = ('id',)


class UpdatePersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ('id', 'organization', 'full_name', 'code', 'email')
        read_only_fields = ('id',)


class ListDepartmentPersonalPostionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentPersonalPostion
        fields = ('id', 'department', 'personal', 'position')
        read_only_fields = fields


class CreateDepartmentPersonalPostionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepartmentPersonalPostion
        fields = ('id', 'department', 'personal', 'position')
        read_only_fields = ('id',)


class UpdateDepartmentPersonalPostionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentPersonalPostion
        fields = ('id', 'department', 'personal', 'position')
        read_only_fields = ('id',)


class ListSubDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')
        read_only_fields = fields


class ListDepartmentPersonalSerializer(serializers.ModelSerializer):
    personal = ListPersonalSerializer()
    position = ListPositionSerializer()

    class Meta:
        model = DepartmentPersonalPostion
        fields = ('personal', 'position')
        read_only_fields = fields


class ListDepartmentSerializer(serializers.ModelSerializer):
    supervisor = ListPersonalSerializer()
    sub_departments = ListSubDepartmentSerializer(many=True)
    personals = ListDepartmentPersonalSerializer(many=True)

    class Meta:
        model = Department
        fields = ('id', 'organization', 'parent', 'name',
                  'supervisor', 'sub_departments', 'personals')
        read_only_fields = fields


class CreateDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'organization', 'parent', 'name', 'supervisor')
        read_only_fields = ('id',)


class UpdateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'organization', 'parent', 'name', 'supervisor')
        read_only_fields = ('id',)


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalTask
        fields = ('id', 'personal', 'body', 'notify_at', 'notified')
        read_only_fields = ('id', 'notified')
