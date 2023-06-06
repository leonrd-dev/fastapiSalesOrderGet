from fastapi import APIRouter,Depends,HTTPException,status
import schema
import salesordercrud
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db


router = APIRouter(tags=["Get Sales Order"],prefix="/AFS")

@router.get("/get-header-sales-orders/{SO_SYS_NO}", response_model = schema.SO_Header,status_code=status.HTTP_200_OK)
def get_sales_orders(SO_SYS_NO, db:Session=Depends(get_db)):
    sales_order = salesordercrud.get_header_sales_order_crud(db,SO_SYS_NO)
    if not sales_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return sales_order

@router.get("/get-detail-sales-order/{SO_SYS_NO}", status_code=status.HTTP_200_OK)
def get_sales_orders(SO_SYS_NO, db:Session=Depends(get_db)):
    sales_order = salesordercrud.get_detail_sales_order_crud(db,SO_SYS_NO)
    if not sales_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return sales_order

@router.get("/SalesOrderSelect/{SO_SYS_NO}/",response_model = schema.SO_Header,status_code=status.HTTP_200_OK)
def get_sales_order(SO_SYS_NO, db:Session=Depends(get_db)):
    sales_order = salesordercrud.get_all_sales_order(db, SO_SYS_NO)
    if not sales_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return sales_order


RouterSO = router


