# peloton
Data challenge

All the original data and intermediate data are in the data/ directory, including the python script to generate the analytics data.

The A/B tests results, details and discussions on the effect of push notifications are in AB_tests.ipynb file.

The A/A tests results, details and discussions on the effect of Holiday season are in AA_tests.ipynb file. 

The results of the analysis are summarized in a presentation [here](https://docs.google.com/presentation/d/1SyGZHM0E4hTYB1GK_egMKx0PQWL1S0OaHjIgoQVm67Q/edit?usp=sharing).

If you can not open it, here is the full link:

https://docs.google.com/presentation/d/1SyGZHM0E4hTYB1GK_egMKx0PQWL1S0OaHjIgoQVm67Q/edit?usp=sharing


All the python depedencies are in the requirements.txt file. 

The analysis are make with docker container jupyter/datascience-notebook.

To run the docker image, do `docker run -it --rm -v "$PWD":/home/jovyan/work --shm-size=1024m -p 8888:8888 jupyter/datascience-notebook`.