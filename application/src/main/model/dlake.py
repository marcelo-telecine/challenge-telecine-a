from marshmallow import Schema, fields
from main.model import ObjectIdr

class Dlake(Schema):
    _id = ObjectIdr(required=False)
    class Meta:
        fields = ("_id", "Title", "Year", "imdbID", "Type", "Poster")


