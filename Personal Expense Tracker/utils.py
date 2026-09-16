import datetime

def get_today_date():
    return datetime.date.today().isoformat()

def format_currency(amount): #adad karbar
    return f"{amount:,.0f} Dollar"

def filter_by_date(expences, start_date, end_date):
    return [expence for expence in expences if start_date <= expence.date <= end_date]