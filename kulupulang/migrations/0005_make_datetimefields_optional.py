# Generated by Django 3.2.11 on 2022-02-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kulupulang', '0004_rename_definition_to_meaning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='passed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batch',
            name='submitted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='passed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
