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