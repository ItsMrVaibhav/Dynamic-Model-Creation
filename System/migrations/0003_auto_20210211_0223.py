# Generated by Django 3.1.6 on 2021-02-10 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0002_auto_20210211_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Markssssss',
        ),
    ]