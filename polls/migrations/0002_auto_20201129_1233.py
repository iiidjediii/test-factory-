# Generated by Django 3.1.3 on 2020-11-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.AddField(
            model_name='answer',
            name='answers',
            field=models.CharField(default=12, max_length=4096),
            preserve_default=False,
        ),
    ]
