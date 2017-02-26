class boy:
    #initializes a boy with given attributes
    def __init__ (self,name,attr,budgt,intel,min_attr,boy_type):
        self.name = name
        self.attr = attr
        self.budgt = budgt
        self.intel = intel
        self.min_attr = min_attr
        self.status = "single"
        self.girlfrnd = ''
        self.boy_type = boy_type 

    #checks eligibity a given girl for a particular boy
    def check_eligible(self,girl):

        if(self.budgt < girl.budgt) :
            return False
        if(self.min_attr > girl.attr):
            return False
        if(self.status == "commited" or girl.status == "commited"):
            return False
        else: 
	    return True


    def self_status (self):
    #returns status of a boy
        return self.status
    
