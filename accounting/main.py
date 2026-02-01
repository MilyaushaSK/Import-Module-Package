import application.salary
from application.db.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    get_employees()
    application.salary.calculate_salary()
    print(datetime.today().date())