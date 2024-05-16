from django.apps import AppConfig


class GroupsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "groups"


class EventCalendarConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "event_calendar"

    