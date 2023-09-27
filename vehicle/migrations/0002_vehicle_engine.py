# Generated by Django 3.2.6 on 2021-08-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='engine',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True, verbose_name='Engine'),
        ),
    ]
