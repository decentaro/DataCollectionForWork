# Generated by Django 4.0 on 2021-12-31 23:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputError',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bays', models.CharField(choices=[('BAY1', 'Bay1'), ('BAY2', 'Bay2'), ('BAY3', 'Bay3'), ('BAY4', 'Bay4'), ('BAY5', 'Bay5')], default='B1', max_length=9)),
                ('general_description_of_failure', models.CharField(choices=[('BASES', 'Bases'), ('VERTICALS', 'Vertical'), ('CARM', 'C-Arm'), ('ATP', 'ATP'), ('SKINS', 'Skins'), ('TOPHAT', 'Top Hat')], default='BS', max_length=9)),
                ('title_of_error', models.CharField(max_length=100)),
                ('fix_of_error', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
