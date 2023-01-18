from django.db import models
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail, ImageField
from django.utils.translation import gettext_lazy as _

from orzu.news.instances import get_news_path


class News(models.Model):
    photo = ImageField(_("Изображение"), upload_to=get_news_path)
    landscape_photo = ImageField(_("Альбомное изображение"))
    title = models.CharField(_("Заголовок"), max_length=150)
    description = models.TextField(_("Описание"))
    created_on = models.DateField(_("Создано"), auto_now_add=True)

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")

    @property
    def thumbnail_preview(self):
        if self.photo:
            _thumbnail = get_thumbnail(self.photo, '300x350', upscale=False, crop="center", quality=100)
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""
