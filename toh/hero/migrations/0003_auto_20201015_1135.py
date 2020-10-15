# Generated by Django 3.1.2 on 2020-10-15 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_hero_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hero',
            name='age',
            field=models.IntegerField(default=25),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader_set', to='hero.hero')),
                ('members', models.ManyToManyField(related_name='teams', to='hero.Hero')),
            ],
        ),
    ]
