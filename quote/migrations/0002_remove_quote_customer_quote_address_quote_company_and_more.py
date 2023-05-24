# Generated by Django 4.2 on 2023-04-07 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='customer',
        ),
        migrations.AddField(
            model_name='quote',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='company',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='position',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='priority',
            field=models.CharField(choices=[('UG', 'Urgent - 1 to week or less'), ('NM', 'Normal - 2 to 4 weeks'), ('LW', 'Low - Still Researching')], default='NM', max_length=2),
        ),
        migrations.AddField(
            model_name='quote',
            name='web_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]