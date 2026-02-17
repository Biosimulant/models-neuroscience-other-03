# AMPAR-trafficking-heterosynaptic-plasticity
Codes of the paper: AMPA receptor trafficking and its role in heterosynaptic plasticity (SREP-17-56929)
 www.nature.com/articles/s41598-018-28581-w 

Fig1: code for fig 1. We ran simulations with different amounts of anchors and different values of kb for 
the dissociation reaction (anchorAMPAR -> anchor + AMPAR).

Fig2_7: code used for figs 2-7. The initial 30 s of simulations should be used to allow the system to reach steady-state.
We removed this interval in the figs. 
To simulate LTP or LTD, just set the amount of enzLTP (or enzLTD) to be released using release_pattern 1 or 2.

Fig8_9: two-state model of LTP/LTD.We used the initial 40 s of simulations to allow the system to reach steady-state. 
