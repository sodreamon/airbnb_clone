from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command create users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users do you want create?"
        )
        # --number를 실행 횟수를 받는 명령어로 씀, --number가 없을 경우 default값으로 1을 준다는 뜻, --number 값은 str이라 type=int 지정

    def handle(self, *args, **options):
        number = options.get("number")
        # number가 있을 때는 number만큼 지정
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        # User(AbstractUser)의 staff와 superuser BooleanField를 False 값으로 고정시킨 나머지에 fake data를 줌
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Users created"))
