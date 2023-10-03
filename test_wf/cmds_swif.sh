#!/bin/bash

# show wfs 
alias lswf="swif2 list"

# delete wf
function delwf { swif2 cancel $1 -delete; }