from typing import List

from fastapi import APIRouter

from app.models.custommer_model import Customer


customers_route = APIRouter(
    prefix="/customers",
    tags=['Покупатели:']
)


@customers_route.get("/", summary=('Показать всех'))
async def read_customers():
    return await Customer.objects.all()


@customers_route.post("/")
async def create_customers(item: Customer):
    return await item.save()




# @customers_route.get("/", summary=('Показать всех'),
#                      response_model=List[schemas.Customer])
# def read_customers(skip: int = 0, limit: int = 100,
#                    db: Session = Depends(get_db)):
#     customers = crud.get_customers(db, skip=skip, limit=limit)
#     return customers