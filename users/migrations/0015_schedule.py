# Generated by Django 5.1.4 on 2025-01-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_bear_load'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=0, max_length=50)),
                ('obj', models.CharField(max_length=100, null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('est_cost', models.FloatField(default=0)),
                ('act_cost', models.FloatField(default=0)),
            ],
        ),
    ]
