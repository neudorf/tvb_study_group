# Session 2 - Imaging inputs and post-processing considerations for brain network modelling

<br>

Slide deck for this session can be found [here](.) and recording can be found [here](.).

<br>

## GOALS
Participants are able to make appropriate decisions about post-processing of structural connectomes 
- Create or check appropriateness of inputs
- Understand formatting requirements for inputs

#### Concepts covered: 
- dMRI cleaning & tractography primer
  - Overview of dMRI processing resources, tutorials, and use cases (FSL, MRtrix, TVB-UKBB)
- Pitfalls for dMRI tractography (probabilistic vs deterministic)
- Graph theory fundamentals
- Post-processing choices (normalization within subject (streamlines vs probabilities), types of thresholding, normalization across the sample)
  - Handling NaN values (removing susceptible ROIs or subjects, interpolation, inference from existing literature)
- What makes a good connectome?
  - Weights & tract length distributions
  - Graph metrics (density, degree, centrality)
  - Qualitative features
- Functional features for optimization
  - MRI FC, FCD, FCDvariance
- Required TVB inputs for each simulation output modality
  - File-naming, file content structure

<br> 

## RESOURCES

#### [CCDB](https://ccdb.alliancecan.ca/)
The Compute Canada Database is essential for setting up and configuring your Digital Research Alliance of Canada (DRA) account. You can also view and edit account, group, usage, and allocation information. You will need to create a DRA account **as soon as possible** in order to follow some of the tutorials in later sessions.



#### [DRA Wiki](https://docs.alliancecan.ca/wiki/Technical_documentation)
The Digital Research Alliance of Canada has provided a detailed technical documentation wiki that should be the "primary source for users with questions on equipment and services of the Alliance".



#### [DRA Training](https://alliancecan.ca/en/services/advanced-research-computing/technical-support/training-calendar)
The Digital Research Alliance of Canada offers free online training sessions for all skill levels, to equip researchers with the skills and knowledge to perform effective computational work and use DRA HPC resources efficiently. Content covers a wide range of topics, including data analysis, parallel computing, machine learning, and version control.


<br>

## SCRIPTS



<br>

## HOMEWORK

#### Required:
- Install TVB environment ( instructions emailed & on Slack on Friday Mar 22)
  - Wed March 27: establish a compute canada account
- Follow Justin’s github repo to set up environment
- Jupyter lab setup and interactive session

#### Optional:
- Set up a jupyter notebook to explore structural connectome and functional features 
  - Plotting
  - Checking graph metrics using BCT or other tools (give some links)
  - Apply thresholding to sample

<br>

## READINGS

