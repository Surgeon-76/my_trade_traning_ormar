

import ormar

from app.settings.db import (
    database,
    metadata
)


class OrderItem(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    quantity: int = ormar.SmallInteger()
