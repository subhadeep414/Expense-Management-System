from typing import List
from fastapi import FastAPI,HTTPException
from datetime import date

from fastapi.openapi.utils import status_code_ranges

import db_helper
from pydantic import BaseModel

app=FastAPI()

class Expense(BaseModel):
    amount:float
    category:str
    notes:str

class DateRange(BaseModel):
    start_date:date
    end_date:date

@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses(expense_date:date):
    expenses=db_helper.fetch_expense_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date:date,expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expenses(expense_date,expense.amount,expense.category,expense.notes)
    return {"message":"Expense updated successfully"}

@app.post("/analytics")
def get_analytics(date_range:DateRange):
    data=db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if not data:
        HTTPException(status_code=500,detail="Failed to retrieve the data from database")
    total=sum([row['total'] for row in data])


    breakdown={}

    for row in data:
        percentage=(row['total']/total)*100 if total!=0 else 0
        breakdown[row['category']]={'total':row['total'],'percentage':percentage}
    return breakdown

@app.get("/analytics/months")
def get_analytics_by_month():
    monthly_expenses=db_helper.fetch_expenses_summary_by_month()
    if not monthly_expenses:
        HTTPException(status_code=500, detail="Failed to retrieve the data from database")
    else:
        return monthly_expenses