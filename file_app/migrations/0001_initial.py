# Generated by Django 3.2.5 on 2022-03-24 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_id', models.IntegerField()),
                ('name', models.CharField(max_length=1000)),
                ('wallet_id', models.CharField(max_length=1000)),
            ],
        ),
    ]
