def finddHCF(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if ((x%i==0) and (y%i==0)):
            hcf=i
    return hcf
print('THe HCf of the given number is:',finddHCF(12, 30))

