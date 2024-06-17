# Generated by Django 5.0.6 on 2024-06-11 11:58

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='pub_id',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='pub_name',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='sub_id',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='sub_name',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='sub_time',
        ),
        migrations.AddField(
            model_name='subscription',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='pub',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pubs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subscription',
            name='sub',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('pub', 'sub'), name='unique_subscription'),
        ),
    ]