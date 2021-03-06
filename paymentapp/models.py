from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.base import Model
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator,MinValueValidator
from .managers import UserManager
from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    phone_number = models.IntegerField(('phone_number'),validators=[MinValueValidator(10**8),MaxValueValidator(10**9-1)],unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='media/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
class Category(models.Model):
    category_title = models.CharField(('category_title'), max_length=50,)
    def __str__(self):
        return self.category_title
class Product(models.Model):
    product_title = models.CharField(('product_title'), max_length=50,)
    product_price = models.IntegerField(('product_price'),)
    product_description = models.TextField(('product_description'),blank=True)
    product_image = models.CharField(('product_image'), max_length=100,default="placeholder")
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    user= models.ManyToManyField(User)
    def __str__(self):
        return "Product name "+self.product_title
@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            instance_file_field = getattr(instance,field.name)
            delete_file_if_unused(sender,instance,field,instance_file_field)
            
@receiver(pre_save)
def delete_files_when_file_changed(sender,instance, **kwargs):
    if not instance.pk:
        return
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            try:
                instance_in_db = sender.objects.get(pk=instance.pk)
            except sender.DoesNotExist:
                return
            instance_in_db_file_field = getattr(instance_in_db,field.name)
            instance_file_field = getattr(instance,field.name)
            if instance_in_db_file_field.name != instance_file_field.name:
                delete_file_if_unused(sender,instance,field,instance_in_db_file_field)

def delete_file_if_unused(model,instance,field,instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = model.objects.filter(**dynamic_field).exclude(pk=instance.pk).exists()
    if not other_refs_exist:
        instance_file_field.delete(False)