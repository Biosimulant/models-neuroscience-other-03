
The files in this directory form an implementation of a BCM-like
synaptic plasticity rule in a conductance-based model. The simulation
environment is NEURON.  The model contains Na, KDR, KA and h currents,
and employs GHK-based implementations of AMPA and NMDA receptors.
Whereas the MOD files for the channel and receptor currents were
derived from previous studies, the main files associated with this
model are Fig2.hoc and Wghkampa.mod. Fig2.hoc helps recreate Fig.
2A and Fig. 2B of the following paper:

Narayanan R, Johnston D. The h current is a candidate mechanism for 
regulating the sliding modification threshold in a BCM-like synaptic 
learning rule.  J Neurophysiol. 2010 Aug; 104(2):1020-33. doi: 
10.1152/jn.01129.2009.  PubMed PMID: 20554832. PubMed Central PMCID: 
PMC2934916.

Running the functions Fig2A() and Fig2B() in the file Fig2.hoc will
create files that will contain data for plotting Fig. 2A and Fig.
2B of the paper, respectively. Example outputs that were obtained
by running Fig2A() and Fig2B() are also provided as TXT files in
this directory. A calcium-based synaptic plasticity rule (from
Shouval et al., PNAS, 2002) is incorporated into the model to update
the weight, and these weight updates are performed in the MOD file
"Wghkampa.mod".

Implemented by Rishikesh Narayanan. Contact rishi.n@gmail.com.
