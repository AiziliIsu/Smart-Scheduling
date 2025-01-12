from django.db import models

class Course(models.Model):
    subject_area = models.CharField(max_length=20)
    course_code = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    is_core = models.BooleanField(default=True)
    actual_credits = models.IntegerField(default=6)
    undergraduate_year = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    cohort_number = models.IntegerField(blank=True, null=True)
    course_type = models.CharField(max_length=200)
    n_weeks = models.IntegerField(default=16)
    class_meeting_patterns = models.CharField(max_length=200)
    default_instructor = models.CharField(max_length=300)
    
    scaler_value = models.FloatField(default=1.0)
    
    def __str__(self):
        return self.title


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
    prefered_timeslots = models.ForeignKey("TimeSlots", on_delete=models.CASCADE, related_name="prefered_timeslots")
    courses_as_student = models.ManyToManyField(Course, related_name='cources_as_student')
    courses_as_teacher = models.ManyToManyField(Course, related_name='cources_as_teacher')
    scaler_value = models.FloatField(default=1)
    student_scaler = models.FloatField(default=1.0)
    teacher_scaler = models.FloatField(default=10.0)

    def __str__(self):
        return f"{self.name} ({self.role})"

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


class TimeSlots(models.Model):
    name = models.CharField(max_length=255)
    timeslots = models.JSONField()
