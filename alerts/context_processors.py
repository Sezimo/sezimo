from .models import Notification
from datetime import datetime
from django.urls import Resolver404, resolve
from django.db.models import Q

def notification_context_processor(request):
    """
    Adds the active notifications to the context
    """
    # Clear out old announcements.
    Notification.objects.filter(display=True, expiration_date__lte=datetime.now().astimezone()).update(display=False)

    # Get app name for app based announcements
    try:
        path = resolve(request.path)
        app = path.app_name
        if app: # App can be a blank string
            cache_name = f'{app}_notification_cache'
        else:
            cache_name = 'notification_cache'
    except (AttributeError, Resolver404):
        app = None
        cache_name = 'notification_cache'

    # Get the announcements and return
    # Need to use Q objects because None doesn't work in an app__in=[]
    notification = Notification.objects.filter(Q(display=True) & (Q(app=app) | Q(app=None)))
    return {
        'notifications': notification,
        # Caches are indeed global, so need to pass an argument to the cache tag.
        'app_announcement_cache': cache_name
    }