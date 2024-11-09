import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Fake Pop Script
import random
from first_app.models import Topic, WebPage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the web page
        webpg = WebPage.objects.get_or_create(
            topic=top, name=fake_name, url=fake_url)[0]

        # Create a fake access record for that web page
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print('Populating complete!')
