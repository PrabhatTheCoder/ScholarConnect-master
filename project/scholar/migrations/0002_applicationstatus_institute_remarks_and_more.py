# Generated by Django 5.0 on 2023-12-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationstatus',
            name='institute_remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicationstatus',
            name='institute_verification_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicationstatus',
            name='state_authority_remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicationstatus',
            name='state_authority_verification_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
