import numpy as np

# number of data points to throw out as unequilibrated 
nequil = 500

# temperatures we ran at
temps = [220,230]
tlow = temps[0]
thigh = temps[1]

# Boltzmann constant in kJ/mol*K
kb = 0.008314

data = dict()
experiments = [1,2]  # two sets of experiments.
for e in experiments:
    for t in temps:
        # load in data for the experiment.
        filename = 'isobutane_' + str(t) + 'K_' + str(e) + '.xvg'
        f = open(filename,'r')
        lines = f.readlines()
        f.close()
        evals = list()
        for l in lines:
            if l[0] not in ['#','@']:
                evals.append(np.float(l.split()[1]))
        data[t] = np.array(evals)

    # now compute heat capacity using fluctuation formula.
    Cv_fluct = ((np.std(data[tlow][nequil:])/tlow)**2)/kb
    print("CV through fluctuations {:8.4f}".format(Cv_fluct))

    # can you compute through the difference formula?
    Cv_diff = 0
    print("CV through finite difference {:8.4f}".format(Cv_diff))

