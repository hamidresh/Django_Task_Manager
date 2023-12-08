# Generated by Django 4.2.7 on 2023-11-29 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=20)),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')], max_length=20)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='taskpage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_type', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskpage.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskpage.user')),
            ],
        ),
    ]