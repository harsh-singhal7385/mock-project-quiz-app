# Generated by Django 4.0.1 on 2022-03-10 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='quizId',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='quizId',
        ),
    ]