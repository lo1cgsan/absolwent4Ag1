# Generated by Django 4.1.1 on 2022-09-22 07:39

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
            name='Klasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(default='', max_length=3, verbose_name='nazwa klasy')),
                ('rok_matury', models.IntegerField(default=0, verbose_name='rok matury')),
                ('rok_naboru', models.IntegerField(default=0, verbose_name='rok naboru')),
            ],
        ),
        migrations.CreateModel(
            name='Absolwent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klasa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uczniowie', to='osoby.klasa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
