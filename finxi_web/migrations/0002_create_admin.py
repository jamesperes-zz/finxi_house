from django.utils import timezone
from django.db import migrations
from finxi_web.models import BasicUserMod

def create_superuser(apps, schema_editor):
    superuser = BasicUserMod()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.date_joined = timezone.now()
    superuser.username = 'admin'
    superuser.email = 'admin@admin.com'
    superuser.set_password('admin1234')
    superuser.save()


class Migration(migrations.Migration):
    dependencies = [
        ('finxi_web', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]