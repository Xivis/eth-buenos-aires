# Generated by Django 2.1.3 on 2019-08-07 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('meetup_url', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField()),
                ('place_name', models.CharField(blank=True, max_length=255, null=True)),
                ('place_street', models.CharField(blank=True, max_length=255, null=True)),
                ('place_number', models.CharField(blank=True, max_length=255, null=True)),
                ('place_city', models.CharField(blank=True, max_length=255, null=True)),
                ('place_map_url', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'event',
            },
        ),
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.FileField(upload_to='')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'verbose_name': 'event photo',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'sponsor',
            },
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('speaker', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.TimeField()),
                ('language', models.CharField(blank=True, choices=[('SPANISH', 'spanish'), ('ENGLISH', 'english')], max_length=255, null=True)),
                ('level', models.CharField(blank=True, choices=[('INITIAL', 'initial'), ('MEDIUM', 'medium'), ('ADVANCED', 'advanced')], max_length=255, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'verbose_name': 'talk',
            },
        ),
        migrations.CreateModel(
            name='TalkMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(upload_to='')),
                ('talk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Talk')),
            ],
            options={
                'verbose_name': 'talk material',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(to='events.Sponsor'),
        ),
    ]
