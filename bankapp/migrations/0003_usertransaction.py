# Generated by Django 2.1.4 on 2019-02-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_auto_20190216_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('userid', models.ForeignKey(on_delete='do_nothing', to='bankapp.BankUser')),
            ],
        ),
    ]
