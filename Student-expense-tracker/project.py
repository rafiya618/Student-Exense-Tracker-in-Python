import datetime
from datetime import datetime
my_income=200000
my_password="python123"
my_username="user1"

def Authentication(p,u)-> bool:
    if p==my_password and u==my_username:
        return True
def calculate_total(user)->float:
        user.total_expense=(
        float(user.hostel_due)
        +float(user.transportation)
        +float(user.food)
        +float(user.university_due)
        +float(user.entertainment)
        +float(user.medical)
        +float(user.personal_stuff)
        )
        return user.total_expense
def calculate_saving(user)->float:
        user.money_saved=my_income-user.total_expense
        return user.money_saved

class Expenses:
    hostel_due=None
    transportation=None
    food=None
    university_due=None
    entertainment=None
    medical=None
    personal_stuff=None
    total_expense=0.0
    money_saved=0.0

    def __init__(self) -> None:
         pass
    
    def add_monthly_expense(self):
        u=input("USERNAME: ")
        p=input("PASSWORD: ")
        if Authentication(p,u):
            self.hostel_due=float(input("Hostel Due: "))
            self.transportation=float(input("Transportantation: "))
            self.food=float(input("Food: "))
            self.university_due=float(input("University Due: "))
            self.entertainment=float(input("Entertainment: "))
            self.medical=float(input("Medical: "))
            self.personal_stuff=float(input("Personal Stuff: "))
            self.total_expense=calculate_total(self)
            self.money_saved=calculate_saving(self)
            month = datetime.now().month
            year = datetime.now().year
            entery=str(month)+"/"+str(year)
            with open('Expenses.txt','a') as file:
                file.write(
            str(entery) + " " +
            str(self.hostel_due) + " " +
            str(self.transportation) + " " +
            str(self.food) + " " +
            str(self.university_due) + " " +
            str(self.entertainment) + " " +
            str(self.medical) + " " +
            str(self.personal_stuff) + " " +
            str(self.total_expense) + " " +
            str(self.money_saved) + "\n"
            )
    
    def view_monthly_expenses(self):
        u=input("USERNAME: ")
        p=input("PASSWORD: ")
        if Authentication(p,u):    
            list=[]
            with open('Expenses.txt','r') as file:
                for line in file:     
                    for word in line.split():      
                            list.append(word)
                
            for index in range(0,len(list),10):
                print(f"""
                        📅 MONTH-YEAR: {list[index]} 
                    ___________________________
                        🏨 Hostel Due: Rs.{list[index+1]}
                        🚖 Transport: Rs.{list[index+2]}
                        🍔 Food: Rs.{list[index+3]}
                        📚 University Due: Rs.{list[index+4]}
                        🎯 Entertainment: Rs.{list[index+5]}
                        🩺 Medical: Rs{list[index+6]}
                        👕 Personal Stuff: Rs.{list[index+7]}
                    ___________________________
                        💰 TOTAL EXPENSE: Rs.{list[index+8]}
                        💵 MONEY SAVED: Rs.{list[index+9]}
                    **************************

                    """)
def main():
    user1=Expenses()
    while(True):
        try:
            choice=int(input(f""">>>>WELCOME TO YOUR MONTHLY EXPENSES TRACKER<<<<
                        -> Press 1 to ADD 
                        -> Press 2 to VIEW
                    """))
            if choice==1:
                user1.add_monthly_expense()
            elif choice==2:
                user1.view_monthly_expenses()
            else:
                break
        except ValueError:
             print("Invalid input:(")
if __name__ == '__main__':
    main()