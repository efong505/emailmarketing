# Generated by Django 4.2 on 2023-04-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_quote_quoted_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'ordering': ['created']},
        ),
        migrations.RemoveIndex(
            model_name='quote',
            name='quote_quote_created_d95553_idx',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='status',
            new_name='stat',
        ),
        migrations.AddIndex(
            model_name='quote',
            index=models.Index(fields=['created'], name='quote_quote_created_0efce0_idx'),
        ),
    ]
