# Generated by Django 2.1.3 on 2019-03-31 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book', models.CharField(max_length=100)),
                ('ISBN', models.IntegerField(primary_key=True, serialize=False)),
                ('image', stdimage.models.StdImageField(blank=True, upload_to='bookCover/')),
                ('ebook', models.FileField(blank=True, help_text='Upload the ebook if present', upload_to='ebooks/')),
                ('date', models.DateField(auto_now=True, help_text='Date of Publication')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Library',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='library.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='books_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='has_read', to=settings.AUTH_USER_MODEL),
        ),
    ]
