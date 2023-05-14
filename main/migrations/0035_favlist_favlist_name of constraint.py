# Generated by Django 4.1.5 on 2023-02-15 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_delete_fav'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='favlist',
            constraint=models.UniqueConstraint(fields=('user', 'item'), name='name of constraint'),
        ),
    ]