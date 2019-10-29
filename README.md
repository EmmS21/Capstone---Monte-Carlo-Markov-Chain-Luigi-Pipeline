# Springboard-Capstones
 
The purpose of this capstone is to build a pipeline for a Monte Carlo Markov Chain model. The initial objective was to use this model to gain a deeper understanding of conversion rates from users who land on a given signup page and go through the signup process- moving through different states in the signup process. 

The states are defined as; i.) session - landing on the specified signup landing page
ii.) lead - landing on a page indicating progression from session to filling in details in the first part of the signup process
iii.) opportunity - landing on pages indicating progression from lead to opportunity. However, an assumption was made that pages containing the string continue, which indicates that the user may have closed the signup process and continued the signup process at a later stage, is an indicator that the user in question has progressed from lead to opportunity.
iv.) complete - landing on pages that appear to indicate that the user has completed the signup process.

This is uni-directional process as users can only move forward through each state sequentially. 

For the sake of simplicity and getting results that where more feasible given constraints in context, I deviated from the initial objective of building an attribution model to building a model that would give insights regarding different conversion rates based on filters ranging from time of day to day of week and device used when signup commenced.

These are the files and folders included in this repository

##### AttributionModel
- contains all files and links to data required for this model

##### Capstone 
- separate_csv.py - separating the data source into 4 csv files
- state_to_state_transitions - returning the sequence of marketing channels engaged by the user before signup was completed
- state_to_state_transitions2 - determining whether or not a user moved from one state to another
- gaussian_kdefit - estimating probability distribution for each transition
- get_samples - getting samples from output created by gaussian_kdefit task
- state_to_state_machine - generating simulations based on probabilities in samples output
- parent_wrapper - concatenating simulations into a single file and running the entire pipeline

##### Data
1. DataFile - contains a single file 'attributionfile' with a Google Drive link to the data file used in this model
2. ModelData - contains 3 folders; i.) fullmcsims (simulations created), ii.) original (simulations with no filters), iii.) all pickle files created through model. This is also the destination folder of all output created by the model save for the simulations
3. Sims - empty destination folder of all simulations generated 


- Notebooks - contains 2 files; i.) comparesims.ipynb - comparing simulation conversion rates to conversion rates observed in original simulation (with no filters), ii.) Samplesvactuals.ipynb - comparing sample transitions to population data
- Data Extraction - contains sqlextract.sql - the sql script used to extract the data from the source
- Project Reports - contains i.) Project Report.pdf, this is a full report on the project with a more indepth explanation of each task, ii.) Capstone 1 Insights Report, this is a presentation of the business insights extracted from the simulations carried out

