# Generated by Django 3.2.17 on 2023-02-06 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_feature_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='layer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='test_app.layer'),
        ),
    ]
