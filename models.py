import os

from mongoengine import connect
from mongoengine import DynamicDocument, StringField, DynamicField

DB_HOST = "mongodb://{}:{}@mongodb:27017".format(
    os.getenv('MONGODB_INITDB_ROOT_USERNAME'),
    os.getenv('MONGODB_INITDB_ROOT_PASSWORD'))

connect('e_com_db', host=DB_HOST)


class DynamicForm(DynamicDocument):
    name = StringField(required=True)
    fields = DynamicField()

    @classmethod
    def get_all_forms(cls):
        templates = cls.objects.all()
        return [{"name": template.name, "fields": template.fields} for template in templates]
