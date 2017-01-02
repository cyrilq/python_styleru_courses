from Client import Client

class Company(Client):

    def __init__(self, name, job, pay, experience, education, email):
        super().__init__(name, email)
        self.job = job
        self.pay = pay
        self.experience = experience
        self.education = education

    def test(self, job, pay, experience, education):
        j, py, ex, ed = False, False, False, False
        if job in self.job:
            j = True
        if self.pay[0] < pay < self.pay[1]:
            py = True
        if self.experience[0] < experience < self.experience[1]:
            ex = True
        if self.education[0] < education < self.education[1]:
            ed = True

        return j and py and ex and ed

    def __str__(self):
        return super().__str__()

if __name__ == '__main__':
    Sberbank = Company('Sberbank', ['job1', 'job2'], (100, 150), (1, 3), (1, 4), 'Sberbank@gmail.com')
    print(Sberbank.test('job1', 120, 2, 2))
    print(Sberbank)

