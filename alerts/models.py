from django.db import models
from root.utils.func.get_apps import get_apps
# Create your models here.
class Notification(models.Model):
    """
    Model to hold global announcements
    """
    # Bootstrap CSS Class that will be passed to the template. 
    COLOR_CHOICES = [('primary', 'primary '), ('success','success'), ('warning','warning'), ('danger', 'danger')]

    admin_panel_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Name")
    display = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(null=True, blank=True)
    color = models.CharField(max_length=15, choices=COLOR_CHOICES)
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=False, null=False) # replace this with a WYSIWYG later
    app = models.CharField(max_length=30, null=True, blank=True, choices=get_apps(), help_text="Which app to show announcement on. None will show on all.")
    def __str__(self):
        return f'{self.admin_panel_name} ({self.color.upper()}) {f"({self.app})" if self.app else ""}'

    class Meta:
        verbose_name = "Annoucement"