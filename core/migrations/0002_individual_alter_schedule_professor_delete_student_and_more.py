# Generated by Django 5.1.3 on 2024-12-04 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('professor', 'Professor'), ('student', 'Student')], max_length=10)),
                ('courses', models.ManyToManyField(related_name='individuals', to='core.course')),
            ],
        ),
        migrations.AlterField(
            model_name='schedule',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.individual'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
    ]
