# my-mini-project

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
12. Run `main.py` by either clicking the play button in the top right of vscode or in the terminal with
```
python src\main.py
```
13. The program will now be usable, enjoy using it! I've included more information about the project itself below.



