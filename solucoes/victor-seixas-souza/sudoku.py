import math

def num_to_list(num):
    return [int(x) for x in str(num)]

def list_to_num(lis):
    num = 0
    for x in lis:
        num = 10*num + x
    return num

def invert(num):
    l = num_to_list(num)
    l.reverse()
    return list_to_num(l)

def alldig(num):
    l = num_to_list(num)
    l.sort()
    allnum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return l == allnum

def mult(a):
    return range(math.ceil(100000000/a)*a,999999999,a)

def line1():
	print("Possibilities for the line (877, 127)")
	for num in mult(877):
	    if not alldig(num):
	        continue
	    if invert(num) % 127 != 0:
	        continue
	    l = num_to_list(num)
	    if l[6] == 5 or l[7] == 5 or l[8] == 5:
	    	continue
	    print(num)

def line2():
	print("Possibilities for the line (79, 29)")
	for num in mult(79):
	    if not alldig(num):
	        continue
	    if invert(num) % 29 != 0:
	        continue
	    l = num_to_list(num)
	    if l[3]+l[4]+l[5] != 15:
	        continue
	    if l[4] != 5:
	        continue
	    if l[3] == 4 or l[5] == 4:
	    	continue
	    print(num)

nlist = []
def line3():
	print("Possibilities for the line (11,5)")
	nlist = []
	d = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
	d[0] = set([5])
	d[1] = set([8])
	d[2] = set([3,4,9])
	d[3] = set([2])
	d[4] = set([7])
	d[5] = set([6])
	d[6] = set([4,9])
	d[7] = set([1])
	d[8] = set([3,9])
	for num in range(math.ceil(500000000/11)*11,599999999,11):
		if not alldig(num):
			continue
		l = num_to_list(num)
		comp = True
		for i in range(9):
			if l[i] not in d[i]:
				comp = False
				break
		if not comp:
			continue
		print(num)
		nlist.append(num)
	return nlist

def line4():
	print("Possibilities for the line (125)")
	nlist = []
	d = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
	d[0] = set([6])
	d[1] = set([8])
	d[2] = set([3,4,7,9])
	d[3] = set([7,9])
	d[4] = set([3,4,7])
	d[5] = set([3,4,9])
	d[6] = set([1])
	d[7] = set([2])
	d[8] = set([5])
	for num in mult(125):
		if not alldig(num):
			continue
		l = num_to_list(num)
		comp = True
		for i in range(9):
			if l[i] not in d[i]:
				comp = False
				break
		if not comp:
			continue
		print(num)
		nlist.append(num)
	return nlist

def line5():
	print("Possibilities for the line (17,2)")
	nlist = []
	d = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
	d[0] = set([6])
	d[1] = set([5])
	d[2] = set([1,7,9])
	d[3] = set([2])
	d[4] = set([8])
	d[5] = set([3])
	d[6] = set([7,9])
	d[7] = set([1,7,9])
	d[8] = set([4])
	for num in mult(17):
		if not alldig(num):
			continue
		l = num_to_list(num)
		comp = True
		for i in range(9):
			if l[i] not in d[i]:
				comp = False
				break
		if not comp:
			continue
		print(num)


def line6():
	print("Possibilities for the line (257,4)")
	nlist = []
	d = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
	d[0] = set([1,2,3,4,6,7,8])
	d[1] = set([2,4,6,8])
	d[2] = set([1,2,3,4,5,6,7])
	d[3] = set([2,3,4,5,7])
	d[4] = set([9])
	d[5] = set([1,3,5,7,8])
	d[6] = set([3,4,6,7,8])
	d[7] = set([1,2,3,5,6,7,8])
	d[8] = set([2,4,6,8])
	for num in mult(257):
		if not alldig(num):
			continue
		if invert(num) % 4 != 0:
			continue
		l = num_to_list(num)
		comp = True
		for i in range(9):
			if l[i] not in d[i]:
				comp = False
				break
		if not comp:
			continue
		print(num)
		nlist.append(num)
	return nlist

def line7():
	print("Possibilities for the line (4)")
	nlist = []
	d = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
	d[0] = set([9])
	d[1] = set([6])
	d[2] = set([5])
	d[3] = set([7,8])
	d[4] = set([1])
	d[5] = set([3])
	d[6] = set([2,7])
	d[7] = set([2])
	d[8] = set([4])
	for num in range(math.ceil(800000000/4)*4,999999999,4):
		if not alldig(num):
			continue
		l = num_to_list(num)
		comp = True
		for i in range(9):
			if l[i] not in d[i]:
				comp = False
				break
		if not comp:
			continue
		print(num)
		nlist.append(num)
	return nlist

def line8():
	print("Possibilities for the line (22)")
	nlist = []
	d = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
	d[0] = set([6,8,9])
	d[1] = set([3,6,8,9])
	d[2] = set([7])
	d[3] = set([5])
	d[4] = set([2,3,4,6,8])
	d[5] = set([1])
	d[6] = set([3,4,9])
	d[7] = set([3,4,8,9])
	d[8] = set([2])
	for num in mult(22):
		if not alldig(num):
			continue
		l = num_to_list(num)
		comp = True
		for i in range(9):
			if l[i] not in d[i]:
				comp = False
				break
		if not comp:
			continue
		print(num)
		nlist.append(num)
	return nlist
	
#	d = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
#	d[0] = set([1,2,3,4,5,6,7,8,9])
#	d[1] = set([1,2,3,4,5,6,7,8,9])
#	d[2] = set([1,2,3,4,5,6,7,8,9])
#	d[3] = set([1,2,3,4,5,6,7,8,9])
#	d[4] = set([1,2,3,4,5,6,7,8,9])
#	d[5] = set([1,2,3,4,5,6,7,8,9])
#	d[6] = set([1,2,3,4,5,6,7,8,9])
#	d[7] = set([1,2,3,4,5,6,7,8,9])
#	d[8] = set([1,2,3,4,5,6,7,8,9])


def line9():
	print("Possibilities for the line (8,2)")
	nlist = []
	d = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
	d[0] = set([4])
	d[1] = set([5,7,9])
	d[2] = set([5,7,9])
	d[3] = set([5,6,7,9])
	d[4] = set([8])
	d[5] = set([1])
	d[6] = set([3])
	d[7] = set([6,7,9])
	d[8] = set([2])
	for num in range(math.ceil(400000000/8)*8,499999999,8):
		if not alldig(num):
			continue
		l = num_to_list(num)
		comp = True
		for i in range(9):
			if l[i] not in d[i]:
				comp = False
				break
		if not comp:
			continue
		print(num)
		nlist.append(num)
	return nlist

def comp367():
	list3 = line3()
	list6 = line6()
	list7 = line7()
	for x in list6:
		for y in list3:
			for z in list7:
				lx = num_to_list(x)
				ly = num_to_list(y)
				ly.reverse()
				lz = num_to_list(z)
				comp = True
				for i in range(9):
					if lx[i] == ly[i]:
						comp = False
						break
					if lx[i] == lz[i]:
						comp = False
						break
					if ly[i] == lz[i]:
						comp = False
						break
				if not comp:
					continue
				print("Compatible", x, y, z)

def comp_hor():
	list8 = line8()
	list4 = line4()
	for x in list4:
		for y in list8:
			lx = num_to_list(x)
			lx.reverse()
			ly = num_to_list(y)
			comp = True
			for i in range(9):
				if lx[i] == ly[i]:
					comp = False
					break
			if not comp:
				continue
			print("Compatible", x, y)
			
			
# Solution
#234165789
#517928436
#689734125
#153492678
#968357241
#742816953
#321549867
#475681392
#896273514

def column(matrix, i):
    return [row[i] for row in matrix]

def check():
	solution = True
	s = [[2,3,4,1,6,5,7,8,9],
		 [5,1,7,9,2,8,4,3,6],
		 [6,8,9,7,3,4,1,2,5],
		 [1,5,3,4,9,2,6,7,8],
		 [9,6,8,3,5,7,2,4,1],
		 [7,4,2,8,1,6,9,5,3],
		 [3,2,1,5,4,9,8,6,7],
		 [4,7,5,6,8,1,3,9,2],
		 [8,9,6,2,7,3,5,1,4]]
	print("Solution")
	for l in s:
		for x in l:
			print(x, end=' ')
		print()
	
	
	print("Checking Lines:")
	for i in range(9):
		print("Line", i+1, end=":  ")
		l = s[i]
		for x in l:
			print(x, end=' ')
		if alldig(list_to_num(l)):
			print(" => CHECK")
		else:
			print(" => FAILURE!!!")
			solution = False
	
	print("Checking Columns:")
	for i in range(9):
		print("Column", i+1, end=":  ")
		l = column(s,i)
		for x in l:
			print(x, end=' ')
		if alldig(list_to_num(l)):
			print(" => CHECK")
		else:
			print(" => FAILURE!!!")
			solution = False
	
	print("Checking Squares:")
	for i in range(3):
		for j in range(3):
			print("Square", i+1, j+1, end=":  ")
			l = []
			for x in range(3):
				for y in range(3):
					l.append(s[3*i+x][3*j+y])
			print(l[0], l[1], l[2])
			print("            ", l[3], l[4], l[5])
			print("            ", l[6], l[7], l[8], end=' ')
			if alldig(list_to_num(l)):
				print(" => CHECK")
			else:
				print(" => FAILURE!!!")
				solution = False
	
	print("Checking Magic Square:")
	l = []
	for x in range(3):
		for y in range(3):
			l.append(s[3+x][3+y])
	print("Middle Square", end=":  ")
	print(l[0], l[1], l[2])
	print("               ", l[3], l[4], l[5])
	print("               ", l[6], l[7], l[8], end=' ')
	
	magic = True
	if l[0]+l[1]+l[2] != 15:
		magic = False
	if l[3]+l[4]+l[5] != 15:
		magic = False
	if l[6]+l[7]+l[8] != 15:
		magic = False
	if l[0]+l[3]+l[6] != 15:
		magic = False
	if l[1]+l[4]+l[7] != 15:
		magic = False
	if l[2]+l[5]+l[8] != 15:
		magic = False
	if l[0]+l[4]+l[8] != 15:
		magic = False
	if l[2]+l[4]+l[6] != 15:
		magic = False
	
	if magic:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Checking Divisibility:")
	
	print("Line   1 divisible by  22 <--", end=":  ")
	l = s[0].copy()
	l.reverse()
	num =list_to_num(l)
	print(num, "% 22 ==", num % 22, end="  ")
	if num % 22 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Line   2 divisible by   2 -->", end=":  ")
	num =list_to_num(s[1])
	print(num, "% 2 ==", num % 2, end="   ")
	if num % 2 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
		
	print("Line   3 divisible by 125 -->", end=":  ")
	num =list_to_num(s[2])
	print(num, "% 125 ==", num % 125, end=" ")
	if num % 125 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False

	print("Line   5 divisible by  29 -->", end=":  ")
	num =list_to_num(s[4])
	print(num, "% 29 ==", num % 29, end="  ")
	if num % 29 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Line   5 divisible by  79 <--", end=":  ")
	l = s[4].copy()
	l.reverse()
	num =list_to_num(l)
	print(num, "% 79 ==", num % 79, end="  ")
	if num % 79 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Line   8 divisible by   8 -->", end=":  ")
	num =list_to_num(s[7])
	print(num, "% 8 ==", num % 8, end="   ")
	if num % 8 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Line   8 divisible by   2 <--", end=":  ")
	l = s[7].copy()
	l.reverse()
	num =list_to_num(l)
	print(num, "% 2 ==", num % 2, end="   ")
	if num % 2 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Column 1 divisible by   4 -->", end=":  ")
	num =list_to_num(column(s,0))
	print(num, "% 4 ==", num % 4, end="   ")
	if num % 4 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Colimn 1 divisible by 257 <--", end=":  ")
	l = column(s,0).copy()
	l.reverse()
	num =list_to_num(l)
	print(num, "% 257 ==", num % 257, end=" ")
	if num % 257 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Column 3 divisible by   2 -->", end=":  ")
	num =list_to_num(column(s,2))
	print(num, "% 2 ==", num % 2, end="   ")
	if num % 2 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Colimn 3 divisible by  17 <--", end=":  ")
	l = column(s,2).copy()
	l.reverse()
	num =list_to_num(l)
	print(num, "% 17 ==", num % 17, end="  ")
	if num % 17 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Column 6 divisible by  11 -->", end=":  ")
	num =list_to_num(column(s,5))
	print(num, "% 11 ==", num % 11, end="  ")
	if num % 11 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Colimn 6 divisible by   5 <--", end=":  ")
	l = column(s,5).copy()
	l.reverse()
	num =list_to_num(l)
	print(num, "% 5 ==", num % 5, end="   ")
	if num % 5 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Column 7 divisible by 127 -->", end=":  ")
	num =list_to_num(column(s,6))
	print(num, "% 127 ==", num % 127, end=" ")
	if num % 127 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Colimn 7 divisible by 877 <--", end=":  ")
	l = column(s,6).copy()
	l.reverse()
	num =list_to_num(l)
	print(num, "% 877 ==", num % 877, end=" ")
	if num % 877 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	print("Column 9 divisible by   4 -->", end=":  ")
	num =list_to_num(column(s,8))
	print(num, "% 4 ==", num % 4, end="   ")
	if num % 4 == 0:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	
	if solution:
		print("SOLUTION CHECKED!")
	else:
		print("SOLUTION FAILED!")

	diagonal = list_to_num([s[i][i] for i in range(9)])
	print("Main diagonal : ", diagonal)
	print("2*3*61*109*5501 = ", 2*3*61*109*5501, end=' ')
	if diagonal == 2*3*61*109*5501:
		print(" => CHECK")
	else:
		print(" => FAILURE!!!")
		solution = False
	return s
	
s = check()

