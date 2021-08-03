from django.db import models

class makeModel(models.Model):
    make_name = models.CharField(null=True, blank=True, max_length=100)
    model_name = models.CharField(null=True, blank=True, max_length=100)
    def __str__(self):
        return '{} {}'.format(self.make_name, self.model_name)
