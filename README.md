# simple_crud_rest_server
Python/Flask based REST server for learning.

This REST server stores JSON objects in RAM only, it does not save to disk. It is intended for teaching/learning only. 

Functions are:

  `GET http://localhost:500/welcome` - Get a welcome page

  `GET http://localhost:5000/welcome/<name>` - Get a welcome page with your name in it.
  
  `GET http://localhost:5000/records` - Get a JSON list of records. Starts empty, so you have a create a record first to see much here.
                                    Returns a record_id for each record which must be used for update and delete functions.
  
  `GET http://localhost:5000/record/<name>` - Returns a list of records who's name matches name.
 
  `POST http://localhost:5000/record?record_name=<name>` - Create a new record named "name". Accepts any JSON object as the POST body. Content type
                                                        must be "application/json"
  
  `PUT http://localhost:5000/record/id?id=<id>` - Update the record with the id of <<id>>.
  
  `DELETE http://localhost:5000/record/id?id=<id>` - Delete the record with the id of <id>. 
  
  
Cheers!
