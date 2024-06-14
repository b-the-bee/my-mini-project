# CLI Café Order Management Tool with MySQL Database (Python)

# Requirements
Docker 26.1.1

Python 3.12.1

Pip 24.0
    
Requirements in requirements file (details in install instructions)
    
VSCode or similar IDE

GitBash (optional)

# Install Instructions

## Getting Started
1. Download and install Docker.
2. Download and install Python (should contain pip with this version).
4. Extract code from repo download or clone using GitBash https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository.

## Setting up the database
5. Install the required modules by doing:
```
python -m pip install -r src\requirements.txt
```
6. Next, setup the docker mysql server with:
```
cd source
docker compose up
```
7. You should now have access to the database, go to http://localhost:8080/.
8. Enter the username and password from `src\.env` with the database name as `order_mgmt`. ![alt text](readme-images\image0.png)
9. Go to SQL command. ![alt text](readme-images\image1.png)
10. Copy-paste the `src\build-db.sql` SQL commands then click execute, the database is now setup.

## Optional extra steps
11. Copy paste the example SQL files such as 
    a. `data\couriers-examples.sql `
    b. `data\items-examples.sql`
    c. `data\products-examples.sql `
into the SQL command box and execute like previously shown.

## Final Step
12. Run `run.py` by either clicking the play button in the top right of vscode or in the terminal with
```
python src\run.py
```
13. The program will now be usable on the IP generated in the terminal, go to this IP with /index to view the different tables and interact with them. 
I hope you enjoy using it! I've included more information about the project itself below.

# Running analysis
To analyse the frequency of products used, open the products frequency analysis jupyter notebook and click run on the left.

# Project reflections
How did your design go about meeting the project's requirements?
To meet the requirements, each week I created a mental plan for each week about what I would do and how to implement it.

How did you guarantee the project's requirements?
I read through my notes to see what we had done that week, and how to implement it into my project for the sake of refactoring.

If you had more time, what is one thing you would improve upon?
I would further annotate my code to explain each function and refactor for simplicity. I would also complete the API and website on the GUI branch/

What did you most enjoy implementing?
I most enjoyed implementing SQL and a Flask API into my project, this was a good challenge as I had only done a little bit of each previously and it was interesting,
I got to learn more about other programming and development languages and how to have them interact with my Python code.
