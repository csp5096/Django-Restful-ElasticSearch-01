from django.db import models

class Activation(models.Model):
    name = models.CharField(max_length=128, unique=True)

class Submission(models.Model):
    profile_id = models.UUIDField()
    activation = models.ForeignKey(Activation, on_delete=models.CASCADE, related_name='submissions')

    class Meta:
        unique_together = [
            ('activation', 'profile_id')
        ]





