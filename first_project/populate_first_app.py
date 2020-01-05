import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Games', 'Marketplace', 'News', 'Search', 'Social']

def addTopic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = addTopic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        webPg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        accRec = AccessRecord.objects.get_or_create(name=webPg, dateVisit=fake_date)[0]

if __name__=='__main__':
    print('Populating script')
    populate(20)
    print('Populating complete!')


