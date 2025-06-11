from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('category', models.CharField(choices=[('Reminder', 'Reminder'), ('Update', 'Update'), ('Transaction', 'Transaction')], max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('recipients', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date', '-time'],
            },
        ),
    ]
