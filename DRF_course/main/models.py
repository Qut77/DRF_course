from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Trip(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    destination = models.ForeignKey('Destination', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Путешествие',
        verbose_name_plural='Путешествия'


class Destination(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Место назначения',
        verbose_name_plural='Места назначения'

# class User(models.Model):
#     title = models.CharField(max_length=100, db_index=True)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name='Пользователь',
#         verbose_name_plural='Пользователи'
