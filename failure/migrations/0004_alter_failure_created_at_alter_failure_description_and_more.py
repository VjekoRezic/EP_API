# Generated by Django 4.2.4 on 2023-08-23 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workcenter', '0001_initial'),
        ('workorder', '0002_alter_workorder_start_time'),
        ('failure', '0003_remove_failure_solved_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failure',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='The timestamp when the failure was created.', verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='failure',
            name='description',
            field=models.TextField(help_text='A detailed description of the failure.', verbose_name='failure description'),
        ),
        migrations.AlterField(
            model_name='failure',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Indicates if the failure is marked as deleted.', verbose_name='is_deleted'),
        ),
        migrations.AlterField(
            model_name='failure',
            name='name',
            field=models.CharField(help_text='The name of the failure.', max_length=150, verbose_name='failure name'),
        ),
        migrations.AlterField(
            model_name='failure',
            name='reported_by',
            field=models.ForeignKey(help_text='The user who reported the failure (Foreign Key to User model).', on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL, verbose_name='reported by'),
        ),
        migrations.AlterField(
            model_name='failure',
            name='updated_at',
            field=models.DateTimeField(help_text='The timestamp when the failure was last updated.', null=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='failure',
            name='work_center',
            field=models.ForeignKey(help_text='The work center where the failure occurred (Foreign Key to WorkCenter model).', on_delete=django.db.models.deletion.CASCADE, to='workcenter.workcenter', verbose_name='work center'),
        ),
        migrations.AlterField(
            model_name='failure',
            name='work_order',
            field=models.ForeignKey(help_text='The associated work order (Foreign Key to WorkOrder model).', null=True, on_delete=django.db.models.deletion.CASCADE, to='workorder.workorder', verbose_name='work order'),
        ),
    ]
