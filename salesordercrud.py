import modelorm
from sqlalchemy.orm import Session



def get_all_sales_order_crud(db:Session, offset:int=0, limit:int=100):
    return db.query(modelorm.SO_Header).order_by(modelorm.SO_Header.so_sys_no).offset(offset).limit(limit).all()

def get_one_sales_order_crud(db:Session,get_id:int):
    return  db.query(modelorm.SO_Header).filter(modelorm.SO_Header.so_sys_no==get_id).first()
    
def post_sales_order(db:Session, payload:modelorm.SO_Header):
    return modelorm.SO_Header(**payload.dict())

def delete_sales_order(db:Session,get_id:int):
    return db.query(modelorm.SO_Header).filter(modelorm.SO_Header.so_sys_no==get_id).delete(synchronize_session=False)
    
def put_sales_order(db:Session,payload:modelorm.SO_Header, get_id:int):
    edit_sales_order= db.query(modelorm.SO_Header).filter(modelorm.SO_Header.so_sys_no==get_id)
    edit_sales_order.update(payload.dict())
    messages_sales_order = edit_sales_order.first()
    return edit_sales_order, messages_sales_order

def patch_sales_order(db:Session, get_id:int):
    return db.query(modelorm.SO_Header).filter(modelorm.SO_Header.so_sys_no==get_id).first()
