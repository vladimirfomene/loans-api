# Flask Loan API for Loan Agent Collection App

## Prerequisite
In order to be able to setup our environment we will need to install the following
softwares. If you already have these installed, move to the next section. Click on each link to get instructions for installation.

* [Python 3 and Pip](https://www.python.org/downloads/)
* [Docker](https://docs.docker.com/engine/install/ubuntu/)
* [Install Pipenv](https://pypi.org/project/pipenv/)
* [Git version control system](https://git-scm.com/downloads)
* [Ngrok](https://ngrok.com/download)


## Clone The Project
Clone the project by issuing the following command in the terminal/console. Once the 
project is cloned, move to the project's directory with the next command.

```sh
# Clone project
git clone https://github.com/vladimirfomene/loans-api.git

# move to project directory
cd loans-api
```

## Install Dependencies
In order to install all the external libraries run the following command:

```sh
# Install dependencies
pipenv install
```
## Database Setup
Now that we have our application code, we need to setup our database. To make this process
simple, we are going to run our database inside a Docker container. To do that, run the following command in terminal/console.

```sh
# Setup DB on a Docker container
sudo docker run --name loan-api \
    -p 9000:5432 \
    -e POSTGRES_DB=loanapp \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -d postgres
```

With that done, if we run `sudo docker ps -a` we should see our database container running.

## Data Migration

With that in place, we need to migrate some loans and customers to our database.
To do that, head to the **src** directory and execute the following commands:

```sh
# enter project environment
pipenv shell 

# migrate customers and loans to DB
python -m migrate
```

## Run Project

To run the project, run the following commands:

```sh
# make the script executable
chmod u+x bootstrap.sh

# bootstrap Flask API
./bootstrap.sh
```

## Expose API to World

After extracting the Ngrok software, put the executable in the home directory. Notice that the Flask server is running on `localhost:5000`. To route this channel to a 
publicly accessible address execute the following command:

```sh
~/ngrok http 5000
```

This will create a tunnel and publish your public addresses to the console. Make sure to keep this addresses in mind, we will need one of them to setup the mobile app.