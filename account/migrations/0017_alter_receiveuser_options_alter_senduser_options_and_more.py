# Generated by Django 5.0.1 on 2024-02-07 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_remove_senduser_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receiveuser',
            options={'ordering': ['-full_name']},
        ),
        migrations.AlterModelOptions(
            name='senduser',
            options={'ordering': ['-full_name']},
        ),
        migrations.RenameField(
            model_name='receiveuser',
            old_name='fax',
            new_name='account_number',
        ),
        migrations.RenameField(
            model_name='receiveuser',
            old_name='city',
            new_name='other',
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
            name='gender',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='identity_type',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='receiveuser',
            name='marrital_status',
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
        migrations.AddField(
            model_name='receiveuser',
            name='transaction_origin',
            field=models.CharField(blank=True, choices=[('Bank Transfer', 'Bank Transfer'), ('Cash Deposit', 'Cash Deposit'), ('Mobile Money', 'Mobile Money'), ('Other', 'Other')], max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='receiveuser',
            name='transaction_type',
            field=models.CharField(blank=True, choices=[('Bank', 'Bank'), ('Wallet', 'Wallet'), ('Memo Name', 'Memo Name'), ('Other', 'Other')], max_length=40, null=True),
        ),
    ]