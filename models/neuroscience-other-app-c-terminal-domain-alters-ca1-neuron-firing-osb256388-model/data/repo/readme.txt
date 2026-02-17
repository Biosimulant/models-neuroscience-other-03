
NEURON files from the paper: 

The Amyloid Precursor Protein C-terminal domain alters CA1 neuron firing, modifying hippocampus oscillations and impairing spatial memory encoding by Paula A. Pousinha, Xavier Mouska, Daniela Bianchi, Mariana Temido-Ferreira, Joana Rajão-Saraiva, Rui Gomes, Sebastian P. Fernandez, Ana Rita Salgueiro-Pereira, Carine Gandin, Elisabeth F. Raymond, Jacques Barik, Luisa V. Lopes, Michele Migliore, Romain Goutagny, Ingrid Bethus and Hélène Marie (2019). Cell Reports. In press.


The CA1 pyramidal cell model is the one previously validated against experimental findings and used to build a network (Bianchi et al., 2014, ModelDB accession number 151126). We optimized the neuron model to reproduce the number of spikes observed experimentally under control conditions as a function of a somatic current injection.

The testcell.hoc file will reproduce the results in Fig. 5A of the paper (CTR case). 
Setting the variable somacaL=0.01 in testcell.hoc and soma_kca=0.005 in pyramidalcell4b.hoc, the results shown in Fig. 5B (AICD case) will be displayed.


Questions on the NEURON simulation should be addressed to
(replace -at- with the usual @ symbol):
danielabianchi12-at-gmail.com
michele.migliore-at-cnr.it

Changelog
---------
2022-05: Updated MOD files to contain valid C++ and be compatible with the upcoming versions 8.2 and 9.0 of NEURON.
