# Generated by Django 4.1.9 on 2023-05-26 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_user_is_online_remove_user_job_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreservation',
            name='status',
            field=models.CharField(default='En cours', max_length=20),
        ),
    ]