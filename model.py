from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from typing import List





Base = declarative_base()

class SO_Detail(Base):
    __tablename__ = 'atSalesOrder1'
    SO_LINE_NO = Column(Integer, primary_key=True)
    ITEM_CODE = Column(String)
    QTY_DEMAND  = Column(Numeric)
    DISC_PERCENT = Column(Numeric)
    DISC_AMOUNT = Column(Numeric)
    QTY_SUPPLY = Column(Numeric)
    SO_SYS_NO = Column(Integer, ForeignKey('atSalesOrder0.SO_SYS_NO'))
    header = relationship("SO_Header", back_populates="items")


class SO_Header(Base):
    __tablename__ = 'atSalesOrder0'
    SO_SYS_NO = Column(Integer, primary_key=True)
    SO_DOC_NO = Column(String)
    SO_DATE = Column(Date)
    SO_STATUS = Column(String)
    CUST_CODE = Column(String)
    TOP_CODE = Column(String)
    TOTAL = Column(Numeric)
    SALES_EMP_NO = Column(String, nullable=True)
    items = relationship("SO_Detail", back_populates="header")


