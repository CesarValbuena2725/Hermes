from django.db import models
from accounts.models import Developer


# Create your models here.


class PR(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField() # Dont you dare not explain your work!
    content = models.TextField()



class Review(models.Model):
    pr = models.ForeignKey(PR, on_delete=models.CASCADE)
    author = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)

    STATUS_CHOICES = [
        ('CH_RQ' , 'Changes Requested'),
        ('ACC', 'Accepted'),
    ]

    status = models.CharField(choices=STATUS_CHOICES, max_length=5)



class Comment(models.Model):
    line_on_pr = models.PositiveIntegerField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=500)