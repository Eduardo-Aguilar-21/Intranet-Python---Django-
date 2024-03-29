# Generated by Django 4.0.2 on 2022-03-26 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notas', '0002_usuario_tipousu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomcarrera', models.CharField(max_length=50)),
                ('descarrera', models.CharField(max_length=50)),
                ('estcarrera', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomcur', models.CharField(max_length=30)),
                ('creditos', models.IntegerField()),
                ('estcur', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomdis', models.CharField(max_length=50)),
                ('estdis', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomest', models.CharField(max_length=50)),
                ('apeest', models.CharField(max_length=50)),
                ('dniest', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=50)),
                ('emailest', models.EmailField(max_length=254)),
                ('estest', models.IntegerField()),
                ('carrera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Notas.carrera')),
                ('distrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Notas.distrito')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Notas.usuario')),
            ],
        ),
    ]
