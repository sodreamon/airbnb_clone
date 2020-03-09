from django.core.management.base import BaseCommand, CommandError
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command create facilities"

    """ def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that i love you?"
        ) 
        """

    def handle(self, *args, **options):
        facilities = [
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
