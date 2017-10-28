import numpy as np

def crazyfunction(x):

    # Does a complicated function of x
    # take the 100th through 200th highest values
    b = np.sort(x)[-200:-100]

    # compute the exponential average of these
    val = -np.log(np.mean(np.exp(-b)))

    # take the result to the power of the cube root of itself.
    val = np.power(val,np.power(val,1.0/3.0))

    return val

samplesize = 1000
# generate 1000 random numbers between 0 and 10

xorig = 10*np.random.random(size=samplesize)

#Value of the function
print("Value of the function on representative data set: {:8.3f}".format(crazyfunction(xorig)))

# do it 2000 times to get statistics.

ntrials = 2000
results = np.zeros(ntrials)

for i in range(ntrials):
    x = 10*np.random.random(size=samplesize)  # generate the data 10 times
    results[i] = crazyfunction(x)

print("Repeated sampling: {:8.3f}".format(np.std(results)))

# now, do it by bootstrap.
xb = np.zeros(samplesize)
for i in range(ntrials):
    #
    # insert the lines here (could be as few as 2) to do the bootstrap test.
    #
    results[i] = crazyfunction(xb)

print("Bootstrap sampling: {:8.3f}".format(np.std(results)))
