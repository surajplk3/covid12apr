# Generated by Django 3.0.3 on 2020-04-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='covid_data_anal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cumulative_conf', models.ImageField(blank=True, upload_to='graphs')),
            ],
        ),
        migrations.AddField(
            model_name='covid_ind',
            name='day_increment_active',
            field=models.IntegerField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='covid_ind',
            name='day_increment_confirmed',
            field=models.IntegerField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='covid_ind',
            name='day_increment_deaths',
            field=models.IntegerField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='covid_ind',
            name='day_increment_recovered',
            field=models.IntegerField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='covid_ind',
            name='deaths',
            field=models.IntegerField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='covid_ind',
            name='recovered',
            field=models.IntegerField(db_index=True, null=True),
        ),
    ]