class Model():
    def __init__(self):
        self.dic = {}
        
    def __getattr__(self,key):
        return self.dic[key]

    def __setattr__(self, key, value):
        self.dic[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    

user = Model()
user.__setattr__('id',123)
print(user.getValue('id'))
