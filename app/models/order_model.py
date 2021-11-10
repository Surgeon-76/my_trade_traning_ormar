from datetime import datetime
from typing import Optional

import ormar

from app.settings.db import(
    database,
    metadata
)
from app.models.item_model import Item
from app.models.orderitem_model import OrderItem
class Order(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    date_placed: datetime = ormar.DateTime(default=datetime.now(), index=True)
    #item: ormar.ManyToMany(Item)