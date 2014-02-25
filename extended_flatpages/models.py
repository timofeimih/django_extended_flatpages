from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from themes.models import Theme

class CMSFlatPage(FlatPage):
    description = models.CharField(verbose_name=_(u"Description"),max_length=100)
    keywords = models.CharField(verbose_name=_(u"Keywords"),max_length=255)
    class_name = models.ForeignKey(Theme)

    class Meta:
        verbose_name = _(u'Static page')
        verbose_name_plural = _(u'Static pages')
