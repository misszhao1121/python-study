class Dog:
    def set_age(self,age):
        if age >0 and age <=100:
            self.age = age
        else:
            self.age = 0
    def get_age(self):
        return self.age
dog = Dog()
#dog.age = 10
#dog.name="小白"


dog.set_age(10)
age = dog.get_age()
#dog.get_name("丁丁")
print(age)
