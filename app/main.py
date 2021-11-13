from fastapi import FastAPI
from app.models.custommer_model import Customer

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


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()

@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
print(Customer.get_column_alias)
app.include_router(customers.customers_route)
# app.include_router(orders.order_route)
# app.include_router(items.items_route)
# app.include_router(orderitems.links_route)
