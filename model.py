from typing import List, Optional
from pydantic import BaseModel
from decimal import Decimal
import datetime

class SO_Detail(BaseModel):
    ITEM_CODE: str
    QTY_DEMAND: Decimal
    DISC_PERCENT: Decimal
    DISC_AMOUNT: Decimal
    QTY_SUPPLY: Decimal
    SO_SYS_NO: int

    class Config :
        orm_mode = True

class SO_Header(BaseModel):
    SO_SYS_NO: int
    SO_DOC_NO: str
    SO_DATE: datetime.date
    SO_STATUS: str
    CUST_CODE: str
    TOP_CODE: str
    TOTAL: Decimal
    SALES_EMP_NO: Optional[str] = None
    # Item:Optional[List[SO_Detail]] = []
    Item: List[SO_Detail] = []

    class Config :
        orm_mode = True

