# Generated by Django 2.2.9 on 2020-02-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20200202_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='entryorder',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
