# Generated by Django 4.1.7 on 2023-07-20 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counting', '0004_donation_note_custom_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='named_donations',
            name='custom_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counting.donation_category_custom'),
        ),
    ]
