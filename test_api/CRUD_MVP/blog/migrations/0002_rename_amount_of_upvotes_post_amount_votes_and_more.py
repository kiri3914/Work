# Generated by Django 4.0.3 on 2022-03-04 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='amount_of_upvotes',
            new_name='amount_votes',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author_name',
            new_name='author',
        ),
    ]
