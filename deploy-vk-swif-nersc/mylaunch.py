import subprocess
import math
import glob
import sys
import os


PROJECT = "m3792"
timelimit = "00:01:00"
qos = "debug"
NODETYPE = "cpu"
WORKFLOW = "test-nersc"
JOB_STR = "job1"


# SLURM options
SBATCH  = ['-sbatch']
SBATCH += [f'--account={PROJECT}']
# SBATCH += ['--volume="/global/project/projectdirs/%s/launch:/launch"' % PROJECT]
# SBATCH += ['--image=%s' % IMAGE]
SBATCH += ['-t', timelimit]
SBATCH += ['-N', '1']
# SBATCH += ['--tasks-per-node=1']
# SBATCH += ['--cpus-per-task=64']
SBATCH += ['-q', qos]
SBATCH += ['-C', NODETYPE]
SBATCH += ['-o', 'job-%j.out']
SBATCH += ['-e', 'job-%j.err']

nersc_project_dir = "/global/homes/j/jlabtsai/swif"



def create_wf(new_site=False):
    # Create workflow
    cmd =  ['swif2', 'create', '-workflow', WORKFLOW]
    
    # check site info: swif2 show-sites
    if new_site:
        cmd += ['-site-name', "perlmutter",
                "-site-path", "/global/homes/j/jlabtsai/swif", 
                "-site-globus-endpoint", "63e2f6ac-a46f-4853-b518-e6e33859e860",
                "-site-login-user", "jlabtsai",
                "-site-login-host", "perlmutter",
                ]
    else:
        cmd += ['-site', 'perlmutter']

    print(f'create_wf cmd = {cmd}')
    subprocess.call(cmd)


def add_job():
# Command for job to run
    CMD = [f"{nersc_project_dir}/cmd.sh"]
    # CMD = [f'echo "Hello World" > {nersc_project_dir}/hello.txt']


    # Make swif2 command
    SWIF2_CMD  = ['swif2']
    SWIF2_CMD += ['add-job']
    SWIF2_CMD += ['-workflow', WORKFLOW]
    SWIF2_CMD += ['-name', JOB_STR]
    
    
    # Add SBATCH options and actual command to run to swif2 command		
    SWIF2_CMD += SBATCH + ['::'] + CMD
    print(f'add_job cmd = {SWIF2_CMD}')
    subprocess.call(SWIF2_CMD)



def run_wf():
    # Run workflow
    cmd =  ['swif2', 'run', '-workflow', WORKFLOW]
    print(f'run_wf cmd = {cmd}')
    subprocess.call(cmd)


if __name__ == "__main__":

    create_wf()
    add_job()
    run_wf()