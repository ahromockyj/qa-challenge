# Techstars QA Hiring Challenge

## Instructions:
Attached is project code that uses flask and python to create and run a docker container that exposes an api to perform some simple math. Using this code, please write automated test cases using Python 3.x and any testing packages of your choosing to thoroughly test the compute endpoint. Additionally, perform manual testing on the API and document any bugs discovered during testing.

## Running:
To run the code and expose the flask server at `localhost:5000`, run the command `docker-compose up`

## Expected API Functionality:
The API should receive a two number operation through the url and calculate and return status code `200` and the result, rounded to the nearest whole integer. If the inputs are invalid or cannot be computed, status code `400` and the string “INVALID” is expected to be returned.

The API endpoint for computing is available at `GET /compute/<number><operator><number>`

**Operators:**
| OPERATOR | ACTION   |
| :------: | :------- |
| +        | Add      |
| -        | Subtract |
| *        | Multiply |
| ~        | Divide   |

&nbsp;  

**Here are some examples of expected inputs and responses:**
| INPUT             | EXPECTED RESULT |
| :---------------- | :-------------- |
| GET /compute/2+2  | 4               |
| GET /compute/2+-2 | 0               |
| GET /compute/2-3  | -1              |
| GET /compute/7*3  | 21              |
| GET /compute/7~3  | 2               |
| GET /compute/2    | INVALID         |
| GET /compute/2+h  | INVALID         |
