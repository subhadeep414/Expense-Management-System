import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger=setup_logger("db-helper")

@contextmanager
def connect_db(commit=False):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        database="expense_manager",
        password="root"
    )

    if connection.is_connected():
        print("Connected to Database")
    else:
        print("Some Error in Connecting to Database")

    cursor=connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()
    cursor.close()
    connection.close()

def fetch_expense_for_date(expense_date):
    logger.info(f"fetch_expense_for_date called for date {expense_date}")
    with connect_db(commit=False) as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (expense_date,))
        expenses=cursor.fetchall()
        return expenses

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called for date {expense_date}")
    with connect_db(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s",(expense_date,))

def insert_expenses(expense_date,amount,category,notes):
    logger.info(f"insert_expenses called for date {expense_date}")
    with connect_db(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",(expense_date,amount,category,notes,))

def fetch_expense_summary(start_date,end_date):
    logger.info(f"fetch_expense_summary called for start date {start_date} and end date {end_date}")
    with connect_db(commit=False) as cursor:
        cursor.execute(
            '''
                    SELECT category,SUM(amount) as total
                    FROM expenses
                    WHERE expense_date
                    BETWEEN %s AND %s
                    GROUP BY category
            ''',(start_date,end_date,)
            )
        datas=cursor.fetchall()
        return datas

def fetch_expenses_summary_by_month():
    logger.info("fetch_expense_summary_by_month called for getting analytics by month")
    with connect_db(commit=False) as cursor:
        cursor.execute(
            '''
                SELECT DATE_FORMAT(expense_date, '%M') AS month_name, 
                    MONTH(expense_date) AS month_number, 
                    SUM(amount) AS total_spending
                FROM expenses
                GROUP BY month_name, month_number
                ORDER BY month_number;
            '''
        )
        datas=cursor.fetchall()
        return datas

if __name__=="__main__":
    # print(fetch_expense_for_date("2025-02-15"))
    # insert_expenses("2025-02-15",200,"Food","Eat yummy biriyani")
    # delete_expenses_for_date("2025-02-15")
    # data=fetch_expense_summary("2024-08-01","2024-08-05")
    # for result in data:
    #     print(result)
    print(fetch_expenses_summary_by_month())