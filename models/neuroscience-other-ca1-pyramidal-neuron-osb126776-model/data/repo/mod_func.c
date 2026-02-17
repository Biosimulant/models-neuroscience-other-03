#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," h.mod");
fprintf(stderr," kadist.mod");
fprintf(stderr," kaprox.mod");
fprintf(stderr," kdrca1.mod");
fprintf(stderr," na3n.mod");
fprintf(stderr," naxn.mod");
fprintf(stderr, "\n");
    }
_h_reg();
_kadist_reg();
_kaprox_reg();
_kdrca1_reg();
_na3n_reg();
_naxn_reg();
}
