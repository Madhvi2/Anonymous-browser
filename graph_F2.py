import random
import networkx as nx
from networkx.generators.classic import empty_graph
import fileinput



node_count = input("Enter the number of nodes you want to create:")             #numer of nodes for which graph is to be created

m = input("\nEnter the minimum degree it should have:")                         #minimum degree of the graph


G = nx.Graph()
G.add_nodes_from([0,1,2])                                                       #manual creation of graph of three nodes
G.add_edges_from([(0,1),(0,2),(1,2)])


selection_set = [0,1,2]
source = 3

if m < 1 or  m >= node_count:                                                   #graph creation
     raise nx.NetworkXError("\nScale-Free network must have m>=1\
      and m<node_count, m=%d,node_count = %d"%(m,node_count))
G.name = "Scale-Free network"

while source < node_count:
   x = random.choice(selection_set)                                             #preferential attachment
   selection_set.append(x)
   G.add_edge(source,x)
   count = 1
   while count < m:
        p = random.random()
        neighborhood = [nbr for nbr in selection_set \
                               if not G.has_edge(source,nbr) \
                               and not nbr == source]
        if neighborhood:                                                        #clustering cofficient
           nbr = random.choice(neighborhood)
           G.add_edge(source,nbr) 
           selection_set.append(nbr)
                 
        count = count+1
        
   selection_set.extend([source]*m)
   source +=1


f = open("neighbours.txt",'w')                                                  #writting neighbours of all nodes to a neighbour.txt file
for i in range (0,node_count):
  f.write(str(G.neighbors(i)) + "\n")

f.close()


f = open("deg_all.txt",'w')                                                     #writting degree of all nodes to deg_all txt and used only
for i in range (0,node_count):                                                  #once at the time of creation of graph
  f.write(str(i) + " " + str(G.degree(i)) + "\n")

f.close()



variable = map(chr, range(97,123))                                                # assigning randon variable to nodes and writing to variable.txt file
f = open("variable.txt", 'w')
for i in range (0,node_count):
  f.write(random.choice(variable) + "\n")
f.close()


ch ='y'
while ch == 'y':

	 
	node = input("Enter the  node to examined: ")                                   #enter the node to be examined
	fin1 = open ("neighbours.txt","r")
	
	
	finx = open ("variable.txt","r")	
	p = 0
	while(p < node):
	    finx.readline()
	    p +=1

	st1 = finx.readline()                                                            #writing the variable of a node to a list 
	finx.close()





	i = 0
	while(i<node):
	    fin1.readline()
	    i +=1

	st = fin1.readline()                                                            #writing the neighbours of a node to a list 
	li = eval(st)
	fin1.close()

	def quickSort(unsortedList):                                                    #quicksort 
	
	
		if len(unsortedList) <= 1:
			return unsortedList

	
		pivotIndex = int(len(unsortedList)/2)
		pivotElement = unsortedList.pop(pivotIndex)

		lessThanList = []
		greaterThanList = []
	
	
		for item in unsortedList:
			if item <= pivotElement:
				lessThanList.append(item)
			else:
				greaterThanList.append(item)

		sortedList = []
	
		if len(lessThanList) > 0:
			sortedList.extend(quickSort(lessThanList))
	
		sortedList.append(pivotElement)

		if len(greaterThanList) > 0:
			sortedList.extend(quickSort(greaterThanList))
	
		return sortedList
	


	myList = li
	deg_node = len(myList)
	mysortedlist = quickSort(myList)                                              # list of sorted neighbours for making analysis easy


	a_count = 0
	b_count = 0
	c_count = 0
	d_count = 0
	e_count = 0
	f_count = 0
	g_count = 0
	h_count = 0
	i_count = 0
	j_count = 0
	k_count = 0
	l_count = 0
	m_count = 0
	n_count = 0
	o_count = 0
	p_count = 0
	q_count = 0
	r_count = 0
	s_count = 0
	t_count = 0
	u_count = 0
	v_count = 0
	w_count = 0
	x_count = 0
	y_count = 0
	z_count = 0

	t =0
	while(t <  len (mysortedlist)):                                               #checking for each neighbour the variable selected based upon the maximum
		fin1 = open ("neighbours.txt","r")                                    #degree among its neighbours
	
		node1 = mysortedlist[t]
		i = 0
		while(i<node1):
		    fin1.readline()
		    i +=1

		st = fin1.readline()
		li1 = eval(st)
		fin1.close()   #added
	       	myList1 = li1
		mysortedlist1 = quickSort(myList1) 
	

		neighbor_degree = [[]]                                             # calculating the highest degree among the neigbours of a node
		f = open("degree.txt", 'w')
		for i in range (0,len(mysortedlist1)):
		    x = mysortedlist1[i]
		    neighbor_degree.append([str(x), str(G.degree(x))])	
		    f.write(str(x) + ":" + str(G.degree(x)) + ":" + "\n" ) 
		f.close()

		d = [[]]
		l = 0
		f = open("degree.txt","r")
		while( l < len(mysortedlist1)):
		   x = f.readline()
		   y = x.split(':')[0]
		   z = x.split(':')[1]
		   d.append([int(z),int(y)])
		   l +=1

		d.remove([])
		v = min(d)                                                             # THE MINIMUM ELEMENT IS SELECTED
		h = v[1]
	     	f.close()


	     	fin2 = open("variable.txt","r")                                    #getting variable from the file correseponding to a particular node
		s = 0
		while(s < h):
		    fin2.readline()
		    s += 1

		var = fin2.readline()
		print var
	
	
		if var[0] == "a":
		     a_count += 1
		     
		elif var[0] == "b":
		     b_count += 1
		     
		elif var[0] == "c":
		     c_count += 1
		     
		elif var[0] == "d":
		     d_count += 1
		     
		elif var[0] == "e":
		     e_count += 1
		     
		elif var[0] == "f":
		     f_count += 1
		     
		elif var[0] == "g":
		     g_count += 1
		     
		elif var[0] == "h":
		     h_count += 1
		     
		elif var[0] == "i":
		     i_count += 1
		     
		elif var[0] == "j":
		     j_count += 1
		     
		elif var[0] == "k":
		     k_count += 1
		     
		elif var[0] == "l":
		     l_count += 1
		     
		elif var[0] == "m":
		     m_count += 1


		elif var[0] == "n":
		     n_count += 1
		     
		elif var[0] == "o":
		     o_count += 1
		     
		elif var[0] == "p":
		     p_count += 1
		     
		elif var[0] == "q":
		     q_count += 1
		     
		elif var[0] == "r":
		     r_count += 1
		     
		elif var[0] == "s":
		     s_count += 1
		     
		elif var[0] == "t":
		     t_count += 1
		     
		elif var[0] == "u":
		     u_count += 1
		     
		elif var[0] == "v":
		     v_count += 1
		     
		elif var[0] == "w":
		     w_count += 1
		     
		elif var[0] == "x":
		     x_count += 1
		     
		elif var[0] == "y":
		     y_count += 1
		         
		     
		else:
		     z_count += 1             
		fin2.close()

		"""		
		fin2 = open("variable.txt","r+")                                   # UPDATING variable.txt
		s = 0
		while(s < node1):
		    fin2.readline()
		    s += 1

		fin2.write(var)
	     	fin2.close() 
		"""
		
		fin3 = open("log_minimum.txt", "a")                                        # WRITING OUTPUT to the log.txt file	
		fin3.write(str(node1) + "\t" + var)
		fin3.close()            #ADDED
		
	     	t +=1


	fin3 = open("log_minimum.txt","a")

	fin3.write('node choosen: ' + str(node) + "\t\twith degree: " + str(deg_node) + "\t with variable: " + str(st1) + "\n")
	fin3.write('a count is' + "\t" + str(a_count) + "\n")

	fin3.write('b count is' + "\t" + str(b_count) + "\n")

	fin3.write('c count is' + "\t" + str(c_count) + "\n")

	fin3.write('d count is' + "\t" + str(d_count) + "\n")

	fin3.write('e count is' + "\t" + str(e_count) + "\n")

	fin3.write('f count is' + "\t" + str(f_count) + "\n")

	fin3.write('g count is' + "\t" + str(g_count) + "\n")

	fin3.write('h count is' + "\t" + str(h_count) + "\n")

	fin3.write('i count is' + "\t" + str(i_count) + "\n")

	fin3.write('j count is' + "\t" + str(j_count) + "\n")

	fin3.write('k count is' + "\t" + str(k_count) + "\n")

	fin3.write('l count is' + "\t" + str(l_count) + "\n")

	fin3.write('m count is' + "\t" + str(m_count) + "\n")

	fin3.write('n count is' + "\t" + str(n_count) + "\n")

	fin3.write('o count is' + "\t" + str(o_count) + "\n")

	fin3.write('p count is' + "\t" + str(p_count) + "\n")

	fin3.write('q count is' + "\t" + str(q_count) + "\n")

	fin3.write('r count is' + "\t" + str(r_count) + "\n")

	fin3.write('s count is' + "\t" + str(s_count) + "\n")

	fin3.write('t count is' + "\t" + str(t_count) + "\n")

	fin3.write('u count is' + "\t" + str(u_count) + "\n")

	fin3.write('v count is' + "\t" + str(v_count) + "\n")

	fin3.write('w count is' + "\t" + str(w_count) + "\n")

	fin3.write('x count is' + "\t" + str(x_count) + "\n")

	fin3.write('y count is' + "\t" + str(y_count) + "\n")

	fin3.write('z count is' + "\t" + str(z_count) + "\n\n\n\n")
	fin3.close()
	
	ch = raw_input("Do you want to continue (y/n): ")
	if ch == 'y':
		continue
	else:
		break
	
