# Generated by Django 5.1.3 on 2024-11-05 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constutionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constutionapp.section')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='constutionapp.chapter'),
        ),
    ]
