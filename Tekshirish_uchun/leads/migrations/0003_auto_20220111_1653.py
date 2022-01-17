# Generated by Django 3.1.4 on 2022-01-11 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20220111_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.userprofile'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.userprofile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_organiser',
            field=models.BooleanField(default=False),
        ),
    ]
