# -*- coding: utf-8 -*-
from django.contrib import admin
# Original flatpages admin
from models import CMSFlatPage 
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm
# For translation
from django.conf import settings
# For CKEditor
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext_lazy as _
from themes.models import Theme

class CustomFlatpageForm(FlatpageForm):
    locals()['content'] = forms.CharField(widget=CKEditorWidget(), required=False, label=_(u'Content'))
    description = forms.CharField(required=False, label=_(u'Description'))
    keywords = forms.CharField(required=False, label=_(u'Keywords'))
    class_name = forms.ModelChoiceField(queryset=Theme.objects.all(), label=_(u'Class'))
    
    class Meta:
        model = CMSFlatPage


class CustomFlatPageAdmin(FlatPageAdmin): 
    form = CustomFlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', 'keywords', 'description', 'class_name')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )

admin.site.unregister(FlatPage) 
admin.site.register(CMSFlatPage, CustomFlatPageAdmin)