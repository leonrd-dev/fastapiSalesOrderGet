from fastapi import APIRouter,Depends,HTTPException,status
import salesordercrud
import exception
import schema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
import response

router = APIRouter(tags=["Get Sales Order"],prefix="/api/general")

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

@router.post("/create-sales-order", status_code=201)
def post_sales_order(payload:schema.SO_Header,db:Session=Depends(get_db)):
    try:
        new_sales_order = salesordercrud.post_sales_order(db, payload)
        db.add(new_sales_order)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=exception(409))
    db.refresh(new_sales_order)
    return response.payload(exception(201), new_sales_order)

@router.delete("/delete-sales-order/{SO_SYS_NO}", status_code=202)
def delete_sales_order(SO_SYS_NO, db:Session=Depends(get_db)):
    deleted_sales_order = salesordercrud.delete_sales_order(db,SO_SYS_NO)
    if not deleted_sales_order:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=exception(404))
    db.commit()
    return response.payload(exception(202), deleted_sales_order)

@router.put("/update-sales-order/{SO_SYS_NO}", status_code=202)
def put_sales_order(payload:schema.SO_Header, SO_SYS_NO,db:Session=Depends(get_db)):
    update_sales_order, update_data_new  = salesordercrud.put_sales_order(db,payload, SO_SYS_NO)
    if not update_sales_order:
        db.commit()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=exception(404))
    db.commit()
    db.refresh(update_data_new)
    return response.payload(exception(200), update_data_new)

