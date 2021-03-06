# Generated by Django 2.1.5 on 2019-01-31 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='last_login',
            new_name='last_logout',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='total_hours',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
