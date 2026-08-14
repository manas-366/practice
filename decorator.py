def sqrt(sqrtv):
    def cal():
        sqrv,n1=sqrtv()
        res=n1**0.5
        return sqrv,n1, res
    return cal


def square(v):
    def calculate():
        n=v()
        res=n**2
        return res,n
    return calculate
    
@sqrt
@square
def get_val():
    return int(input("enter your number :"))
r1,val,r2=get_val()
print(f'the value is {r1}')
print(f'the value is {val}')
print(f'the value is {r2}')
