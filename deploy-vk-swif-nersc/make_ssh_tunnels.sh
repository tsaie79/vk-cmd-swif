#/bin/bash

#make sure these connections work. This script should be run at ifarm.


## s: jiriaf2301, c: ifarm
ssh -NfL 12347:localhost:35393 jiriaf2302

## s: ifarm, c: perlmutter
ssh -NfR 35393:localhost:12347 perlmutter 
### after this, one should see "Login connection to host x3113c0s11b0n0"
### One can run "ssh x3113c0s11b0n0" at NERSC then know what the login node is.



# Run at NERSC login
## ssh -J tsai@scilogin2.jlab.org -ANfL 35393:localhost:35393 jiriaf2301