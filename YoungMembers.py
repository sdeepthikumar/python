from CareAllSystem import CareAllSystem
import ElderMembers

class YoungMembers(CareAllSystem):
    care_takers = [] 
      
    @classmethod
    def add_care_takers(cls,obj_self):
        cls.care_takers.append(obj_self)
   
    def add_to_careseeker_list(self,obj):
        self.careseeker_list.append(obj)
        
    def __init__(self,userid,category,name,age,gender,phone,city,status):
        super().register(userid,category,name,age,gender,phone,city,status)
        self.careseeker_list = []
        YoungMembers.add_care_takers(self)
    
    def find_care_seekers(self):
        available_careseekers = [cs for cs in ElderMembers.ElderMembers.care_seekers if cs.status == True]
        return(available_careseekers)
    
    def seek_approval(self,obj_cs):
        message = ''
        if obj_cs.status == False:
            message = "Sorry! Elder member is not available. "
        if self.status == False:
            message = message + "Sorry! Caretaker is not available. "
        if obj_cs.status == True and self.status == True:
            request_status = ElderMembers.ElderMembers.request_approval(self,obj_cs)
            return request_status
        else:
            return message
    
    def assign_careseeker(self,obj_cs,approval = None):
        if approval:
            message = ''
            if self.status == False:
                message = "Sorry!{} has already been assigned 4 members.Please choose another.".format(self.name)
            elif self.status == True:
                self.add_to_careseeker_list(obj_cs)
                message = "Elder member assigned successfully!"
            if self.status == True and len(self.careseeker_list) == 4:
                self.set_status(False)
            return message
        else:
                return "Please request elder for approval"