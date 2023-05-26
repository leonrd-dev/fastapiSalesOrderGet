from fastapi import APIRouter,Depends,HTTPException,status, FastAPI
import schema
import salesordercrud
import exception
import response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db

app = FastAPI()

router = APIRouter(tags=["Get Sales Order"],prefix="/SalesOrder")

@router.get("/get-sales_order", status_code=status.HTTP_200_OK)
def get_sales_order(db:Session=Depends(get_db)):
    sales_order = salesordercrud.get_all_sales_order_crud(db,0,100)
    if not sales_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return sales_order

@router.get("/get-sales-order/{SO_SYS_NO}", status_code=status.HTTP_200_OK)
def get_sales_order(SO_SYS_NO, db:Session=Depends(get_db)):
    sales_order = salesordercrud.get_one_sales_order_crud(db, SO_SYS_NO)
    if not sales_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return sales_order


