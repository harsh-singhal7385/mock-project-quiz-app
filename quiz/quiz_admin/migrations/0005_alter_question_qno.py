# Generated by Django 4.0.3 on 2022-03-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_admin', '0004_alter_question_qno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qno',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
