# Generated by Django 3.1.2 on 2021-09-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_auto_20210914_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion_match_performance',
            name='tierId',
        ),
        migrations.AddField(
            model_name='champion_match_performance',
            name='tier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]