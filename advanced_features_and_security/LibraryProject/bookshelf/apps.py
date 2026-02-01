# bookshelf/apps.py
from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.contrib.contenttypes.models import ContentType

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        post_migrate.connect(create_groups, sender=self)


def create_groups(sender, **kwargs):
    from .models import Book

    # Define group names
    groups = ['Admins', 'Editors', 'Viewers']

    for group_name in groups:
        group, created = Group.objects.get_or_create(name=group_name)

    # Assign permissions
    content_type = ContentType.objects.get_for_model(Book)

    # Admins: all permissions
    admin_perms = Permission.objects.filter(content_type=content_type)
    Group.objects.get(name='Admins').permissions.set(admin_perms)

    # Editors: can_create and can_edit
    editor_perms = Permission.objects.filter(
        codename__in=['can_create', 'can_edit']
    )
    Group.objects.get(name='Editors').permissions.set(editor_perms)

    # Viewers: can_view only
    viewer_perms = Permission.objects.filter(codename='can_view')
    Group.objects.get(name='Viewers').permissions.set(viewer_perms)
