# Generated by Django 4.2.5 on 2023-09-09 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(db_column='Usuarios_id', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.usuarios')),
            ],
            options={
                'db_table': 'Temas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('creation_fecha', models.DateTimeField(auto_now_add=True)),
                ('tema', models.ForeignKey(db_column='Temas_id', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.temas')),
                ('user', models.ForeignKey(db_column='Usuarios_id', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.usuarios')),
            ],
            options={
                'db_table': 'respuestas',
                'managed': True,
            },
        ),
    ]