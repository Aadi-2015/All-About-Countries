# C;ass1
class India:
    def capital(self):
        print('Capital -- New Delhi')
    def lan(self):
        print('Language -- Hindi')
    def type(self):
        print('Type -- Developing') 
class Usa:        
    def capital(self):
        print('Capital -- Washington DC')
    def lan(self):
        print('Language -- English')
    def type(self):
        print('Type -- Developed') 
obj_ind = India()
obj_usa = Usa()
for country in (obj_ind,obj_usa):
    country.capital()
    country.lan()
    country.type()         