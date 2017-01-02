import Email


class Client:

    # initialization of the class
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.Email = Email.Email(email)

    # send email
    def sendSuplly(self):
        self.Email.sendMessage()

    def __str__(self):
        return "Name %s, Email %s" % (self.name, self.email)


if __name__ == '__main__':

    # start testing
    cl1 = Client('Vitya', 'vitya@gmail.com')
    cl1.sendSuplly()
    print(cl1)