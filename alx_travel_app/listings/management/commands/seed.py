from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed database with sample listings"

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()  # Optional: clear existing data
        for i in range(10):
            Listing.objects.create(
                title=f"Listing {i+1}",
                description=f"This is the description for listing {i+1}.",
                price_per_night=random.randint(50, 500)
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded listings"))