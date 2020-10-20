from marshmallow import Schema
from main.model import ObjectIdr

class Collection(Schema):
    _id = ObjectIdr()
    class Meta:
        fields = ("_id", "imdb", "genre", "description")
