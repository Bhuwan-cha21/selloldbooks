# Generated by Django 4.0.3 on 2022-03-28 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_blog_footer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='footer',
        ),
    ]
