n=input("Enter the mobile number:")
n=[int(i) for i in n]
nlist=[0,1,2,3,4,5,6,7,8,9]
chk=[i for i in nlist if i not in n]
print(chk)