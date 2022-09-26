#!/usr/bin/python3

#Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
#https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
#or like sw.PNG

def print_matrix1(a,x,y):
	mrows = len(x)
	ncols = len(y)

	#Print string y values as columns
	for j in range(ncols+1):
		if(j>0):
			print("%s " %y[j-1], end=' ');
		else:
			print("     ", end=' ');
	print();

	#Print rows of matrix
	for i in range(mrows+1):

		# print string x values at start of rows
		if(i==0): # skip first row
			print(" ", end=' ');
		else:
			print("%s"%x[i-1], end=' ');

		# print values in the matrix by row
		for j in range(ncols+1):
			print("%2d" % a[i][j], end=' ')
		print()
	print()


def gen_matrix(x, y, match_score=3, gap_cost=2):
	mrows = len(x)
	ncols = len(y)
	max_val = 0

	#initialize matrix to zeroes
	a = [0] * (mrows + 1)
	for i in range(mrows + 1):
		a[i] = [0] * (ncols + 1)
	
	#print_matrix(a,x,y)
	
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			match = a[i-1][j-1] - match_score
			if(x[i-1] == y[j-1]):
				match = a[i-1][j-1] + match_score
			delete = a[i - 1][j] - gap_cost
			insert = a[i][j - 1] - gap_cost
			a[i][j]=max(match,delete,insert,0)

			if(a[i][j]>max_val):
				max_val = a[i][j]
				max_i = i
				max_j = j

	#print_matrix(a,x,y)	
	return(a,max_i,max_j)


def backtrace(a,x,y,i,j,match_score=3, gap_cost=2):
	'''
	@desc: trace and print the alignment
	@params:
		a - generated matrix	
		x - string x 
		y - string y
		i - row index of matrix max value
		j - column index of matrix max value
	'''

	u = "" # upper sequence
	l = "" # lower sequence
	al = "" # alignment
	
	while(a[i][j]>0):
		#start with highest value in the matrix
		if(x[i-1] == y[j-1]):
			u = x[i-1] + u  # add to alignment
			l = y[j-1] + l 	# add to alignment
			al = "|" + al
			i -= 1
			j -= 1
		else:
			# find next max value
			max_val = max(a[i-1][j-1], a[i-1][j], a[i][j-1])

			if(a[i-1][j] == max_val): #check upper block
				u = "-" + u # add gap
				l = x[i-1] + l  # add to alignment
				al = "|" + al 
				i -= 1 
			elif(a[i][j-1] == max_val): #check left block
				u = y[j-1] + u  # add to alignment
				l = "-" + l # add gap
				al = "|" + al
				j -= 1
			else: #check diagonal block  
				u = x[i-1] + u  # add to alignment
				l = y[j-1] + l 	# add to alignment
				al = " " + al  # not equal
				i -= 1
				j -= 1

	print(" ".join(u))
	print(" ".join(al))
	print(" ".join(l))
	return

def main():
	x = "AGCACACA"	
	y = "ACACACTA"

	a,max_i,max_j=gen_matrix(x,y)
	print_matrix1(a,x,y)
	backtrace(a,x,y,max_i,max_j)


if __name__ == "__main__":
	main()
