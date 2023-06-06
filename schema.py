from typing import List, Optional
from pydantic import BaseModel
from decimal import Decimal
import datetime

class SO_Detail(BaseModel):
    ItemName: str
    ItemName: str
    QtyDemand: Decimal
    ItemPrice : Decimal
    DiscPercent: Decimal
    DiscAmount: Decimal
    LineTotal: Decimal
    QtySupplied: Decimal

    
    class Config :
        orm_mode = True

class SO_Header(BaseModel):
    SOSysNo: int
    SODocNo: str
    SODate: datetime.date
    SOStatus: str
    CustomerCode: str
    CustomerName : str
    CustomerAddress : str
    CustomerMobilePhoneNo : str
    TOP: str
    TotalAmount: Decimal
    SalesEmployeeNo: Optional[str] = None
    SalesEmployeeName: str
    Items: Optional [List[SO_Detail]] = []

    class Config :
        orm_mode = True

