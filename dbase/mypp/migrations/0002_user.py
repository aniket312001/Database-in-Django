# Generated by Django 3.1.3 on 2021-09-06 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypp.company')),
            ],
        ),
    ]
