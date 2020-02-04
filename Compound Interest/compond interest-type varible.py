#£ily Lin
#2020/2/2
'''
k = 360   daily or 365
k = 52    weekly
k = 12    monthly
k = 2     semi-annuly
k = 1     annuly
'''
#Amount = p(1+r)^n
#n = years
# r = rate
# t = years after
'''
if the decimal is too long, ignore the one that behind alot of zeros
and if the last place is different than the previous repeted places

example: 0.999999999999998  = 1
         375.0000000000007  = 375

please round it into the most resent place
**this occurs becasue it convert from binary to decimal 
'''

# type
print("""type the value in the function:
      example:
      Annually compund:
      aca(P,r,n):
      acp(A,r,n):
      acr(A,P,n):
      acn(A,P,r):
      interest compound k times per year:
      cia(P,r,k,t):
      cip(A,r,k,t):
      cit(k,A,P,r):
      cir(A,P,k,t):
      cik(A,P):
      interest compound continously:
      era(P,r,t):
      err(A,P,t):
      ert(A,P,r):
      Annuity future value:
      fv(R,i,n):
      fvr(FV,i,n):
      Annuities Present Value:
      pv(R,i,n):
      pvr(PV,i,n):   """)
import math
e = math.e
"""-----------------Annually compound-------------------------------"""
#annually compound: find A
def aca(P,r,n):
    A = P*((1 + r)** n)
    return A

#annually compound: find P
def acp(A,r,n):
    pp = A/((1+r)**n)
    return pp

#annuly compound: find r
def acr(A,P,n):
    rr = ((A/P)**(1/n))-1
    return rr

#annuly compound: find n
def acn(A,P,r):
    nn = math.log((A/P),(1+r))
    return nn

"""--------------------interest compond k times per year----------------------------"""
#compound interest : find A
def cia(P,r,k,t):
    A = P*((1 + (r/k))** (k*t))
    return A

#compound interest : find P
def cip(A,r,k,t):
    pp = A/((1 + (r/k))** (k*t))
    return pp

#compound interest : find t
def cit(k,A,P,r):
    tt = (1/k)*math.log((A/P),(1 + (r/k)))
    return tt

#compound interest : find r (APY)
def cir(A,P,k,t):
    rr = ((A/P)**(1/(k*t)))-1
    return rr

#note that k and t always > 0, 1^kt = 1
#**compound interest : find (r/k)^kt = (A/P)-1
def cik(A,P):
    kk = (A/P)-1
    return "(r/k)**(k*t) is:"+ kk

"""---------------------interest compound continuously---------------------------"""

#effective rate: find A
def era(P,r,t):
    A = P*(e**(r*t))
    return A

#effective rate: find r 
def err(A,P,t):
    er = (math.log(A/P))/t
    return er

#effective rate: find t
def ert(A,P,r):
    et = (math.log(A/P))/r
    return et

"""------------------Annuity future value------------------------------"""

#Future Value of an Annuity: find FV
def fv(R,i,n):
    FV = R*((((1+i)**n)-1)/i)
    return FV

#Future Value of an Annuity: find R
def fvr(FV,i,n):
    rr = (FV*i)/(((1+i)**n)-1)
    return rr


"""----------------------Annuities Present Value--------------------------"""
#Present Value of an Annuity: find PV
def pv(R,i,n):
    PV = R*((1-((1+i)**(-n)))/i)
    return PV

#Present Value of an Annuity: find PV
def pvr(PV,i,n):
    rr = (PV*i)/(1-((1+i)**(-n)))
    return rr 




    
    
 
