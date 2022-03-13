# Generated by Django 3.2.9 on 2022-03-13 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.CharField(editable=False, max_length=32)),
                ('datetime', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('clinician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.clinician')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicedate')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicetime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
