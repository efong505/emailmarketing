# Generated by Django 4.2 on 2023-04-11 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0010_alter_quote_email_alter_quote_name_alter_quote_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
