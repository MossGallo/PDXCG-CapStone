# Generated by Django 4.0.5 on 2022-06-07 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_climbevent_delete_climb'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbevent',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='climb_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
