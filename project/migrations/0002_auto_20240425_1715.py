# Generated by Django 3.0.8 on 2024-04-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('delete', 'Delete'), ('stoped', 'Stoped')], default='active', max_length=10),
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
