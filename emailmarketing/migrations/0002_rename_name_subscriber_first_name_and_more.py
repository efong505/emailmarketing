# Generated by Django 4.2 on 2023-05-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailmarketing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='last_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
