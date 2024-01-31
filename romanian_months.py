from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime("%d/%m/%Y")
current_year = current_date.strftime("%Y")
current_month = current_date.strftime("%m")

def get_month_name(month):
    month_names = {
        "01": "Ianuarie",
        "02": "Februarie",
        "03": "Martie",
        "04": "Aprilie",
        "05": "Mai",
        "06": "Iunie",
        "07": "Iulie",
        "08": "August",
        "09": "Septembrie",
        "10": "Octombrie",
        "11": "Noiembrie",
        "12": "Decembrie"
    }

    return month_names.get(month, "Invalid Month")


current_month_ro = get_month_name(current_month)