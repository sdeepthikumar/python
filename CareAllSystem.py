class CareAllSystem:
    
    def register(self,userid,category,name,age,gender,phone,city,status = None):
        self.userid = userid
        self.category = category
        self.name = name
        self.age = age
        self.phone = phone
        self.city = city
        self.status = status
        self.account_balance = 0
        self.rating = 0
        self.rating_count = 0
        self.average_rating = 0
        self.reviews =[]
        
    def get_status(self):
        return self.status
    
    def set_status(self,new_status):
        self.status = new_status
        
    def allocate_funds(self,amount):
        self.account_balance = self.account_balance + amount
        
    def transfer_funds(self,obj,amount):
        self.account_balance = self.account_balance - amount
        obj.account_balance = obj.account_balance + amount
        
    def get_account_balance(self):
        return self.account_balance
        
    def rate_users(self,new_rating):
        self.rating_count += 1
        self.rating = self.rating + new_rating
        self.average_rating = round((self.rating/self.rating_count),1)
    
    def get_rating(self):
        return self.average_rating
    
    def add_review(self,review):
        self.reviews.append(review)
    
    def get_review(self):
        return self.reviews
 
        
    