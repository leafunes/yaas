# YAAS - Yet another account system

YAAS is a simple tool that helps you to log every credit and debit in your account.

## Running YAAS
YAAS have two individual proyects:
- api: backend. It handles all business logic and stores the transactions.
- app: frontend. It shows the account status and all the transaction history in a user friendly manner.

### Runing api
Prerequisites:
- python3
- pip
- pipenv

To run the YAAS api you have to:
1. cd api
2. pipenv install
3. pipenv run test
4. pipenv run dev

This last command will run the api in port 5000


### Running app

Prerequisites:
- node 14

To run the YAAS app you have to:
1. run the api in a different shell
2. cd app
3. npm install
4. npm run

This last command will run (and open a browser tab) the app in port 3000

### TODOs:
- Proper testing in frontend, with jest and react testing library
- Proper error handling in the frontend. It only follows the "happy path" nowadays
- Custom hooks in frontend. This can be an opportunity to parametrize the urls of the api
- Dockerize the entire proyect
- Implementing a real database engine (like mongo)
- Parametrize the services in the api to have a different database engine depending if its running in local or production
- Grow YAAS as a multiuser system