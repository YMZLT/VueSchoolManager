# Generated by Django 3.1.7 on 2021-05-14 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0002_auto_20210514_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opentable',
            old_name='semaster',
            new_name='semester',
        ),
        migrations.AlterUniqueTogether(
            name='opentable',
            unique_together={('course', 'teacher', 'semester')},
        ),
    ]