# Generated by Django 4.1.7 on 2023-06-23 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_number', models.CharField(max_length=50, null=True)),
                ('meta_data', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='donation_note',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counting.donation_category'),
        ),
        migrations.AddField(
            model_name='donation_note',
            name='count',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counting.count'),
        ),
        migrations.AlterField(
            model_name='unnamed_donations',
            name='donation_note',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='counting.donation_note'),
        ),
        migrations.AlterField(
            model_name='unnamed_donations',
            name='donation_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='unnamed_donations',
            name='fifty_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unnamed_donations',
            name='five_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unnamed_donations',
            name='hundred_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unnamed_donations',
            name='one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unnamed_donations',
            name='ten_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unnamed_donations',
            name='twenty_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unnamed_donations',
            name='two_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='named_donations',
            name='donation_detail_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counting.donation_detail'),
        ),
    ]