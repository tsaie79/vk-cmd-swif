#/bin/bash

#make sure these connections work. This script should be run at ifarm.


## s: jiriaf2301, c: ifarm
export FUNCTION_PORT=1911

ssh -NfR $FUNCTION_PORT:localhost:$FUNCTION_PORT jiriaf2301

## s: ifarm, c: perlmutter
ssh -NfL $FUNCTION_PORT:localhost:$FUNCTION_PORT perlmutter


## TEST: using gateway ifarm to connect to perlmutter from jiriaf2301
### Run this at jiriaf2301
# ssh -J ifarm -NfR 42053:localhost:42053 perlmutter

## Perlmutter s: login, c: compute; run this at compute by specifing this line at command script for swif2.
### ssh -NfL 42053:localhost:42053 login01



