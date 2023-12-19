# Generated by Django 4.2.8 on 2023-12-19 16:48

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('apelido', models.CharField(max_length=32, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('nascimento', models.DateField()),
                ('stack', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), null=True, size=None)),
            ],
        ),
    ]
