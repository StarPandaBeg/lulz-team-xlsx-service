
from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from config import *


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def totext(te):
    return text(te)


class TransactionsWithReceipts(Base):
    __tablename__ = 'transactions_with_receipts'
    id = Column(Integer, primary_key=True)
    account_number = Column(String)
    transaction_id = Column(String)
    operation_type = Column(String)
    operation_category = Column(String)
    status = Column(String)
    creation_date = Column(Date)
    authorization_date = Column(Date)
    transaction_date = Column(Date)
    original_operation_id = Column(String)
    operation_amount_in_currency = Column(String)
    operation_currency = Column(String)
    amount_in_account_currency = Column(String)
    counterparty = Column(String)
    counterparty_inn = Column(String)
    counterparty_kpp = Column(String)
    counterparty_account = Column(String)
    counterparty_bank_bik = Column(String)
    counterparty_bank_corr_account = Column(String)
    counterparty_bank_name = Column(String)
    payment_purpose = Column(String)
    payment_number = Column(String)
    sequence = Column(String)
    code = Column(String)
    card_number = Column(String)
    mcc = Column(String)
    place_of_transaction_city = Column(String)
    place_of_transaction_country = Column(String)
    organization_address = Column(String)
    bank = Column(String)
    document_creator_status = Column(String)
    budget_classification_code = Column(String)
    oktmo_code = Column(String)
    tax_payment_basis = Column(String)
    tax_period_customs_code = Column(String)
    tax_document_number = Column(String)
    tax_document_date = Column(String)
    tax_payment_type = Column(String)
    komandirovka_id = Column(Integer)
    receipt_fd = Column(String)
    receipt_fp = Column(String)
    receipt_fn = Column(String)


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_number = Column(String)
    transaction_id = Column(String)
    operation_type = Column(String)
    operation_category = Column(String)
    status = Column(String)
    creation_date = Column(Date)
    authorization_date = Column(Date)
    transaction_date = Column(Date)
    original_operation_id = Column(String)
    operation_amount_in_currency = Column(String)
    operation_currency = Column(String)
    amount_in_account_currency = Column(String)
    counterparty = Column(String)
    counterparty_inn = Column(String)
    counterparty_kpp = Column(String)
    counterparty_account = Column(String)
    counterparty_bank_bik = Column(String)
    counterparty_bank_corr_account = Column(String)
    counterparty_bank_name = Column(String)
    payment_purpose = Column(String)
    payment_number = Column(String)
    sequence = Column(String)
    code = Column(String)
    card_number = Column(String)
    mcc = Column(String)
    place_of_transaction_city = Column(String)
    place_of_transaction_country = Column(String)
    organization_address = Column(String)
    bank = Column(String)
    document_creator_status = Column(String)
    budget_classification_code = Column(String)
    oktmo_code = Column(String)
    tax_payment_basis = Column(String)
    tax_period_customs_code = Column(String)
    tax_document_number = Column(String)
    tax_document_date = Column(String)
    tax_payment_type = Column(String)
    komandirovka_id = Column(Integer)
