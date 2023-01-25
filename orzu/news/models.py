from django.db import models
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail, ImageField
from django.utils.translation import gettext_lazy as _

from orzu.news.instances import get_news_path


class News(models.Model):
    photo = ImageField(_("Изображение"), upload_to=get_news_path)
    landscape_photo = ImageField(_("Альбомное изображение"))
    title_uz = models.CharField(_("Заголовок uz"), max_length=150)
    title_en = models.CharField(_("Заголовок en"), max_length=150, null=True, blank=True)
    title_ru = models.CharField(_("Заголовок ru"), max_length=150, null=True, blank=True)
    description_uz = models.TextField(_("Описание uz"))
    description_en = models.TextField(_("Описание en"), null=True, blank=True)
    description_ru = models.TextField(_("Описание ru"), null=True, blank=True)
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
