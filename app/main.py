from fastapi import FastAPI

from app.routers import (
    customers,
    items,
    orders,
    orderitems
)
from app.settings.db import (
    database,
    metadata,
    engine
)

app = FastAPI(
    title="Супер-пупер МеГаШоП v 2.2E+5",
    description="Второй блин не лучше первого...- комкуется не хуже)))"
)

metadata.create_all(engine)

app.state.database = database

# app.include_router(customers.customers_route)
# app.include_router(orders.order_route)
# app.include_router(items.items_route)
# app.include_router(orderitems.links_route)