# Generated by Django 3.2.6 on 2021-09-11 04:55

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grocery', '0005_alter_cleaning_subdepartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='U_Id',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
