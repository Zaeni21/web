# Generated by Django 2.2.4 on 2020-04-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0012_tokenrequest_bounty_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulktransfercoupon',
            name='make_paid_for_first_minutes',
            field=models.IntegerField(default=0),
        ),
    ]