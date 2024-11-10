class StoredNumber:
    def __init__(self, num):
        self.num = num
    
    def __str__(self):
        return f'The number: {self.num}'
    
    def set_number(self, num):
        self.num = num
    
    

instance_1 = StoredNumber(1)
instance_2 = StoredNumber(2)

print(instance_1, instance_2)

instance_1.set_number(5)
print(instance_1, instance_2)

the_list = [instance_1, instance_2]
print(the_list)
for instance in the_list:
    print(instance)
