# Generated by Django 2.2.7 on 2019-12-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_code', models.CharField(help_text='Code requested by Vendor Team', max_length=10, verbose_name='Site Code')),
                ('delivery_type', models.CharField(choices=[('Single MPLS', 'Single MPLS'), ('Single Internet', 'Single Internet'), ('MPLS + Internet', 'MPLS + Internet'), ('Double MPLS', 'Double MPLS'), ('Double Internet', 'Double Internet')], max_length=64, verbose_name='Type of delivery')),
                ('address', models.CharField(max_length=64, verbose_name='Site Address')),
                ('bandwidth', models.IntegerField(verbose_name='Bandwidth')),
                ('site_classification', models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')], max_length=64, verbose_name='Site Classification:')),
                ('instalation_date', models.CharField(max_length=64, verbose_name='Date when line will be installed on site?')),
                ('local_contact', models.CharField(max_length=64, verbose_name='???Contact to person on site???')),
                ('technical_contact', models.CharField(max_length=64, verbose_name='???Contact to person on site???')),
                ('lan_assistance', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you need assistance with LAN?')),
                ('voip_assistance', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you need VoIP on site?')),
                ('parrarelorhot', models.IntegerField(choices=[(1, 'Parallel move'), (2, 'Hot-cut ')], verbose_name='Parallel move or hot-cut ?')),
                ('company_name', models.CharField(max_length=64, verbose_name='Company Name:')),
                ('city', models.CharField(max_length=64, verbose_name='City:')),
                ('address_2', models.CharField(max_length=64, verbose_name='Address:')),
                ('post_code', models.CharField(max_length=64, verbose_name='Postal Code:')),
                ('country', models.CharField(max_length=64, verbose_name='Country:')),
                ('office_hours', models.IntegerField(choices=[(1, '7-17'), (2, '8-16'), (3, '24/7')], verbose_name='Office Hours:')),
                ('division', models.IntegerField(choices=[(1, 'Road'), (2, 'Air & Sea'), (3, 'Solutions')], verbose_name='Division:')),
            ],
        ),
    ]
