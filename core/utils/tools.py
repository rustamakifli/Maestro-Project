from time import time

from django.conf import settings
from unidecode import unidecode

def get_users_image(instance, filename):
    if "." in filename:
        return "users/%s_%s" % (
            str(time()).replace(".", "_"),
            unidecode(filename.rsplit(".", 1)[0])
            + ".{}".format(filename.rsplit(".", 1)[1]),
        )
    else:
        return "users/%s_%s" % (
            str(time()).replace(".", "_"),
            unidecode(filename),
        )
    
def get_blogs_image(instance, filename):
    if "." in filename:
        return "blogs/%s_%s" % (
            str(time()).replace(".", "_"),
            unidecode(filename.rsplit(".", 1)[0])
            + ".{}".format(filename.rsplit(".", 1)[1]),
        )
    else:
        return "blogs/%s_%s" % (
            str(time()).replace(".", "_"),
            unidecode(filename),
        )
    
def get_services_image(instance, filename):
    if "." in filename:
        return "services/%s_%s" % (
            str(time()).replace(".", "_"),
            unidecode(filename.rsplit(".", 1)[0])
            + ".{}".format(filename.rsplit(".", 1)[1]),
        )
    else:
        return "services/%s_%s" % (
            str(time()).replace(".", "_"),
            unidecode(filename),
        )
