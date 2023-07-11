s = "cdeenetpi" 
a = [5,2,0,1,6,4,8,3,7]
msg = ""
for i in range(0, len(a)-1):  #run this one time less to disallow the last append (e,0)
    if (i==0):
        msg = msg+s[i]  # for the first exception we are going to append first value regardless of any logic
        delta_var = a[i]  # update the pointer to find out next value to visit ( a[0] = 5)
    
    msg = msg+s[delta_var]   # now the values will be appended acc to the address of the visited variable
    delta_var = a[delta_var]  # update the visited address to hop on to next directed graph entry
    
print (msg)

     