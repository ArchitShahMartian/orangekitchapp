# Generated by Django 3.2.12 on 2022-03-27 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20220208_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('primary_address', models.CharField(max_length=300)),
                ('secondary_address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('priority', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('advance', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customer')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(choices=[('Plate Racks', 'Plate Racks'), ('Horizontal Plate Racks(Single)', 'Horizontal Plate Racks(Single)'), ('Horizontal Plate Racks(Double)', 'Horizontal Plate Racks(Double)'), ('Quarter Plate Racks(Double)', 'Quarter Plate Racks(Double)'), ('Quarter Plate Racks(Four Section)', 'Quarter Plate Racks(Four Section)'), ('Soup Bowl(Horizontal)', 'Soup Bowl(Horizontal)'), ('Soup Bowl(Vertical)', 'Soup Bowl(Vertical)'), ('Soup Bowl Racks (W/ Plate)', 'Soup Bowl Racks (W/ Plate)'), ('Katori Racks', 'Katori Racks'), ('Plizner Glass Racks', 'Plizner Glass Racks'), ('Wine Glass Racks', 'Wine Glass Racks'), ('Coffee Mug/Kulud Racks', 'COffee Mug/Kulud Racks'), ('Onion Potato Trolley', 'Onion Potato Trolley'), ('Onion Potato Trolley (W/ Partition)', 'Onion Potato Trolley (W/ Partition)'), ('Wine Holder', 'Wine Holder')], max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('product_name', 'size', 'material')},
        ),
        migrations.CreateModel(
            name='WireSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diameter', models.FloatField(choices=[(3, '3'), (5, '5'), (6, '6')])),
                ('length', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
