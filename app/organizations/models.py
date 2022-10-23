from email.policy import default
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=256)


class Position(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name='positions')
    name = models.CharField(max_length=256)


class Personal(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name='personals')
    full_name = models.CharField(max_length=160)
    email = models.EmailField()
    code = models.CharField(max_length=10)


class Department(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name='deparments')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='sub_departments', null=True, blank=True)
    name = models.CharField(max_length=256)
    supervisor = models.ForeignKey(Personal, on_delete=models.SET_NULL, related_name='departments', null=True)


class DepartmentPersonalPostion(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='personals')
    personal = models.ForeignKey(
        Personal, on_delete=models.CASCADE, related_name='positions')
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name='personals')



class PersonalTask(models.Model):
    personal = models.ForeignKey(
        Personal, on_delete=models.CASCADE, related_name='tasks')
    body = models.TextField()
    deadline_at = models.DateTimeField()
    notified = models.BooleanField(default=False)
