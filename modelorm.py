from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship





Base = declarative_base()

class SO_Detail(Base):
    __tablename__ = 'atSalesOrder1'

    so_sys_no = Column(Integer, primary_key=True)
    item_code = Column(String)
    item_name = Column(String)
    qty_demand = Column(Numeric)
    item_price = Column(Numeric)
    disc_percent = Column(Numeric)
    disc_amount = Column(Numeric)
    line_total = Column(Numeric)
    qty_supplied = Column(Numeric)
    so_sys_no = Column(Integer, ForeignKey('atSalesOrder0.id'))
    header = relationship("SO_Header", back_populates="items")


class SO_Header(Base):
    __tablename__ = 'atSalesOrder0'
    so_sys_no = Column(Integer, primary_key=True)
    so_doc_no = Column(String)
    so_date = Column(Date)
    so_status = Column(String)
    customer_code = Column(String)
    customer_name = Column(String)
    customer_address = Column(String)
    customer_mobile_phone_no = Column(String)
    top = Column(String)
    total_amount = Column(Numeric)
    sales_employee_no = Column(String, nullable=True)
    sales_employee_name = Column(String)
    items = relationship("SO_Detail", back_populates="header")