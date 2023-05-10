from fastapi import FastAPI, Depends
from database import engine
from sqlalchemy import text
import json
from decimal import Decimal
from datetime import datetime
from model import SO_Header, SO_Detail

test = FastAPI()
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# SP :
# 	HEADER
# 	exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362

# 	DETAIL
# 	exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=3635362     

# def for_sales_order_select(db = Depends(get_db)): 
#     conn = db.connect()
#     header = conn.execute("exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362").fetchall()
#     detail = conn.execute("exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=3635362").fetchall()
#     conn.close()
#     return header, detail

# def get_sales_order(so_sys_no: int) -> dict:
#         with engine as conn:
#             header = conn.execute("exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=:so_sys_no"), {"so_sys_no": so_sys_no}.fetchall()
#             detail = conn.execute("exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=:so_sys_no"), {"so_sys_no": so_sys_no}.fetchall()
#         return {'header': header, 'detail': detail}

@test.get('/AFS/SalesOrderSelect')
async def for_sales_order_print():
    with engine.connect() as con:
        header = con.execute(text("exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362"))
        headerfetch = header.fetchone()        
        # headerkeys = header.keys()
        
        # headerresult = [dict(zip(headerkeys, row))for row in headerfetch]
        # headerresult = dict(zip(headerkeys, headerfetch))
       
        main_table = SO_Header(
                SOSysNo=headerfetch[0],
                SODocNo=headerfetch[1],
                SODate=headerfetch[3],
                SOStatus=headerfetch[4],
                CustomerCode=headerfetch[5],
                CustomerName=headerfetch[6],
                CustomerAddress=headerfetch[7],
                CustomerMobilePhoneNo=headerfetch[8],
                TOP=headerfetch[9],
                TotalAmount=headerfetch[10],
                SalesEmployeeNo=headerfetch[11], 
                SalesemployeeName=headerfetch[12],
                Items=[],     
        )

        detail = con.execute(text("exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=3635362"))
        detailfetch = detail.fetchall()   
        # detailkeys = detail.keys()

      

        for row in detailfetch:
            itemdetail = SO_Detail(
                ItemCode=row[0],
                ItemName=row[1],
                QtyDemand=row[2],
                ItemPrice=row[3],
                DiscPercent=row[4],
                DiscAmount=row[5],
                LineTotal=row[6],
                QtySupplied=row[7],
            )
            main_table.Items.append(itemdetail)


        return main_table


        
      
        
        # detailresult = [dict(zip(detailkeys, row))for row in detailfetch]     
       
        # detailresult = []
        # headerresult['Items'] = detailresult

       
        # response_json = json.dumps(headerresult, default = str)



    
             
# from fastapi import FastAPI
# from database import engine
# from sqlalchemy import text
# import json
# from decimal import Decimal
# from datetime import datetime

# test = FastAPI()


# class DecimalEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Decimal):
#             return float(obj)
#         return super(DecimalEncoder, self).default(obj)

# class CustomJSONEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.isoformat()
#         return super().default(obj)


# @test.get("/AFS/SalesOrderSelect")
# async def get_sales_order():

#     with engine.connect() as conn:
#         header_query = text("exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362")
#         header_result = conn.execute(header_query).fetchone()
#         detail_query = text("exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=3635362")
#         detail_result = conn.execute(detail_query).fetchall()
    

#     header_keys = ['SOSysNo', 'SODocNo', 'SODate', 'SOStatus', 'CustomerCode', 'CustomerName', 'CustomerAddress', 'CustomerMobilePhoneNo', 'TOP', 'TotalAmount', 'SalesEmployeeNo', 'SalesemployeeName']
#     header_dict = dict(zip(header_keys, header_result))
#     detail_keys = ['ItemCode', 'ItemName', 'QtyDemand', 'ItemPrice', 'DiscPercent', 'DiscAmount', 'LineTotal', 'QtySupplied']
#     detail_list = [dict(zip(detail_keys, row)) for row in detail_result]


#     header_dict['Items'] = detail_list


#     response_json = json.dumps(header_dict, cls=DecimalEncoder, default=str)
#     return response_json


