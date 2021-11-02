from datetime import datetime
from typing import Optional

import ormar

from app.models.order_model import Order
from app.settings.db import (
    database, 
    metadata
)


class Customer(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    first_name: str = ormar.String(max_length=100, index=True)
    last_name: str = ormar.String(max_length=100, index=True)
    username: str = ormar.String(max_length=50, Index=True)
    email: str = ormar.String(max_length=200, index=True)
    hashed_password: str = ormar.String(max_length=50)
    created_on: datetime = ormar.DateTime(default=datetime.now(), index=True)
    updated_on: datetime = ormar.DateTime(default=datetime.now())
    orders: Optional[Order] = ormar.ForeignKey(Order)