# Generated by Django 4.0.4 on 2022-05-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id_tarea', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('dead_line', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('isCompleted', models.BooleanField()),
                ('priority_id', models.IntegerField()),
                ('id_usuario', models.IntegerField()),
            ],
        ),
    ]