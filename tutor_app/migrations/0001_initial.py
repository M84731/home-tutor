# Generated by Django 3.1.2 on 2020-12-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booknow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('sub', models.CharField(max_length=100)),
                ('clas', models.CharField(max_length=100)),
                ('board', models.CharField(max_length=100)),
                ('cit', models.CharField(max_length=100)),
                ('sid', models.IntegerField()),
                ('tid', models.IntegerField()),
                ('dof', models.DateField()),
                ('day', models.IntegerField()),
                ('hrb', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='formtutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('addr', models.TextField(max_length=300)),
                ('pins', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('exp', models.IntegerField()),
                ('doj', models.DateField()),
                ('online', models.CharField(max_length=100)),
                ('hour', models.IntegerField()),
                ('img', models.FileField(upload_to='')),
                ('tutoring', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=200)),
                ('fun', models.CharField(max_length=200)),
                ('demo', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='stregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('ph', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ttregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('ph', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
    ]
