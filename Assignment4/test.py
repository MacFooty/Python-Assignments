import matrix as mx
ans=''
while(ans.lower()!='q'):
	print("1.Matrix transpose\n2.Matrix determinant\n3.Matrix addition\n4.Matrix multiplication\n5.Matrix inverse\nQ.Quit\n")
	print("Enter your response: ")
	ans=input()
	if(ans=='1'):
		r=int(input("Number of rows: "))
		matrix=[]
		for i in range(r):
			row=list(map(float,input("Enter the elements of row "+str(i+1)+str(": ")).split()))
			matrix.append(row)
		print(mx.matrix_transpose(matrix))
	if(ans=='2'):
		
		matrix=[]
		for i in range(2):
			row=list(map(float,input("Enter 2 elements of row "+str(i+1)+str(": ")).split()))
			matrix.append(row)
		print(mx.matrix_det(matrix))
	if(ans=='3'):
		matrices=[]
		for k in range(2):
			r=int(input("Number of rows of matrix "+str(k+1)+": "))
			matrix=[]
			for i in range(r):
				row=list(map(float,input("Enter the elements of row "+str(i+1)+str(": ")).split()))
				matrix.append(row)
			matrices.append(matrix)
		print(mx.matrix_add(matrices[0],matrices[1]))
	if(ans=='4'):
		matrices=[]
		for k in range(2):
			r=int(input("Number of rows of matrix "+str(k+1)+": "))
			matrix=[]
			for i in range(r):
				row=list(map(float,input("Enter the elements of row "+str(i+1)+str(": ")).split()))
				matrix.append(row)
			matrices.append(matrix)
		print(mx.matrix_mult(matrices[0],matrices[1]))
	if(ans=='5'):
		r=int(input("Number of rows (2 or 3): "))
		matrix=[]
		for i in range(r):
			row=list(map(float,input("Enter the elements of row "+str(i+1)+str(": ")).split()))
			matrix.append(row)
		print(mx.matrix_inverse(matrix))


