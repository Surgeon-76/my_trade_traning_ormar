from datetime import datetime
import ormar

from app.settings.db import (
    database, 
    metadata
)


class Customer(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id = ormar.Integer(primary_key=True, index=True)
    first_name = ormar.String(max_length=100, index=True)
    last_name = ormar.String(max_length=100, index=True)
    username = ormar.String(max_length=50,index=True)
    email = ormar.String(max_length=200, index=True)
    hasheed_password = ormar.String(max_length=50, index=True)
    created_on = ormar.DateTime(default=datetime.now, index=True)
    updated_on = ormar.DateTime(default=datetime.now, onupdate=datetime.now)
    