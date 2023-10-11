# Introduction
How to run vk-cmd in remote compute sites with workflow tool SWIF2. To check the flags of SWIF2, please refer to [SWIF2](https://scicomp.jlab.org/cli/swif.html)


# Setup SWIF2 for the remote compute site, Perlmutter at NERSC
1. [Set up globus endpoint for Perlmutter at NERSC](https://davidljlab.wordpress.com/2018/07/18/swif2-testing/)

2. [Hall-D](https://halldweb.jlab.org/wiki/index.php/HOWTO_Execute_a_Launch_using_NERSC)

3. No password login to perlmutter is required. Please refer to use the scrips in `deploy-vk-swif-nersc/no-password-nersc` to set up the no password login.

4. To run workflows at NERSC, please refer to the python script in `deploy-vk-swif-nersc/mylaunch.py`.
    - Create site for SWIF2 is important. Please refer to the script `deploy-vk-swif-nersc/create-site.py` to create the site. 