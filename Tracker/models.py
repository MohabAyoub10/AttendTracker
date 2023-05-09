from django.db import models
from Collage.models import *




class Lecture(models.Model):
    course_instance = models.ForeignKey(CourseInstance, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    def __unicode__(self):
        return self.course_instance.course.name + " " + self.date + " " + self.time
    

class Attendance(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    def __unicode__(self):
        return self.student.user.first_name + " " + self.student.user.last_name + " " + self.lecture.course_instance.course.name + " " + self.status

