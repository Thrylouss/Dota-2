# Generated by Django 5.0.6 on 2024-09-27 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='attributes/')),
            ],
            options={
                'verbose_name': 'Attribute',
                'verbose_name_plural': 'Attributes',
            },
        ),
        migrations.CreateModel(
            name='DatabaseState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_data_loaded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='news/')),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('complexity', models.PositiveSmallIntegerField()),
                ('advice', models.TextField()),
                ('history', models.TextField()),
                ('attack', models.JSONField()),
                ('defense', models.JSONField()),
                ('mobility', models.JSONField()),
                ('hp', models.JSONField()),
                ('mp', models.JSONField()),
                ('attributes', models.JSONField()),
                ('attack_type', models.CharField(choices=[('melee', 'Ближний бой'), ('ranged', 'Дальний бой')], max_length=6)),
                ('talents', models.JSONField()),
                ('description', models.TextField()),
                ('video', models.CharField(blank=True, max_length=2222, null=True)),
                ('image', models.CharField(blank=True, max_length=2222, null=True)),
                ('icon', models.CharField(blank=True, max_length=2222, null=True)),
                ('main_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attribute')),
            ],
            options={
                'verbose_name': 'Hero',
                'verbose_name_plural': 'Heroes',
            },
        ),
        migrations.CreateModel(
            name='Aspects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.CharField(blank=True, max_length=2222, null=True)),
                ('ability_description', models.TextField(blank=True, null=True)),
                ('ability_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ability_icon', models.CharField(blank=True, max_length=2222, null=True)),
                ('full_description', models.TextField(blank=True, null=True)),
                ('hero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hero')),
            ],
            options={
                'verbose_name': 'Aspect',
                'verbose_name_plural': 'Aspects',
            },
        ),
        migrations.CreateModel(
            name='HeroRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField()),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hero')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.role')),
            ],
            options={
                'verbose_name': 'Hero role',
                'verbose_name_plural': 'Hero roles',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=2222, null=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('damage_type', models.CharField(blank=True, choices=[('physical', 'Physical'), ('magical', 'Magical'), ('pure', 'Pure')], max_length=20, null=True)),
                ('cooldown', models.CharField(max_length=100)),
                ('mana_cost', models.CharField(max_length=100)),
                ('spell_effects', models.JSONField()),
                ('video', models.CharField(blank=True, max_length=2222, null=True)),
                ('tip', models.TextField(blank=True, null=True)),
                ('is_innate', models.BooleanField(default=False)),
                ('ability_is_granted_by_shard', models.BooleanField(default=False)),
                ('ability_is_granted_by_scepter', models.BooleanField(default=False)),
                ('ability_has_scepter', models.BooleanField(default=False)),
                ('ability_has_shard', models.BooleanField(default=False)),
                ('scepter_description', models.TextField(blank=True, null=True)),
                ('shard_description', models.TextField(blank=True, null=True)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hero')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
    ]
