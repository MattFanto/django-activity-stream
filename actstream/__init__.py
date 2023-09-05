try:
    from actstream.signals import action
except:
    pass

try:
    import django
except:
    pass
else:
    if django.VERSION < (3, 2):
        default_app_config = 'actstream.apps.ActstreamConfig'


__version__ = '1.4.2'
__author__ = 'Asif Saif Uddin, Justin Quick <justquick@gmail.com>'
