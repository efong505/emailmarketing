# Generated by Django 4.2 on 2023-05-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zip', models.CharField(blank=True, max_length=12, null=True)),
                ('status', models.CharField(choices=[('Subscribed', 'Subscribed'), ('Unsubscribed', 'Unsubscribed')], default='Subscribed', max_length=20)),
            ],
        ),
    ]
