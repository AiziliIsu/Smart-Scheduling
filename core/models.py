from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)  # Optional description field
    is_mandatory = models.BooleanField(default=True)  # Whether the course is mandatory or elective
    scaler_value = models.FloatField(default=1.0)  # Default scaler value set to 1.0

    def __str__(self):
        return self.name


class Lesson(models.Model):
    LESSON_TYPES = [     
        ('normal', 'Normal Class'),
        ('tutorial', 'Tutorial'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    lesson_type = models.CharField(max_length=10, choices=LESSON_TYPES)
    times_per_week = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.course.name} - {self.lesson_type} ({self.times_per_week} times/week)"


class Individual(models.Model):
    ROLE_CHOICES = [
        ('professor', 'Professor'),
        ('student', 'Student'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    courses = models.ManyToManyField(Course, related_name='individuals')
    scaler_value = models.FloatField(default=0.0)  # Scaler value for the individual

    def __str__(self):
        return f"{self.name} ({self.role})"


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Individual, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # e.g., Monday, Tuesday
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.name} - {self.professor.name} - {self.day_of_week} {self.start_time} to {self.end_time}"
