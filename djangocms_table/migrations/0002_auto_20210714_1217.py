# Generated by Django 3.2.5 on 2021-07-14 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('djangocms_table', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='options',
            field=models.CharField(blank=True, choices=[('highlighted', 'Highlighted')], max_length=100, verbose_name='options'),
        ),
        migrations.AlterField(
            model_name='table',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_table_table', serialize=False, to='cms.cmsplugin'),
        ),
    ]
