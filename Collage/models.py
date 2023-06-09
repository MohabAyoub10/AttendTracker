from django.db import models
from django.conf import settings
# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name


class department(models.Model):
    name = models.CharField(max_length=100)
    head_of_department = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
    



class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    level = models.IntegerField()
    department = models.ForeignKey(department, on_delete=models.CASCADE)    




class Course(models.Model):
    name = models.CharField(max_length=100)
    credit_hours = models.IntegerField()
    Teachering_hours = models.IntegerField()
    code = models.CharField(max_length=10)
    description = models.TextField()

    def __unicode__(self):
        return self.code + " " + self.name
class CourseInstance(models.Model):
    semesters = [
        ('Fall', 'Fall'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Winter', 'Winter')
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100, choices=semesters)
    year = models.IntegerField()

    def __unicode__(self):
        return self.course.code + " " + self.course.name + " " + self.semester + " " + str(self.year)
    
class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_instance = models.ForeignKey(CourseInstance, on_delete=models.CASCADE)



  