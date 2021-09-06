from django.db import models
import random,os
from django.contrib.auth.models import User


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance,filename):
    new_filename = random.randint(1,1234567)
    name,ext = get_filename_ext(filename)
    final_filename = f"{new_filename}{ext}"
    return f"user_details/{new_filename}/{final_filename}"


class UserDetails(models.Model):
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,unique=True )
    Captions = models.TextField()






