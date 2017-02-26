import csv
from q1_b  import boy
from q1_g  import girl
from q1_utility import utility
import logging


utility()

logging.basicConfig(filename='q1_log.txt',
			format='%(asctime)s %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
					level=logging.DEBUG,
						filemode='w')

def allocation():
	

	with open('boys.csv','r') as csvbfile:
		b_read = csv.reader(csvbfile , delimiter = ',')
		B = [boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),(row[5])) for row in b_read]
		csvbfile.close()
	with open('girls.csv','r') as csvgfile:
		g_read = csv.reader(csvgfile , delimiter = ',')
		G = [girl(row[0],int(row[1]),int(row[2]),int(row[3]),(row[4])) for row in g_read]
		csvgfile.close()
	logging.info("matching is taking place:\n")
	for g in  G:
		for b in  B:
			logging.info("checking if girl:"+g.name+"matches with boy:"+b.name);
			if(g.check_eligible(b) and b.check_eligible(g)and g.status == 'single' and b.status == 'single'):

				b.status = 'commited'
				g.status = 'commited' 
				logging.info("girl:-" + g.name + " got commited with boy:-" + b.name)
				b.girlfrnd = g.name
				g.boyfrnd = b.name
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
			
			
allocation()
