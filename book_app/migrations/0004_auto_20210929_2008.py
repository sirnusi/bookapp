# Generated by Django 3.2.7 on 2021-09-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_auto_20210929_0822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentbook',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='commentbook',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]