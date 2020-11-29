# Generated by Django 3.1.3 on 2020-11-28 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=4096)),
                ('is_active', models.BooleanField(default=True)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_finish', models.DateTimeField(verbose_name='expiration date')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4096)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]