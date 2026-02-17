README_R15.txt

The goal of the present simulation is to 
illustrate how SNNAP can be used to simulation
the biophysical properties of a relatively
complex neuron. 

The R15 model is based on models originally
published by Canavier et al. (1991) and 
Butera et al. 1995: 

Butera, R.J., Clark, J.W., Canavier, C.C., 
Baxter, D.A., and Byrne, J.H.  (1995)
Analysis of the effects of modulatory agents
on a modeled bursting neuron: dynamic
interations between voltage and calcium
dependent systems.  J. Comput. Neurosci.
2: 19-44.

Canavier, C.C., Clark, J.W. and Byrne, J.H.
(1991)  Simulation of the bursting activity
of neuron R15 in Aplysia: role of ionic
currents, calcium balance, and modulatory 
transmitters.  J. Neurophysiol. 66: 2107-2124.

The components of the R15 neuron are illustrated
in R15_neu.jpg and Butera_model.jpg. 
The model contains eight ionic conductances,
an intracellular pool of calcium (i.e.,
Ca.ion), an intracellular pool of second messenger
(i.e., cAMP.sm), and modulatory interactions from
the ion and second messenger pools and the
membrane conductances.

The results of the default simulation are illustrated
in R15_ous.jpg.  The model produces endogenous
bursting activity.  At time=60sec a modulator
is applies via the treatment file (i.e., R15.trt).
The resultant increase in the second messenger and 
modulation of membrane conductances alters the 
electrical activity of the neuron.


