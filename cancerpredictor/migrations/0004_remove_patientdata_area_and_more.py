# Generated by Django 4.2.7 on 2023-12-16 09:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cancerpredictor", "0003_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patientdata",
            name="area",
        ),
        migrations.RemoveField(
            model_name="patientdata",
            name="compactness",
        ),
        migrations.RemoveField(
            model_name="patientdata",
            name="concave_points",
        ),
        migrations.RemoveField(
            model_name="patientdata",
            name="concavity",
        ),
        migrations.RemoveField(
            model_name="patientdata",
            name="fractal_dimension",
        ),
        migrations.RemoveField(
            model_name="patientdata",
            name="perimeter",
        ),
        migrations.RemoveField(
            model_name="patientdata",
            name="radius",
        ),
        migrations.RemoveField(
            model_name="patientdata",
            name="smoothness",
        ),
        migrations.RemoveField(
            model_name="patientdata",
            name="symmetry",
        ),
        migrations.RemoveField(
            model_name="patientdata",
            name="texture",
        ),
    ]
