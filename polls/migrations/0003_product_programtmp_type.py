# Generated by Django 3.1.5 on 2021-01-26 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramTmp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.performer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.type')),
            ],
        ),
    ]
