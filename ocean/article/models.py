# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from cmdb.models import *
# Create your models here.


# 知识库文章 modules
class Article(models.Model):
    title = models.CharField(max_length=128)
    keyword = models.CharField(max_length=128)
    #content = RichTextField()
    content = RichTextUploadingField()
    app_system = models.ForeignKey(AppSystem, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.title