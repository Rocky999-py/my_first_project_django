# Generated by Django 3.2 on 2022-02-02 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('instrument', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField(choices=[(1, 'worst'), (2, 'bad'), (3, 'average'), (4, 'good'), (5, 'excellent')])),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.musician')),
            ],
        ),
    ]
