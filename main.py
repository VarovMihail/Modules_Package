from datetime import datetime
from Application.salary import calculate_salary
from db.people import get_employees


if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employees()


