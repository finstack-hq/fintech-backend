# Generated by Django 5.0.1 on 2024-02-06 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_rename_gender_receiveuser_transaction_origin_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receiveuser',
            options={},
        ),
        migrations.AlterModelOptions(
            name='senduser',
            options={},
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='date',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='signature',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='state',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='date',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='identity_image',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='signature',
        ),
        migrations.RemoveField(
            model_name='senduser',
            name='state',
        ),
    ]