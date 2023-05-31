import model
from sqlalchemy.orm import Session
import schema



def get_detail_sales_order_crud(db:Session, offset:int=0, limit:int=100):

    detail = db.query(model.SO_Detail).order_by(model.SO_Detail.SO_SYS_NO).offset(offset).limit(limit).all()

    return detail
   




def get_header_sales_order_crud(db:Session,get_id:int):
    header = db.query(model.SO_Header).filter(model.SO_Header.SO_SYS_NO==get_id).order_by(model.SO_Header.SO_SYS_NO).first()
    return header
def get_all_sales_order(db:Session, get_id:int,offset:int=0, limit:int=100):
    header = db.query(model.SO_Header).filter(model.SO_Header.SO_SYS_NO==get_id).order_by(model.SO_Header.SO_SYS_NO).first()
    # detail = db.query(model.SO_Header).filter(model.SO_Detail.so_sys_no==get_id).order_by(model.SO_Header.so_sys_no).all()
    details = db.query(model.SO_Detail).filter(model.SO_Detail.SO_SYS_NO == get_id).order_by(model.SO_Detail.SO_SYS_NO).all()

    # header_schema = SO_Header.from_orm(header)
    # detail_schema = SO_Detail.from_orm(detail)

    # header_schema.Item.append(detail_schema)
    header_schema = schema.SO_Header.from_orm(header)
    detail_schemas = [schema.SO_Detail.from_orm(row) for row in details]

   
    for detail_schema in detail_schemas:
        header_schema.Item.append(detail_schema)

   

   

    return header_schema


    
