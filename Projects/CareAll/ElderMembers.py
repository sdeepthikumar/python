from CareAllSystem import CareAllSystem
import YoungMembers

class ElderMembers(CareAllSystem):
    care_seekers = [] 
   
    @classmethod
    def add_care_seekers(cls,obj_self):
        cls.care_seekers.append(obj_self)
        
    def __init__(self,userid,category,name,age,gender,phone,city,status):
        super().register(userid,category,name,age,gender,phone,city,status)
        ElderMembers.add_care_seekers(self)
    
    def assign_caretaker(self,ct,approval = None):
        self.caretaker_id = ct.userid
        self.caretaker_name = ct.name
        self.set_status(False)
        
    def find_caretakers(self):
        available_caretakers = [ct for ct in YoungMembers.YoungMembers.care_takers if ct.status == True]
        return(available_caretakers)
        
    
    def request_approval(obj_ct,obj_cs):
        approve = input("Hi {}. Greetings! {} has requested for approval as your caretaker.Please enter Y to approve or N to reject : ".format(obj_cs.name,obj_ct.name))
        if approve == 'Y':
            approval = 1
            obj_cs.assign_caretaker(obj_ct,approval)
            obj_ct.assign_careseeker(obj_cs,approval)
            return "Request Approved.\n{} has been assigned as caretaker of {}\n".format(obj_ct.name,obj_cs.name)
        else:
            return "Request Rejected"
