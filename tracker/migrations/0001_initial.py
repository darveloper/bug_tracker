# Generated by Django 3.0.7 on 2020-06-20 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Done', 'Done'), ('Invalid', 'Invalid')], default='New', max_length=100)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
                ('completed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_by', to=settings.AUTH_USER_MODEL)),
                ('filed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filed_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
