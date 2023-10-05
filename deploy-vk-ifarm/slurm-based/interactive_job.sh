#!/bin/bash
salloc -p ifarm --time=00:30:00 
srun --pty /bin/bash

scp -P 12349 z.txt jeng-yuantsai@localhost:~/