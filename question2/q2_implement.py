import csv
from random import randint
from q2_b  import boy
from q2_g  import girl
from q2_gift import gift
from q2_utility import utility
from q2_couple import commited_pair
import logging


utility()

logging.basicConfig(filename='q2_log.txt',
			format='%(asctime)s %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
					level=logging.DEBUG,
						filemode='w')
	
#allocates boys with girls
def allocation():
	

	with open('boys.csv','r') as csvbfile:
		b_read = csv.reader(csvbfile , delimiter = ',')
		B = [boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),(row[5])) for row in b_read]
		csvbfile.close()
	with open('girls.csv','r') as csvgfile:
		g_read = csv.reader(csvgfile , delimiter = ',')
		G = [girl(row[0],int(row[1]),int(row[2]),int(row[3]),(row[4])) for row in g_read]
		csvgfile.close()
	with open('gifts.csv','r') as csvgiffile:
		gif_read = csv.reader(csvgiffile , delimiter = ',')
		GIF = [gift(row[0],int(row[1]),int(row[2]),row[3]) for row in gif_read]
		csvgiffile.close()
	
	Couple = []
	GIF = sorted(GIF, key = lambda i: i.price)
	logging.info("matching is taking place:\n")
	count=0
	for g in  G:
		for b in  B:
			logging.info("checking if girl:"+g.name+"matches with boy:"+b.name);
			#checking required conditions to match girls with boys
			if(g.check_eligible(b) and b.check_eligible(g)and g.status == 'single' and b.status == 'single'):
				count+=1

				b.status = 'commited'
				g.status = 'commited' 
				logging.info("girl:-" + g.name + " got commited with boy:-" + b.name)
				b.girlfrnd = g.name
				g.boyfrnd = b.name
				Couple = Couple+[(b,g)]
				break
			elif(g.status=="commited"):
				logging.info("girl:-"+g.name+"is already commited")
				break
			elif(b.status=="commited"):
				logging.info("boy:-"+b.name+"is already commited")
			elif (g.budgt > b.budgt):
				logging.info("girl:-" + g.name + " is too costly to handle for boy:-" + b.name)
			elif(b.min_attr > g.attr):
				logging.info("boy:-" +b.name+" does not find girl:-" +g.name+"attractive")
	#logging.info("\n")
	C = [commited_pair(x[0],x[1]) for x in Couple]
	for c in C :
		c.set_compat()
	allocate_gifts(C,GIF)
	girl_happ(C)
	couple_happ(C)
	k = randint(1,count)
	print "for k value = " + str(k) 
	print_k(C,k)
#allocating gifts
def allocate_gifts(C,GIF):
	logging.info("\nboyfriend gifts his girl :\n")
	for c in C :
		#print "hello"
		g=[]
		if(c.boy.boy_type == 'Miser'):
			g = c.boy.allocMiser(c.girl,GIF)
		if(c.boy.boy_type == 'Generous'):
			g = c.boy.allocGen(GIF)
		if(c.boy.boy_type == 'Geek'):
			g = c.boy.allocGk(c.girl,GIF)
		c.GIFT = g
		c.set_compat()
#compute girl happiness
def girl_happ(C):
	gifts=[]
	for c in C:
		#print "hello"
		
		gifts = c.GIFT
		if(c.girl.girl_type == 'Choosy'):
			c.happiness +=c.girl.happ_chsy(gifts)
		if(c.girl.girl_type == 'Norcmal'):
			c.happiness +=c.girl.happ_nr(gifts)
		if(c.girl.girl_type == 'Desperate'):
			c.happiness +=c.girl.happ_des(gifts)
#computing couple happiness from girl happiness
def couple_happ(C):
	for c in C:
		#print "hello"
		if(c.boy.boy_type == 'Miser'):
			c.happiness+=c.boy.budgt - sum([i.price for i in c.GIFT])
		if(c.boy.boy_type == 'Generous'):
			c.happiness *=2
		if(c.boy.boy_type == 'Geek'):
			c.happiness += c.girl.intel
	
def print_k(C,k):
	C = sorted(C,key = lambda x : x.happiness ,reverse = True)
	print "top " + str(k) + " pairs considering happiness"
	for c in C[0:k] :
		print 'Girl : ' + c.girl.name + ' Boy : ' + c.boy.name + ' happiness ' + str(c.happiness) 
	C = sorted(C,key = lambda x : x.compatibility,reverse = True)
	for c in C[0:k] :
		print 'Girl : ' + c.girl.name + ' Boy : ' + c.boy.name + ' compatibility ' + str(c.compatibility) 
	for c in C:
		print "list of gifts from boy:"+c.boy.name +" to the girl:"  + c.girl.name +":-"
		logging.info("gifts given by boy:"+c.boy.name+" to his girl:"+c.girl.name+":-")
		for g in c.GIFT:
			print g.name + ' '
			logging.info("boy " +c.boy.name+" gives gift "+g.name+" to the girl "+c.girl.name)

allocation()
