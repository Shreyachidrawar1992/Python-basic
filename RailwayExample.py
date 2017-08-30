tr_arr = [900, 940, 950, 1100, 1500, 1800]
tr_dep = [910, 1200, 1120, 1130, 1900, 2000]

new_list = sorted(tr_arr)
print new_list
n = len(tr_arr)# Total number of trains

plat_needed = 1 # initially
result = 1
i = 1
j = 0

while (i < n and j < n):
      if tr_arr[i] < tr_dep[j]:
        plat_needed = plat_needed+1
        i=i+1
        if (plat_needed > result):
            result = plat_needed
      else:
        plat_needed = plat_needed-1
        j=j+1

print 'Total number of platforms required = '+str(result)