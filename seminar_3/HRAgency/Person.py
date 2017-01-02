from Client import Client

class Person(Client):


    def __init__(self, name, job, pay, experience, education, email):
        super().__init__(name, email)
        self.job = job
        self.pay = pay
        self.experience = experience
        self.education = education

    def abilityToWorkInCom(self, company):
        if company.test(self.job, self.pay, self.experience, self.education):
            return True
        else:
            print(self.name + ' not suitable for '+ company.name)

    def __str__(self):
        return super().__str__() + ("Job %s" % (self.job))


if __name__ == '__main__':
    # start testing
    Ivan = Person('Ivan', 'unemployed', 0, 0, 'B', 'Ivan@gmail.com')
    print(Ivan)
    Ivan.sendSuplly()
