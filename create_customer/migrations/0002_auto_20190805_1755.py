# Generated by Django 2.2.4 on 2019-08-05 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldata',
            name='address',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='createdAt',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='description',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='email',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='phone',
        ),
    ]
