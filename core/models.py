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
        ('TA', "Teacher Assistant")
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    timezone = models.IntegerField(default=6)
    courses_as_student = models.ManyToManyField(Course, related_name='cources_as_student')
    courses_as_teacher = models.ManyToManyField(Course, related_name='cources_as_teacher')
    scaler_value = models.FloatField(default=1)
    student_scaler = models.FloatField(default=1.0)
    teacher_scaler = models.FloatField(default=10.0)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Classroom(models.Model):
    name = models.CharField(max_length=140)
    capacity = models.IntegerField()
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Lesson(models.Model):
    LESSON_TYPES = [
        ('normal', 'Normal Class'),
        ('tutorial', 'Tutorial'),
        ('extended', 'Extended Class')
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    length_in_minutes = models.IntegerField(default=90)
    lesson_type = models.CharField(max_length=10, choices=LESSON_TYPES)
    times_per_week = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.course.name} - {self.lesson_type} ({self.times_per_week} times/week)"


# class Schedule(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     professor = models.ForeignKey(Individual, on_delete=models.CASCADE)
#     classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
#     day_of_week = models.CharField(max_length=10)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
    
#     def __str__(self):
#         return f"{self.course.name} - {self.professor.name} - {self.day_of_week} {self.start_time} to {self.end_time}"

class TimeSlots(models.Model):
    name = models.CharField(max_length=255)
    timeslots = models.JSONField()
