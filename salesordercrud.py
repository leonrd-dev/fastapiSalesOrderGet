import model
from sqlalchemy.orm import Session
from sqlalchemy import label, func
from fastapi.encoders import jsonable_encoder
import schema
from dataclasses import asdict



def get_detail_sales_order_crud(db:Session, get_id = int):

    detail = db.query(model.SO_Detail.ITEM_CODE,
                      model.Item.ITEM_NAME,
                      model.SO_Detail.QTY_DEMAND,
                      model.SO_Detail.PRICE,
                      model.SO_Detail.DISC_PERCENT,
                      model.SO_Detail.DISC_AMOUNT,
                      label('LineTotal', func.sum(model.SO_Detail.QTY_DEMAND*(model.SO_Detail.PRICE - model.SO_Detail.DISC_REQ_AMOUNT))),
                      model.SO_Detail.QTY_SUPPLY
  
    ).join(model.Item, model.SO_Detail.ITEM_CODE == model.Item.ITEM_CODE, isouter=True
    ).filter(model.SO_Detail.SO_SYS_NO == get_id
    ).group_by(
        model.SO_Detail.SO_SYS_NO,
        model.SO_Detail.ITEM_CODE,  
        model.Item.ITEM_NAME,
        model.SO_Detail.QTY_DEMAND,
        model.SO_Detail.PRICE,
        model.SO_Detail.DISC_PERCENT,
        model.SO_Detail.DISC_AMOUNT,
        model.SO_Detail.QTY_SUPPLY
    ).order_by(model.SO_Detail.SO_SYS_NO).all()

    if detail:
        encoded_details = []
        for item in detail:
            encoded_detail = {
                'ITEM_CODE': item.ITEM_CODE,
                'ITEM_NAME': item.ITEM_NAME,
                'QTY_DEMAND': item.QTY_DEMAND,
                'PRICE': item.PRICE,
                'DISC_PERCENT': item.DISC_PERCENT,
                'DISC_AMOUNT': item.DISC_AMOUNT,
                'LineTotal': item.LineTotal,
                'QTY_SUPPLY': item.QTY_SUPPLY
             }   
        
            encoded_details.append(encoded_detail)
         # detail_schemas = [schema.SO_Detail.from_orm(row) for row in details]
        return encoded_details
    else:
        return None
   




def get_header_sales_order_crud(db:Session,get_id:int):
    header = db.query(model.SO_Header.SO_SYS_NO,
                      model.SO_Header.SO_DOC_NO,
                      model.SO_Header.SO_DATE,
                      model.SO_Header.SO_STATUS,
                      model.SO_Header.CUST_CODE,
                      model.Customer.CUSTOMER_NAME,
                      label('CUSTOMER_ADDRESS', func.concat(model.SO_Header.DLVR_ADDR, ', ', model.SO_Header.DLVR_ADDR1, ', ', model.SO_Header.DLVR_ADDR2)),
                      model.Customer.CUST_MOBILE_PHONE,
                      model.SO_Header.TOP_CODE,
                      model.SO_Header.TOTAL,
                      model.SO_Header.SALES_EMP_NO,
                      model.Employee.EMPLOYEE_NAME
    ).join(model.Employee, model.SO_Header.SALES_EMP_NO==model.Employee.EMPLOYEE_NO, isouter=True
    ).join(model.Customer, model.SO_Header.CUST_CODE==model.Customer.CUSTOMER_CODE,isouter=True
    ).filter(model.SO_Header.SO_SYS_NO==get_id).order_by(model.SO_Header.SO_SYS_NO).first()

    if header is not None:
        encoded_header = {
            'SO_SYS_NO': header.SO_SYS_NO,
            'SO_DOC_NO': header.SO_DOC_NO,
            'SO_DATE': header.SO_DATE,
            'SO_STATUS': header.SO_STATUS,
            'CUST_CODE': header.CUST_CODE,
            'CUSTOMER_NAME': header.CUSTOMER_NAME,
            'CUSTOMER_ADDRESS': header.CUSTOMER_ADDRESS,
            'CUST_MOBILE_PHONE': header.CUST_MOBILE_PHONE,
            'TOP_CODE': header.TOP_CODE,
            'TOTAL': header.TOTAL,
            'SALES_EMP_NO': header.SALES_EMP_NO,
            'EMPLOYEE_NAME': header.EMPLOYEE_NAME
        }
        return encoded_header
    else:
        return None




def get_all_sales_order(db: Session, get_id: int):
    data_header = get_header_sales_order_crud(db, get_id)
    data_detail = get_detail_sales_order_crud(db, get_id)
    
    header_schema = schema.SO_Header.from_orm(data_header)
    detail_schema = [schema.SO_Detail.from_orm(row) for row in data_detail]
    

    # header = db.query(model.SO_Header).filter(model.SO_Header.SO_SYS_NO==get_id).order_by(model.SO_Header.SO_SYS_NO).first()
    # # detail = db.query(model.SO_Header).filter(model.SO_Detail.so_sys_no==get_id).order_by(model.SO_Header.so_sys_no).all()
    # details = db.query(model.SO_Detail).filter(model.SO_Detail.SO_SYS_NO == get_id).order_by(model.SO_Detail.SO_SYS_NO).all()

    # header_schema = SO_Header.from_orm(header)
    # detail_schema = SO_Detail.from_orm(detail)

    # header_schema.Item.append(detail_schema)
    # header_schema = schema.SO_Header.from_orm(header)
    # detail_schemas = [schema.SO_Detail.from_orm(row) for row in details]

   
    # for detail_schema in detail_schemas:
    #     header_schema.Item.append(detail_schema)
    # return header_schema

    return header_schema
    
