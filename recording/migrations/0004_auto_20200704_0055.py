# Generated by Django 3.0.7 on 2020-07-03 23:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recording', '0003_auto_20200704_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voice',
            name='collective',
            field=models.FileField(default='none', upload_to='C:\\Users\\Aubrey\\Desktop\\semester3\\code\\project-NChant\\nchant\\media'),
        ),
        migrations.AlterField(
            model_name='voice',
            name='image',
            field=models.ImageField(default='C:\\Users\\Aubrey\\Desktop\\semester3\\code\\project-NChant\\nchant\\mediadefault.jpg', upload_to='C:\\Users\\Aubrey\\Desktop\\semester3\\code\\project-NChant\\nchant\\media'),
        ),
        migrations.AlterField(
            model_name='voice',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 23, 55, 8, 105952, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='voice',
            name='seed',
            field=models.FileField(default='none', upload_to='C:\\Users\\Aubrey\\Desktop\\semester3\\code\\project-NChant\\nchant\\media'),
        ),
    ]
