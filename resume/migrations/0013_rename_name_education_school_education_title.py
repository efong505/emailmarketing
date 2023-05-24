# Generated by Django 4.2 on 2023-05-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_certification_delete_certifications_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='name',
            new_name='school',
        ),
        migrations.AddField(
            model_name='education',
            name='title',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]