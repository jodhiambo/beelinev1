# Generated by Django 3.0.8 on 2020-08-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20200806_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age_group',
            field=models.CharField(blank=True, choices=[('Below 18 Yrs', 'Below 18 Yrs'), ('18-35 Yrs', '18-35 Yrs'), ('Above 35 Yrs', 'Above 35 Yrs')], default='', max_length=50, null=True),
        ),
    ]