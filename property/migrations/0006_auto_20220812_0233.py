# Generated by Django 2.2.24 on 2022-08-11 23:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_complaint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_flat',
            new_name='flat',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='complaining_user',
            new_name='user',
        ),
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(
                blank=True, 
                default=None, 
                related_name='liked_flats', 
                to=settings.AUTH_USER_MODEL, 
                verbose_name='Кто лайкнул'
            ),
        ),
    ]
