from django.db import models

class Trip(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    destination = models.ForeignKey('Destination', on_delete=models.PROTECT, null=True)

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
