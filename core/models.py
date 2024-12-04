from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='students')
    
    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # e.g., Monday, Tuesday
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return f"{self.course.name} - {self.professor.name} - {self.day_of_week} {self.start_time} to {self.end_time}"




class Constraint(models.Model):
    description = models.CharField(max_length=300)
    constraint_type = models.CharField(max_length=50)  # e.g., 'Time', 'Classroom', 'Professor'
    
    def __str__(self):
        return self.description


