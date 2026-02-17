NEURON mod files from the paper:

Cassarà AM, Hagberg GE, Bianciardi M, Migliore M, Maraviglia B.
Realistic simulations of neuronal activity: A contribution to the
debate on direct detection of neuronal currents by MRI.
Neuroimage. 39:87-106 (2008).

In this paper, we use a detailed calculation of the magnetic field
produced by the neuronal currents propagating over a hippocampal CA1
pyramidal neuron placed inside a cubic MR voxel of length 1.2 mm to
estimate the Magnetic Resonance signal.

The simulation Neuron1.hoc reproduces traces similar to those in Fig.7
(top two panels) and in Fig.8a of the paper.

Under unix systems:
to compile the mod files use the command 
nrnivmodl 
and run the simulation hoc file with the command 
nrngui Neuron1.hoc

Under Windows systems:
to compile the mod files use the "mknrndll" command.
A double click on the simulation file
Neuron1.hoc 
will open the simulation window.

Questions on how to use this model
should be directed to antonio.cassara@roma1.infn.it
