import datetime
class Expence:
    def __init__(self, title, amount, category, date=None):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.datetime.now().isoformat()
    def to_dict(self):
        return {
            'title': self.title,
            'amount': self.amount,
            'category': self.category,
            'date': self.date
        }
    @staticmethod
    def from_dict(data): #یه شی جدید از کلاس اضافه کن و نشون بده
        return Expence( #دیتا همونیه که کاربر وارد میکنه
            title=data["title"],
            amount= data ["amount"],
            category= data ["category"],
            date= data ["date"]
        )