# PopulationDesitySimulator

A simulator for Population Density for humans in an area.

## Intitution behind:
a.  Firstly a dataset is complied for the France comparing the size of cites and population.

b.  Given the definition of tau, initial  impression for French cites tend to have 0.65 value of tau, thus many people tend to live in big cities.

c.  A table is constructed following the intution between tau vs % no of big cities for different values of tau. 

d.  Another table is construction on same intution between tau vs % no of people living in big cities. 

e.  Curve fitting is done to obtain two equations:
1.  ratio of no of big cities =  0.3283081*e^(-(tau - 0.5552639)^2/(2*0.2253474^2))
2. ratio of people living in big cities = 0.9633827*e^(-(tau - 0.9441574)^2/(2*0.4118766^2))

f. Thus, for 0<tau0.5 people favour small cities over big cites and 0.5<tau<1 people favour big cites to live in.

g. After this, the whole simulator was constructed.
 
## Pre-installation steps:
- Make sure you have python 3+ installed on your computer.
- Make sure you have pip3 package installed on your computer.
- Make sure you clone this package to your computer.

## Install requirements: 
In your terminal/command-line go to the project folder and execute the command below:
```bash
pip3 install -r InstallMe.txt 
```
## How to run the project:
Please run the following command in your terminal and read carefully to proceed thereafter.
```bash
python main.py
```
Your results dataframes are stored in the folder output.
