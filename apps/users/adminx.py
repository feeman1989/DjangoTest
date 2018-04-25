#!/usr/local/bin/python2.7
# encoding: utf-8
'''
apps.users.adminx -- shortdesc

apps.users.adminx is a description

It defines classes_and_methods

@author:     xiewenbin

@copyright:  2018 organization_name. All rights reserved.

@license:    license

@contact:    xiewenbin1@bigo.sg
@deffield    updated: Updated
'''

import xadmin
from xadmin import views
from .models import EmailVerifyRecord

class BaseSetting(object):
    enable_themes = True 
    use_bootswatch = True
    
class GlobalSetting(object):
    site_title = "天涯明月笙"
    site_footer = "xiewenbin.com"
    menu_style = "accordion"
    
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type']
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
