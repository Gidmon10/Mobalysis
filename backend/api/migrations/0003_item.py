# Generated by Django 3.2.6 on 2021-08-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210821_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.CharField(db_index=True, default='empty', max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, default='empty', max_length=20)),
                ('description', models.TextField(db_index=True, default='empty', max_length=20)),
                ('colloq', models.CharField(db_index=True, default='empty', max_length=20)),
                ('plaintext', models.CharField(default='empty', max_length=20)),
                ('into', models.JSONField(default=dict)),
                ('image', models.JSONField(default=dict)),
                ('gold', models.CharField(db_index=True, default='empty', max_length=20)),
                ('tags', models.JSONField(default=dict)),
                ('maps', models.JSONField(default=dict)),
                ('stats', models.JSONField(default=dict)),
            ],
        ),
    ]