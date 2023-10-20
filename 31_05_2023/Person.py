class Person:
    
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

if __name__ == '__main__':            # when run for testing only
    # self-test code
    P1 = Person("Surya Charan")
    P2 = Person("Hare Krishna", job="Universe", pay=100000000000000000000)
    print(P1.name, P1.pay)
    print(P2.name, P2.pay)
