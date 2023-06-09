# Generated by Django 4.2 on 2023-05-22 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailmarketing', '0003_subscriber_created_subscriber_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='status',
            field=models.CharField(choices=[('Subscribed', 'Subscribed'), ('Pending', 'Pending'), ('Unsubscribed', 'Unsubscribed')], default='Subscribed', max_length=20),
        ),
    ]
