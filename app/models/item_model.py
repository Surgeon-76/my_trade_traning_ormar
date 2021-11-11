import ormar

from app.settings.db import (
    database,
    metadata
)


class Item(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, Index=True)
    name: str = ormar.String(max_length=200, Index=True)
    cost_price: float = ormar.Decimal(scale=2, precision=2)
    selling_price: float = ormar.Decimal(scale=2, precision=2)
    quantity: int = ormar.Integer()
    