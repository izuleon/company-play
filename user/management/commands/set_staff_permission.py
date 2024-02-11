from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Fills 'Staff' group with permissions to add and view all models."

    def handle(self, *args, **options):
        # Get the 'Staff' group
        staff_group, _ = Group.objects.get_or_create(name="Staff")

        # Find all model content types
        content_types = ContentType.objects.exclude(
            model__in=[
                "permission",
                "logentry",
                "contenttype",
            ]
        )

        # Grant add and view permissions for all models
        for content_type in content_types:
            add_permission = Permission.objects.get(
                name="Can add %s" % content_type.model
            )
            view_permission = Permission.objects.get(
                name="Can view %s" % content_type.model
            )
            staff_group.permissions.add(add_permission, view_permission)

        self.stdout.write(self.style.SUCCESS('Permissions added to the "Staff" group.'))
