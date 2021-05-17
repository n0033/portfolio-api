# Generated by Django 3.1.7 on 2021-03-28 12:05

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technologies', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'python'), (2, 'django'), (3, 'djangorestframwork'), (4, 'javascript'), (5, 'react'), (6, 'html'), (7, 'css')], max_length=13)),
                ('link', models.CharField(max_length=150)),
            ],
        ),
    ]