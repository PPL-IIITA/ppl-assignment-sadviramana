class girl:
    def __init__ (self,name,attr,budgt,intel,girl_type):
        self.name = name
        self.attr = attr
        self.budgt = budgt
        self.intel = intel
        self.status = "single"
        self.boyfrnd = ''
        self.girl_type = girl_type 


    def check_eligible(self,boy):
        if(self.budgt > boy.budgt) :
            return False
        if(self.status == "commited" or boy.status == "commited"):
            return  False
	else:
	    return True


    def self_status (self):
        return self.status
