from fastapi import APIRouter,Depends,HTTPException,status
import schema
import salesordercrud
import exception
import response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db


router = APIRouter(tags=["Get Sales Order"],prefix="/SalesOrder")

@router.get("/get-sales_order", status_code=200)
def get_sales_order(db:Session=Depends(get_db)):
    sales_order = salesordercrud.get_all_sales_order_crud(db,0,100)
    if not sales_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=exception(404))
    return response.payloads(exception(200),sales_order)

@router.get("/get-sales-order/{SO_SYS_NO}", status_code=200)
def get_sales_order(SO_SYS_NO, db:Session=Depends(get_db)):
    sales_order = salesordercrud.get_one_sales_order_crud(db, SO_SYS_NO)
    if not sales_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=exception(404))
    return response.payload(exception(200),sales_order)



