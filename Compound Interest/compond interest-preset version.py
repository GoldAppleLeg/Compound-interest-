##£ily Lin
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
note that you can change the value in the shell
this is the preset

if the decimal is too long, ignore the one that behind alot of zeros
and if the last place is different than the previous repeted places

example: 0.999999999999998  = 1
         375.0000000000007  = 375

please round it into the most resent place
**this occurs becasue it convert from binary to decimal 
'''
import math
#the preset: set your value here
A = 5000
k = 1
t = 20
P = 4000
r = 0.08

n = 10

FV = 1000
PV = 1000
R = 0.01
i = 0.7

e = math.e
"""-----------------Annuly compound-------------------------------"""
#annuly compound: find A
def aca():
    A = P*((1 + r)** n)
    return A

#annuly compound: find P
def acp():
    pp = A/((1+r)**n)
    return pp

#annuly compound: find r
def acr():
    rr = ((A/P)**(1/n))-1
    return rr

#annuly compound: find n
def acn():
    nn = math.log((A/P),(1+r))
    return nn


"""--------------------interest compond k times per year----------------------------"""


#compound interest : find A
def cia():
    A = P*((1 + (r/k))** (k*t))
    return A

#compound interest : find P
def cip():
    pp = A/((1 + (r/k))** (k*t))
    return pp

#compound interest : find t
def cit():
    tt = (1/k)*math.log((A/P),(1 + (r/k)))
    return tt

#compound interest : find r (APY)
def cir():
    rr = ((A/P)**(1/(k*t)))-1
    return rr

#note that k and t always > 0, 1^kt = 1
#**compound interest : find (r/k)^kt = (A/P)-1
def cik():
    kk = (A/P)-1
    return "(r/k)**(k*t) is:"+ kk

"""---------------------interest compound continuously---------------------------"""

#effective rate: find A
def era():
    A = P*(e**(r*t))
    return A

#effective rate: find r 
def err():
    er = (math.log(A/P))/t
    return er

#effective rate: find t
def ert():
    et = (math.log(A/P))/r
    return et

"""------------------Annuity future value------------------------------"""

#Future Value of an Annuity: find FV
def fv():
    FV = R*((((1+i)**n)-1)/i)
    return FV

#Future Value of an Annuity: find R
def fvr():
    rr = (FV*i)/(((1+i)**n)-1)
    return rr


"""----------------------Annuities Present Value--------------------------"""
#Present Value of an Annuity: find PV
def pv():
    PV = R*((1-((1+i)**(-n)))/i)
    return PV

#Present Value of an Annuity: find PV
def pvr():
    rr = (PV*i)/(1-((1+i)**(-n)))
    return rr 

"""----------------------APY--------------------------"""
def apy():
    APY = ((1+(r/k))**k)-1
    return APY
    
    
 
