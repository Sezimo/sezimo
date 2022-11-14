from django.apps import apps

def get_apps():
    """Get all of the apps loaded by Django"""
    app_list = list(apps.app_configs.keys())
    app_list.append(None) # Add None option for all.
    return [(app, app) for app in app_list]