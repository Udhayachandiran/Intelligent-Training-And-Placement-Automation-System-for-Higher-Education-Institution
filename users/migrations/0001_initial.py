# Generated by Django 4.1.5 on 2023-04-03 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hiring_team', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_to_job', models.CharField(default='not registered', max_length=30)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiring_team.jobdetail')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.detail')),
            ],
        ),
    ]
