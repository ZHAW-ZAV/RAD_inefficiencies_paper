# Code Repository for RAD Inefficiencies Paper
This repository contains the code developed for the paper titled *"Uncovering Hidden Inefficiencies in the Route Availability Document"*, presented at the OpenSky Symposium 2024.

## Repository Structure

The repository is structured into the two following parts:

- **preprocessing**  
  This folder contains the code to download the historical trajectories from the OpenSky Network, perprocess the flight plans provided by EUROCONTROL, and match the two to each other:
  1. *processing_m1.ipynb* and *processing_m1_2.ipynb*: Preprocess the flight plans
  2. *get_OSN_data.ipynb* and *get_OSN_data_2.ipynb*: Download the first batch of historical trajectories.
  3. *match_traj_flightplans.ipynb* and *processing_m1_2.ipynb*: Match the flight plans to the trajectories.


- **analysis**  
  Contains the Jupyter notebook *analysis.ipynb* to perform the analysis of the data according to the paper.


## Installation
This repository includes the necessary files to run the code using a Conda/Mamba environment which contains all the required dependancies in the file *environment.yml*.