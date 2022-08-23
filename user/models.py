from django.db import models
from django.contrib import admin


class Language(models.Model):
    name = models.CharField(max_length=100)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        for i in self.phone_number:
            if i == 0:
                i = '+'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Student(AbstractPerson):
    OS_CHOICES = (
        ('windows', 'Windows'),
        ('macos', 'MacOS'),
        ('linux', 'Linux'),
    )
    work_study_place = models.CharField(max_length=100, null=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=100, choices=OS_CHOICES)

    def __str__(self):
        return self.name


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=100, null=True)
    experience = models.DateField()
    students = models.ManyToManyField(Student, through='Course')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_end_date(self):
        date = self.date_started.month + self.language.month
        return date

    @admin.display(description='Group Upper')
    def group_upper(self):
        return self.group.name.upper()

    def __str__(self):
        return f'{self.name} started {self.date_started}'


