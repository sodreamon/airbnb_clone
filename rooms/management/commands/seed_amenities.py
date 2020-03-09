from django.core.management.base import BaseCommand, CommandError
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command create amenities"

    """ def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that i love you?"
        ) 
        """

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop-friendly workspace",
            "TV",
            "Crib",
            "High chair",
            "Self check-in",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
            "Beachfront",
            "Waterfront",
            "Ski-in/ski-out",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
