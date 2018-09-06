import functools as f
def matrix_mult(a,b):
    ca=len(a[0])
    rb=len(b)
    def foo(i,k):
        ans=[a[i][j]*b[j][k] for j in range(rb)]
        return f.reduce(lambda x,y:x+y,ans)
    if(ca==rb):
        c=[[foo(i,j)for j in range(len(b[0]))]for i in range(len(a))]
        return c
    else:
        print("Cannot perform matrix multiplication between "+ str(len(a))+"-by-"+str(len(a[0]))+" matrix and "+str(len(b))+"-by-"+str(len(b[0]))+" matrix")
        
        

def matrix_det(matrix_A):
    try:
        assert(len(matrix_A)<=2 and len(matrix_A)==len(matrix_A[0]))
        if(len(matrix_A)==1):
            return matrix_A[0]
        else:
            return matrix_A[0][0]*matrix_A[1][1]-matrix_A[0][1]*matrix_A[1][0]
    except AssertionError:
        if(len(matrix_A)!=len(matrix_A[0])):
            print("Cannot calculate determinant of a non-square matrix.")
        else:
            print("Cannot calculate determinant of a "+str(len(matrix_A))+"-by-"+str(len(matrix_A))+" matrix.")


def matrix_transpose(matrix_A):
    return [[matrix_A[j][i] for j in range(len(matrix_A))] for i in range(len(matrix_A[0]))]

def matrix_add(a,b):
    if(len(a)!=len(b) or len(a[0])!=len(b[0])):
        print("Cannot perform matrix addition between a-by-b matrix and c-by-d matrix")
    else:
        return [[a[i][j]+b[i][j]for j in range(len(a[0]))]for i in range(len(a))]

def matrix_inverse(a):
    import numpy as np
    if(len(a)!=len(a[0])):
        print("Inverse is only defined for square matrices.")
    else:
        try:
            det=a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
            ans=[[matrix_det([[a[1][1],a[1][2]],[a[2][1],a[2][2]]]),matrix_det([[a[0][2],a[0][1]],[a[2][2],a[2][1]]]),matrix_det([[a[0][1],a[0][2]],[a[1][1],a[1][2]]])],[matrix_det([[a[1][2],a[1][0]],[a[2][2],a[2][0]]]),matrix_det([[a[0][0],a[0][2]],[a[2][0],a[2][2]]]),matrix_det([[a[0][2],a[0][0]],[a[1][2],a[1][0]]])],[matrix_det([[a[1][0],a[1][1]],[a[2][0],a[2][1]]]),matrix_det([[a[0][1],a[0][0]],[a[2][1],a[2][0]]]),matrix_det([[a[0][0],a[0][1]],[a[1][0],a[1][1]]])]]
        except ZeroDivisionError:
            print("The matrix is not invertible.")
        return 1/det*np.matrix(ans)



