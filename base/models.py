from django.db import models
from multiselectfield import MultiSelectField


TECHNOLOGIES = ((0, 'python'),
                (1, 'django'),
                (2, 'djangorestframwork'),
                (3, 'javascript'),
                (4, 'react'),
                (5, 'html'),
                (6, 'css'),
                )


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    technologies = MultiSelectField(choices=TECHNOLOGIES)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    description_1 = models.TextField()
    description_2 = models.TextField()
    description_3 = models.TextField()
    description_4 = models.TextField()
    description_5 = models.TextField()
    description_6 = models.TextField()
    description_7 = models.TextField()
    description_8 = models.TextField()
    description_9 = models.TextField()
    description_10 = models.TextField()

    def __str__(self):
        return self.title
