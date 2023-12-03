# Generated by Django 4.2.5 on 2023-10-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_stepeight_surveylogbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='statementOfOriginality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('teamId', models.IntegerField()),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('inventor1', models.CharField(default='', max_length=1200)),
                ('schoolnamegrade1', models.CharField(default='', max_length=1200)),
                ('sig1', models.CharField(default='', max_length=1200)),
                ('inventor2', models.CharField(default='', max_length=1200)),
                ('schoolnamegrade2', models.CharField(default='', max_length=1200)),
                ('sig2', models.CharField(default='', max_length=1200)),
                ('inventor3', models.CharField(default='', max_length=1200)),
                ('schoolnamegrade3', models.CharField(default='', max_length=1200)),
                ('sig3', models.CharField(default='', max_length=1200)),
                ('inventor4', models.CharField(default='', max_length=1200)),
                ('schoolnamegrade4', models.CharField(default='', max_length=1200)),
                ('sig4', models.CharField(default='', max_length=1200)),
                ('inventor5', models.CharField(default='', max_length=1200)),
                ('schoolnamegrade5', models.CharField(default='', max_length=1200)),
                ('sig5', models.CharField(default='', max_length=1200)),
                ('inventor6', models.CharField(default='', max_length=1200)),
                ('schoolnamegrade6', models.CharField(default='', max_length=1200)),
                ('sig6', models.CharField(default='', max_length=1200)),
            ],
        ),
    ]