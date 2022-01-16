class Account:

    def __init__(self, balance): # 생성자 함수
            self.balance = balance
    def deposit(self, money):
            self.balance += money
    def inquire(self):
        print("잔액은 %d원 입니다."%self.balance)

shinhan = Account(8000) # Account의 인스턴스 생성
shinhan.deposit(1000)
shinhan.inquire()

nonghyup = Account(120000)
nonghyup.inquire()