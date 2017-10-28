#!/bin/bash
#SBATCH -N 1
#SBATCH -p RM-shared
#SBATCH -t 2:00:00
#SBATCH --ntasks-per-node=4

# Add any commands to be ran at the beginning of the indiviual run scripts here:
projectdir=$PWD
scratchdir=${projectdir//project/scratch}/run

mkdir -p $scratchdir
cp -rT $projectdir $scratchdir

cd $scratchdir
/home/pmerz/bin/gromacs-2016/bin/gmx grompp -f system.mdp -p system.top -c start.gro -o system.tpr -maxwarn 5
/home/pmerz/bin/gromacs-2016/bin/gmx mdrun -nt 4 -s system.tpr -deffnm system
# Add any commands to be ran at the end of the indiviual run scripts here:
cp -r $scratchdir/run $projectdir/
cd $projectdir
