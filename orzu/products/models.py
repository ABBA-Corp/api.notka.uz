from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from ordered_model.models import OrderedModel
from sorl.thumbnail import get_thumbnail, ImageField

from orzu.products.instances import get_shots_path, get_banners_path


class Product(OrderedModel):
    name = models.CharField(max_length=200)
    packaging_photo = ImageField(_("Изображение пакета"), upload_to=get_shots_path)
    photo = ImageField(_("Изображение"), upload_to=get_shots_path)
    category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE,
                                 verbose_name=_("Категория продукта"))
    description = models.TextField(_("Описание"))
    weight = models.FloatField(_("Масса"), blank=True, null=True)
    artikul = models.CharField(_("Артикул"), max_length=50)
    carbohydrates = models.FloatField(_("Углеводы"))
    calories = models.FloatField(_("Калории"))
    fats = models.FloatField(_("Жиры"))
    country = models.ForeignKey("ProductCountry", on_delete=models.CASCADE,
                                verbose_name=_("Страна изготовления"))
    is_top = models.BooleanField(_("В топе?"))

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")
        order_with_respect_to = "category"

    def __str__(self):
        return "{} | Категория: {}".format(self.name, self.category.title)

    @property
    def thumbnail_preview(self):
        if self.photo:
            _thumbnail = get_thumbnail(self.photo, '150x150', upscale=False, crop="center", quality=100)
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""


class ProductCategory(models.Model):
    title = models.CharField(_('Заголовок'), max_length=100)

    class Meta:
        verbose_name = _('Категория товара')
        verbose_name_plural = _('Категории товаров')

    def __str__(self):
        return "%s" % self.title


class ProductCountry(models.Model):
    name = models.CharField(_('Название страны'), max_length=50)

    class Meta:
        verbose_name = _('Страна изготовления')
        verbose_name_plural = _('Страны изготовления')

    def __str__(self):
        return "%s" % self.name


class Banners(models.Model):
    photo = ImageField(_("Изображение"), upload_to=get_banners_path)

    class Meta:
        verbose_name = _("Баннер")
        verbose_name_plural = _("Баннеры")

    @property
    def thumbnail_preview(self):
        if self.photo:
            _thumbnail = get_thumbnail(self.photo, '350x200', upscale=False, crop="center", quality=100)
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""
