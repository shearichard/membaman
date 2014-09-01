from django.core.management.base import BaseCommand, CommandError
from members.models import Organisation

class Command(BaseCommand):
    args = '<org_id org_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for org_id in args:
            try:
                poll = Organisation.objects.get(pk=int(org_id))
            except Organisation.DoesNotExist:
                raise CommandError('Organisation "%s" does not exist' % org_id)

            self.stdout.write('Org Name =  "%s"' % poll.name)
