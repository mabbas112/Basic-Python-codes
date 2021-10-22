class Restaurant():
    def __init__(self, restaurant_name, restaurant_cuisine):
        self.restaurant_name= restaurant_name
        self.restaurant_cuisine=restaurant_cuisine
        self.number_served=0
    def describe_restaurant(self):
        print('Restaurant name is {} and Restaurant cuisine is {}.'.format(self.restaurant_name,
                                                                          self.restaurant_cuisine))
    def open_restaurant(self):
        print('Restaurant is open now!')
        
    def set_number_served(self , number_served):
        self.number_served = number_served
    def increment_number_served(self, number_served):
        self.number_served+=number_served
        