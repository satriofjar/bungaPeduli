# Generated by Django 4.2.1 on 2023-05-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_donation_collected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donator',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('Dana', 'Dana'), ('BCA/MANDIRI', 'BCA/MANDIRI')], max_length=100, null=True),
        ),
    ]
