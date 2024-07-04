from datetime import datetime
from application.salary import calculate_salary
import application.application.db.people



if __name__ == '__main__':
    print(datetime.now())
    application.application.db.people.get_employees()
    calculate_salary()

