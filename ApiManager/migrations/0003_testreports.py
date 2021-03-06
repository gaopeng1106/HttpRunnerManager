# Generated by Django 2.0 on 2018-01-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ApiManager', '0002_auto_20180117_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('belong_project', models.CharField(max_length=50)),
                ('belong_module', models.CharField(max_length=50)),
                ('belong_case', models.CharField(max_length=50)),
                ('reports', models.TextField()),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'TestReports',
                'verbose_name': '测试报告',
            },
        ),
    ]
