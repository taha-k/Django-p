import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
import random
import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat(name='Python',views=3,likes=3)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",views=random.randint(0,100))

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",views=random.randint(0,100))

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",views=random.randint(0,100))

    django_cat = add_cat(name="Django",views=3)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",views=random.randint(0,100))

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",views=random.randint(0,100))

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",views=random.randint(0,100))

    frame_cat = add_cat(name="Other Frameworks")

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",views=random.randint(0,100))

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",views=random.randint(0,100))

    frame_cat2 = add_cat(name="Python")

    add_page(cat=frame_cat2,
        title="Bottle2",
        url="http://bottlepy.org/docs/dev/",views=random.randint(0,100))

    add_page(cat=frame_cat2,
        title="Flask2",
        url="http://flask.pocoo.org",views=random.randint(0,100))

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,views=4,likes=4):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes=likes
    c.views=views
    c.save()
    print "category"
    print c
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()