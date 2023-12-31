# Generated by Django 4.2.5 on 2023-10-08 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Possibilities',
            fields=[
                ('possibility_id', models.AutoField(primary_key=True, serialize=False)),
                ('phrase', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('reply_id', models.AutoField(primary_key=True, serialize=False)),
                ('phrase', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('match_phrase', models.CharField(max_length=255)),
                ('possibility_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.possibilities')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.questions')),
                ('reply_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.replies')),
            ],
        ),
    ]
