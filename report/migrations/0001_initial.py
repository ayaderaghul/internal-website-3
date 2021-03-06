# Generated by Django 4.0.1 on 2022-01-14 00:37

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niches', models.CharField(max_length=255)),
                ('project', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('ecosystem', models.CharField(max_length=255)),
                ('launch', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('website', models.URLField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('overview', models.TextField(max_length=255)),
                ('comment', models.TextField(max_length=255)),
                ('rate', models.CharField(choices=[('1', 'potential'), ('2', 'evaluating'), ('3', 'nopotential')], default='2', max_length=2)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('keywords', models.ManyToManyField(max_length=255, to='topics.Keyword')),
            ],
        ),
    ]
