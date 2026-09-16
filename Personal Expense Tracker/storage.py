import json
import os #برای سیستم عامل هست که رابط یرنامه ما و سیستم عامله
from expences import Expence

DATA_FILE= os.path.join("data","expences.json")

def save_expences(expence_list): #ذخیره کردن شی در قالب دیکشنری
    data = [expences.to_dict() for expences in expence_list]
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_expences():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return [Expence.from_dict(item)for item in data]
