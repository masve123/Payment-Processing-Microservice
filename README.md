# Payment-Processing-Microservice
This is a microservice using the API gateway architecture, implementing a payment processing API.


Some notes for the microservices:

## user-service
- This service is responsible for user authentication and authorization.
- Represents a person or entity who can log into your system. They have credentials like a
username and password, and perhaps personal information like a name, contact information, etc. In your system, a User may have the ability to create and manage multiple accounts.


## account-service
- This service is responsible for managing accounts.
- Represents a bank account. An account has a balance, and can be debited and credited. An account can be associated with a User.

- An account represents a financial entity that is owned by a User. The Account keeps track of financial information like balance, transactions, etc. An Account does not have login credentials because it's not something that logs in. It's something that is owned by a User who logs in.


- The separation also provides more flexibility. For example, in the future, if you want to support multiple accounts per user (like savings and checking accounts), or joint accounts (where multiple users own a single account), having separate User and Account models will make these features much easier to implement. Also, by separating the concerns, you can change or refactor one part of your system (like Accounts) without affecting the rest (like Users).


Microservice Application with API Gateway
## Overview
This project demonstrates the design and implementation of a microservice application using the API gateway architecture. Utilizing Kong as our API gateway, this application supports advanced non-functional properties like load balancing, fault tolerance, and security. The goal is to showcase the advantages of the API gateway approach in comparison to traditional microservice architectures without gateway intervention.

## Requirements
- Docker and Docker Compose
- Kong
- Microservices (user_service, payment_service, and account_service)

## Setup
- Clone the Repository
- Navigate to the Project Directory
This directory contains the microservices and necessary configurations.
- Start Kong
If using Docker, ensure Docker is running, then:
```
docker-compose up -d
```
This will start Kong and its database

- Start the Microservices
Each microservvice can be started using the respective command inside its directory:
```
cd user_service && npm start
```
Do the same for 'payment_service' and 'account_service'

- Set up Kong and Load Balancing:
This project demonstrates load balancing across multiple instances of each microservice. Ensure you have registered each instance as described in the setup steps.

# Testing
## Load Balancing
For each service, use a tool like curl or any HTTP client to send multiple requests:
```
curl http://api.user.com
```
If load balancing is set up correctly, these requests will be distributed among the different instances of user_service.
Repeat the process for payment_service and account_service

## Security
Security for each service is added through Kong's plugins. Make sure to follow the security addition steps before testing.

Send a request without an API key:
```
curl http://api.user.com
```
This should return an unauthorized error

Send a request with an API key (You mustreplace [YOUR_API_KEY] with the actual API key):)
```
curl http://api.user.com --header "apikey: [YOUR_API_KEY]"
```
The request should go through if the API key is correct.

## Fault Tolerance:
Kill one of the instances of a microservice, and send requests to the respective endpoint. Thanks to Kong's health checks, the dead instance will be marked as such, and traffic will be sent to the healthy instances, ensuring continuous availability.

## Conclusion:
This project effectively demonstrates the benefits of using an API gateway in a microservice application. With Kong, we were able to easily add load balancing, fault tolerance, and security, showcasing the advantages of this approach compared to traditional architectures.