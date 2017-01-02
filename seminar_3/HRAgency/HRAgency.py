from Company import Company
from Person import Person

class HRAgency():

    np = 0
    nc = 0
    def __init__(self, Pers_arr, Com_arr):
        self.Pers_arr = Pers_arr
        self.Com_arr = Com_arr

    def start(self):
        for person in self.Pers_arr:
            for company in self.Com_arr:
                if person.abilityToWorkInCom(company):
                    person.sendSuplly()
                    self.np += 1

                    company.sendSuplly()
                    self.nc += 1

    # print result
    def result(self):
        return 'Number of people %s, Number of Companies %s' %(self.np, self.np)

if __name__ == '__main__':

    Ivan = Person('Ivan', 'job1', 100, 2, 2, 'Ivan@gmail.com')
    Sberbank = Company('Sberbank', ['job1', 'job2'], (100, 150), (1, 3), (1, 4), 'Sberbank@gmail.com')

    pr = []
    com = []

    pr.append(Ivan)
    com.append(Sberbank)

    hr = HRAgency(pr, com)

    hr.start()
    hr.result()
