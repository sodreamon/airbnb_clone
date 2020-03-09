import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command create rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms do you want create?"
        )
        # --number를 실행 횟수를 받는 명령어로 씀, --number가 없을 경우 default값으로 1을 준다는 뜻, --number 값은 str이라 type=int 지정

    def handle(self, *args, **options):
        number = options.get("number")
        # number가 있을 때는 number만큼 지정
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        # 모든 User objects
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        # room_models.Room에 "number"만큼의 objects를 만듬
        # lambda 함수로 all_users를 랜덤 선택 시킴
        # randint() int값을 제한
        create_photos = seeder.execute()
        # pk(primary key)를 만듬
        created_clean = flatten(list(create_photos.values()))
        # flatten으로 깨끗하게 정리
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            # pk로 해당 room을 찾음
            for i in range(3, random.randint(10, 17)):
                # loop로 사진 개수를 정하고 만듬
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created"))
