# mlops_intro
## Introduces to best practices in mlops at a beginner level

###### The steps we will follow in this tutorial

1. Creating the requirement.txt file
    
   - The requirements.txt file lists all the nessary libraries that are important for the project
   - Before working on a project it is advised to make a seperate working environment using the below commands
       - virtualenv -p python3 mytest
       - .\mytest\Scripts\activate (to activate the environment in windows)
   - once the environment is created and activates we can download all the necessary libraries using the command
       - pip install -r requirements.txt
   - An additonal point that can be noted here is that we do not want to upload the installed virtual environment in github repo 
       - to do so, write \mytest in the .gitignore file 
  
3. Creating a makefile
4. A py file that will be our source code
5. Another Py file for testing

check
