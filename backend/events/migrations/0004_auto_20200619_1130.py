# Generated by Django 2.2.10 on 2020-06-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20191004_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['-event'], 'verbose_name': 'talk'},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='description_es',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='title_es',
        ),
        migrations.RenameField(
            model_name='talk',
            old_name='description',
            new_name='description_es',
        ),
        migrations.RenameField(
            model_name='talk',
            old_name='name',
            new_name='name_es',
        ),
        migrations.AddField(
            model_name='event',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='description_en',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='description_pt',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='name_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
