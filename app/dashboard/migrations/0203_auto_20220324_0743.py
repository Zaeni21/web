# Generated by Django 2.2.24 on 2022-03-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0202_auto_20220324_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='acceptance_criteria',
            field=models.TextField(blank=True, default='', help_text='Acceptance criteria'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='ressources',
            field=models.TextField(blank=True, default='', help_text='Ressources'),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='custom_description',
            field=models.TextField(blank=True, default='', help_text='The description of the Bounty'),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='custom_description_rich',
            field=models.TextField(blank=True, default='', help_text='HTML rich description'),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='custom_title',
            field=models.CharField(blank=True, default='', help_text='The title of the Bounty', max_length=200),
        ),
    ]
