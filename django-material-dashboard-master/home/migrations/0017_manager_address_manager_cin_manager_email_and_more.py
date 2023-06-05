# Generated by Django 4.1.9 on 2023-05-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_voiture_available_nonavailability'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='address',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='manager',
            name='cin',
            field=models.CharField(default='----', max_length=50),
        ),
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.EmailField(default='Not Available', max_length=254),
        ),
        migrations.AddField(
            model_name='manager',
            name='nom',
            field=models.CharField(default='Not Available', max_length=50),
        ),
        migrations.AddField(
            model_name='manager',
            name='picture',
            field=models.ImageField(default='', upload_to='client_pictures/'),
        ),
        migrations.AddField(
            model_name='manager',
            name='prenom',
            field=models.CharField(default='Not Available', max_length=50),
        ),
        migrations.AddField(
            model_name='manager',
            name='tel',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
