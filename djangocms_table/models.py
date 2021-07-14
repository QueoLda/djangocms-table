from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from django.conf import settings

DJANGOCMS_TABLE_OPTIONS = getattr(
    settings,
    "DJANGOCMS_TABLE_OPTIONS",
    (("highlighted", _("Highlighted")),),
)


class Table(CMSPlugin):
    """
    Table plugin
    """

    name = models.CharField(_("name"), max_length=256)

    headers_top = models.PositiveSmallIntegerField(_("top"), default=1)
    headers_left = models.PositiveSmallIntegerField(_("left"), default=0)
    headers_bottom = models.PositiveSmallIntegerField(_("bottom"), default=0)
    options = models.CharField(_("options"), choices=DJANGOCMS_TABLE_OPTIONS, blank=True, max_length=100)
    table_data = models.TextField(_("table data"))

    def __str__(self):
        return self.name

    search_fields = ("name", "table_data")
