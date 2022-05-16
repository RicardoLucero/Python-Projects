from django.db import models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, null=False)
    CourseNumber = models.IntegerField(max_length=10)
    InstructorName = models.CharField(max_length=80, default="", null=False)
    Duration = models.FloatField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.Title
