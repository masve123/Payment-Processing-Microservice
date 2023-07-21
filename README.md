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