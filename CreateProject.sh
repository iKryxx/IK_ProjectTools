#!/bin/bash

echo "Enter the Name of your Project"
read PName
echo "do you wanna include ik_lib.h by default? [1/0]"
read IncludeLib

if [ -z "$PName" ] || [ -z "$IncludeLib" ]
then
   echo "Please enter a value."
fi

# Begin script in case all parameters are correct
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
sudo python3 $SCRIPT_DIR/CreateProject.py $PName $IncludeLib
sudo chmod -R a+rw ./
sudo chmod -R a+x ./
sudo sh Generator.sh
sudo chmod -R a+rw ./
sudo chmod -R a+x ./
sudo make
sudo chmod -R a+rw ./
sudo chmod -R a+x ./
