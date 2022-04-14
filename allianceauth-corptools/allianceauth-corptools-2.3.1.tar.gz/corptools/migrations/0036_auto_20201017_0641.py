# Generated by Django 3.1.1 on 2020-10-17 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0035_auto_20200929_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteraudit',
            name='cache_expire_notif',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='characteraudit',
            name='last_update_notif',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_id', models.BigIntegerField()),
                ('sender_id', models.IntegerField()),
                ('sender_type', models.CharField(choices=[('character', 'character'), ('corporation', 'corporation'), (
                    'alliance', 'alliance'), ('faction', 'faction'), ('other', 'other')], max_length=15)),
                ('notification_text', models.TextField(default=None, null=True)),
                ('timestamp', models.DateTimeField()),
                ('notification_type', models.CharField(max_length=50)),
                ('is_read', models.NullBooleanField(default=None)),
                ('character', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='corptools.characteraudit')),
            ],
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(
                fields=['notification_id'], name='corptools_n_notific_77c7f2_idx'),
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['timestamp'],
                               name='corptools_n_timesta_ca02fe_idx'),
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(
                fields=['notification_type'], name='corptools_n_notific_8ff99b_idx'),
        ),
    ]
