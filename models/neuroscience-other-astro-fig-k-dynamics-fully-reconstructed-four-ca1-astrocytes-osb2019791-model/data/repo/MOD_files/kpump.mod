TITLE kpump

NEURON {
	SUFFIX KNaTrans
	USEION k READ  ki, ko WRITE ik
    USEION na READ  nai	WRITE nai
	 RANGE ik, Kp, Krest, imax, ModulK, ik_Trans
    :RANGE Krest, imax	
}
UNITS {
    (molar) = (1/liter)
    (mV) =	(millivolt)    
    (mM) =	(millimolar)
	(mA) = (milliamp)
	
}

PARAMETER {
	Kp = 0.1 (mA/cm2)
	Krest = 110 (mM)
	imax = 0.1 (mA/cm2)
	ModulK = 7.3

	
	
}

ASSIGNED {
	
	ik (mA/cm2)
	ik_Trans (mA/cm2)
    ki       (mM)	
	ko       (mM)
	nai      (mM) 
}

BREAKPOINT {
    : nai=10
	: ik = Kp*(ki/Krest - 1)
	: ik= imax*(1/(1 + 7.3/ko)^2)*(1/(1 + 10/nai)^3) *(ki/Krest - 1)
	ik_Trans= imax*(1/(1 + ModulK/ko)^2)*(1/(1 + 10/nai)^3)
	ik = ik_Trans
	
	

}

