# Generators don't hold entire results in the memory. It yield one result at a time.

# It is much more readable.

# It is used for performance. As it does not store all the(entire) values at once.it does not take much memory.
# Better performance in terms of Memory as well as execution time
# It is used over list when there are ton or millions of values.

# def squareNumbers_list(numberList):
#     results = list()
#     for i in numberList:
#         results.append(i*i)
#     return results
#
# results = squareNumbers_list([1,2,3,4,5])
# print results


def squareNumbers_generators(numberList):
    for i in numberList:
       results= yield (i*i)

results = squareNumbers_generators([1,2,3,4,5])
#print next(results)

for num in results:
    print num