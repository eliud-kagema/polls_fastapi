# The Polls API will have the following endpoints

1. An API to create poll question
2. API to list all poll questions
3. API to get question detail
4. API to edit poll question
5. API to delete poll question
6. API to create choice for a particular poll question
7. API to update votes for a particular question


### The endpoints

1. Create question - POST http://127.0.0.1:8000/questions/
2. List all questions - GET http://127.0.0.1:8000/questions/
3. Retrieve a particular question - GET http://127.0.0.1:8000/questions/{qid}
4. Edit a particular question - PUT http://127.0.0.1:8000/questions/{qid}
5. Delete a particular question - DELETE http://127.0.0.1:8000/questions/{qid}
6. Create choice for a particular poll question - POST http://127.0.0.1:8000/questions/{qid}/choice
7. Update votes for a particular question - PUT http://127.0.0.1:8000/choices/{choice_id}/vote