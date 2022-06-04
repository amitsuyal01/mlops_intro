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
    - the makefile lists all the processes that needs to be run for this project, these are
        - install: use 'pymake install' in cmd to install all the requirements
        - lint: for checking any warning/errors in the python file, use 'pymake lint' command in cmd
        - test: for testing the calculator, use 'pymake test' to test the file
        - format: use 'pymake format' to forat the python files
        - lastly, all these processes can be run at one using 'pymake all' in cmd 
5. A 'calculator.py' file is our main application
     - the file 'calculator.py' is a simple application that can add two numbers
     - this python file can be used through command line interface
          - use 'python calculator.py number1 number2'
          - or 'python calculator.py -h' for help
7. Another file 'test_calculator.py' is used for performing all the necessary tests
     - the 'test_calculator.py' file is used for testing the 'calculator.py' file using the pytest module




