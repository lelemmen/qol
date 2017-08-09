#!/bin/bash

### Create a new software project template in the ${SOFTWARE_DIR}, with 
###	$1: project_name
### The template looks as follows:
### 	project_name
###		|
###	    	|_____src
###		|
###		|_____docs
###		|
###		|_____tests
###		|
###		|_____build

## Extract the variable
project_name=$1


## If the ${SOFTWARE_DIR} variable is not set, ignore this program
: ${SOFTWARE_DIR:?"is not set or empty."}


## Create the directory tree 
mkdir ${SOFTWARE_DIR}/${project_name}
mkdir ${SOFTWARE_DIR}/${project_name}/src
mkdir ${SOFTWARE_DIR}/${project_name}/docs
mkdir ${SOFTWARE_DIR}/${project_name}/tests
mkdir ${SOFTWARE_DIR}/${project_name}/build

