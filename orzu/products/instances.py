import os


def get_shots_path(instance, filename):
    return os.path.join('products', "product_%s" % str(instance.id), filename)


def get_banners_path(instance, filename):
    return os.path.join('banners', "banner_%s" % str(instance.id), filename)
