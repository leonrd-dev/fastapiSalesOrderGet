import modelorm
from sqlalchemy.orm import Session



def get_all_sales_order_crud(db:Session, offset:int=0, limit:int=100):
    return db.query(modelorm.SO_Header).order_by(modelorm.SO_Header.so_sys_no).offset(offset).limit(limit).all()

def get_one_sales_order_crud(db:Session,get_id:int):
    return  db.query(modelorm.SO_Header).filter(modelorm.SO_Header.so_sys_no==get_id).first()
    
