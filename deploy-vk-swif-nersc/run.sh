#!/bin/bash

source ../cmds_swif.sh

genwf test.json
runwf job-nersc

statwf job-nersc 1