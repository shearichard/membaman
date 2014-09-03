from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from members.models import Organisation


class Command(BaseCommand):
    help = 'Does some very user specific data input from what was previously a spreadsheet'

    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj

    def handle(self, *args, **options):
        org_id = 1
        self.stdout.write('About to start conversion')
        with transaction.atomic():
            for org_id in args:
                try:
                    org = Organisation.objects.get(pk=int(org_id))
                except Organisation.DoesNotExist:
                    raise CommandError('Organisation "%s" does not exist' % org_id)
            org.name = org.name + org_id
            self.save_or_locate(org)

            self.stdout.write('Org Name =  "%s"' % org.name)

