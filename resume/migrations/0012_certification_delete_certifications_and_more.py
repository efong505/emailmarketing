# Generated by Django 4.2 on 2023-05-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_remove_workexperience_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
            options={
                'ordering': ['start', '-end'],
            },
        ),
        migrations.DeleteModel(
            name='Certifications',
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['start', '-end']},
        ),
        migrations.AlterModelOptions(
            name='workexperience',
            options={'ordering': ['-start', 'end']},
        ),
        migrations.RemoveIndex(
            model_name='workexperience',
            name='resume_work_start_96f4f7_idx',
        ),
        migrations.AlterField(
            model_name='education',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='start',
            field=models.DateField(),
        ),
        migrations.AddIndex(
            model_name='education',
            index=models.Index(fields=['start'], name='resume_educ_start_ce07f2_idx'),
        ),
        migrations.AddIndex(
            model_name='workexperience',
            index=models.Index(fields=['-start'], name='resume_work_start_566c28_idx'),
        ),
        migrations.AddIndex(
            model_name='certification',
            index=models.Index(fields=['start'], name='resume_cert_start_8b8aee_idx'),
        ),
    ]