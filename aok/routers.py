"""
No need to import modules
"""

class Router:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

''' These are commented out for simplier use with sqlite3 db.
    route_django_labels = [ "admin", "auth", "contenttypes", "sessions", ]
    route_app_labels = [ "aok", "communities", "communities", "news" ]

    def db_for_read(self, model):
        """
        Attempts to read auth and contenttypes models go to default.
        """
        if model._meta.app_label in self.route_django_labels:
            return "default"
        elif model._meta.app_label in self.route_app_labels:
            return "aok_reader"
        return None

    def db_for_write(self, model):
        """
        Attempts to write auth and contenttypes models go to default.
        """
        if model._meta.app_label in self.route_django_labels:
            return "default"
        elif model._meta.app_label in self.route_app_labels:
            return "aok_writer"
        return None

    def allow_relation(self, obj1, obj2):
        """
        Allow relations if a model in the auth or contenttypes apps is involved.
        """
        if (
            obj1._meta.app_label in self.route_django_labels
            or obj2._meta.app_label in self.route_django_labels
            
            or obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the django system apps only appear in the 'default' database.
        """
        if app_label in self.route_django_labels:
            return db == "default"
        elif app_label in self.route_app_labels:
            return db == "default"
        return None
'''