class User:
    def init(self,first_name,last_name,cf,birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.cf = cf
        self.birth_date = birth_date

    def describe_user(self):
        information = {}
        information["first_name"] = self.first_name
        information["last_name"] = self.last_name
        information["fiscal_code"] = self.cf
        information["birth_date"] = self.birth_date
        return print((k,v) for k,v in information.items())



info = User("Mattia","NNN","1010329383838","04/05/1999")
print(info)