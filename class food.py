class food():
    def __init__(self):
        print('WEL-COME TO THE FOOD SHOP')
        lst = ['rice-plate']
        lst1=['60']
        self.lst=lst
        self.lst1=lst1
    def add_food(self):
        a=int(input('enter the number how many food you want to add:'))
        for i in range(a):
            b=input(f'add foods here,{i+1}:')
            self.lst.append(b)
        print(self.lst)
        for j in range(a):
            e=input('add prize here:')
            self.lst1.append(e)
        print(self.lst1)
    def delete_food(self):
        c=int(input("how many food do you want to delete:"))
        for i in range(c):
            d=int(input("enter index which food you want to delete:"))
            del(self.lst[d])
        print(self.lst)
        for j in range(c):
            del(self.lst1[d])
        print(self.lst1)
    def show_food_lst(self):
        print("This is food list:",self.lst)
    def show_food_by_name(self):
        dict = {}
        x = 0
        for k in self.lst:
            dict[k] = self.lst1[x]
            x = x + 1
        print(dict)
        d=input("search for the food:")
        if d in self.lst or self.lst1 or dic:
            print(f"{d} is available here")
        else:
            print("Oops?.this food is not available")
    def show_food_by_type(self):
        e=input("which types of the food do you want to search veg/non-veg:")
        if e=='veg' or 'vegeterian' or 'vegetable':
            print('available food as below\n',self.lst)
        else:
            print('this types of food not available here')
    def sort_food_list(self):
        (self.lst).sort()
        print("food list sorted by name\n",self.lst)
obj=food()
obj.add_food()
obj.delete_food()
obj.show_food_lst()
obj.show_food_by_type()
obj.show_food_by_name()
obj.sort_food_list()




