# Generated by Django 4.0.5 on 2022-06-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_atenciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examenes',
            fields=[
                ('idExamen', models.AutoField(primary_key=True, serialize=False)),
                ('nombreExamen', models.CharField(max_length=25)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('idMedicamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombreMedicamento', models.CharField(max_length=25)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='atenciones',
            name='anamnesis',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='atenciones',
            name='diagnostico',
            field=models.TextField(max_length=200),
        ),
        migrations.AddField(
            model_name='atenciones',
            name='examenes',
            field=models.ManyToManyField(to='libreria.examenes'),
        ),
        migrations.AddField(
            model_name='atenciones',
            name='medicamento',
            field=models.ManyToManyField(to='libreria.medicamentos'),
        ),
    ]
