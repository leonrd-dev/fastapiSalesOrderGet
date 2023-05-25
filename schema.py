from typing import List, Optional
from pydantic import BaseModel
from decimal import Decimal
import datetime

class SO_Detail(BaseModel):
    ItemCode : str
    ItemCode: str
    ItemName: str
    QtyDemand: Decimal
    ItemPrice: Decimal
    DiscPercent: Decimal
    DiscAmount: Decimal
    LineTotal: Decimal
    QtySupplied: Decimal

class SO_Header(BaseModel):
    SOSysNo: int
    SODocNo: str
    SODate: datetime.date
    SOStatus: str
    CustomerCode: str
    CustomerName: str
    CustomerAddress: str
    CustomerMobilePhoneNo: str
    TOP: str
    TotalAmount: Decimal
    SalesEmployeeNo: Optional[str] = None
    SalesemployeeName: str
    Items:List[SO_Detail]

