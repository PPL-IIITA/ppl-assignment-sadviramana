from math import log,exp
class girl:
    #initializes a girl with given attributes
    def __init__ (self,name,attr,budgt,intel,girl_type):
        self.name = name
        self.attr = attr
        self.budgt = budgt
        self.intel = intel
        self.status = "single"
        self.boyfrnd = ''
        self.girl_type = girl_type 

    #checks eligibity a boy for a particular girl
    def check_eligible(self,boy):
        if(self.budgt > boy.budgt) :
            return False
        if(self.status == "commited" or boy.status == "commited"):
            return  False
	else:
	    return True
    #gives happiness for a choosy girl
    def happ_chsy(self,gifts):
	sum = 0
	for i in gifts:
		if(i.gif_type=='Luxury'):
			sum+=(2*i.value+i.price)
		else :
			sum+=i.price
	sum = int(log(sum))
	return sum
    #gives happiness for a normal girl
    def happ_nr(self,gifts):
	sum = 0
	for i in gifts:
		sum += i.price + i.value
	return sum
    #gives happiness for a desperate girl 
    def happ_des(self,gifts):
	sum=0
	for i in gifts:
		sum+=i.price
	sum = min(int(exp(sum)),1000)
	return sum
