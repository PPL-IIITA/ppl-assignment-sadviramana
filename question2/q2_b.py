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
    #gives gift list for a Miser guy
    def allocMiser(self,girl,gift) :
	total = 0
	g = []
	for i in gift:
		if(i.if_alloc == False) :		
			if(total<girl.budgt):
				total += i.price
				g+=[i]
			else :
				break
	if(total > self.budgt):
			self.budgt = total;
	return g
    #gives gift list for a Generous guy
    def allocGen(self,gift):
	total = 0
	g=[]
	for i in gift:
		if(i.if_alloc == False):
			if(total < self.budgt):
				total+=i.price
				g+=[i]
			else :
				break
	if(total > self.budgt):
			self.budgt = total;
	return g
    #gives gift list for a  Geeks
    def allocGk(self,girl,gift):
	total = 0
	g=[]
	for i in gift:
		if(i.if_alloc == False):
			if(total<girl.budgt):
				total += i.price
				g+=[i]
			else :
				break
	if(total > self.budgt):
			self.budgt = total;
	if( total < self.budgt):
			for i in gift:
				if(i not in g):
					if (i.gif_type == 'Luxury') and ((self.budgt - total) >= i.price):
						total += i.price
						g += [i]
						break

	return g		
	
