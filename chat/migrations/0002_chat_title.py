# Generated by Django 4.2.11 on 2024-05-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='title',
            field=models.CharField(default='default title', max_length=100),
            preserve_default=False,
        ),
    ]
