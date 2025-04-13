from backend import db_helper

def test_fetch_expense_for_date_sep_1():
    expenses=db_helper.fetch_expense_for_date("2024-09-01")
    assert len(expenses)==5

    assert expenses[0]['amount']==1200
    assert expenses[0]['category']=='Rent'

def test_fetch_expense_for_date_invalid():
    expenses = db_helper.fetch_expense_for_date("2024-09-10")
    assert len(expenses)==0

def test_fetch_expense_summary():
    expenses=db_helper.fetch_expense_summary("2099-10-05","2099-1-13")
    assert len(expenses)==0