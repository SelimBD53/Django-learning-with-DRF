from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Student

@receiver(post_save, sender=User)
def create_student(instance, created, **kwargs):
    print("instance:", instance)
    print("created:", created)
    if created:
        Student.objects.create(user=instance)
        print("Student created Successfully!")