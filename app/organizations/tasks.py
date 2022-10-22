from django.core.mail import send_mail
from celery import shared_task
from .models import PersonalTask


@shared_task(bind=True)
def notify_personal(self, task_id: int):
    try:
        task = PersonalTask.objects.select_related('personal').get(pk=task_id)
    except PersonalTask.DoesNotExist:
        return
    send_mail(
        subject='Task',
        message=task.body,
        from_email='from@example.com',
        recipient_list=[task.personal.email],
        fail_silently=False,
    )
    task.notified=True
    task.save()
    return {'task_id': task_id}
