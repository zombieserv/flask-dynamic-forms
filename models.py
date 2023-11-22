import os

from mongoengine import connect
from mongoengine import DynamicDocument, StringField, DynamicField

connect('e_com_db', host=os.getenv("DB_STRING"))


class DynamicForm(DynamicDocument):
    name = StringField(required=True)
    fields = DynamicField()

    @classmethod
    def get_all_forms(cls):
        templates = cls.objects.all()
        return [{"name": template.name, "fields": template.fields} for template in templates]
