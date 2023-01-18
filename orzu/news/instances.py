import os


def get_news_path(instance, filename):
    return os.path.join('news', "news_%s" % str(instance.id), filename)
