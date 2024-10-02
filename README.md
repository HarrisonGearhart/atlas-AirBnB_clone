# Atlas AirBnB Clone Project
This is the first part of an AirBnB Clone project where we develop the backend of an AirBnB clone with a command line interface console. The console is similar to a Bash Shell, except the available commands were created for the purposes of an AirBnB website. The generated data is stored in a JSON File that handles serialization and deserialization.

## Table of Contents
1. [Files and Descriptions](#Files-and-Descriptions)
2. [Usage](#Usage)
3. [Flowchart](#Flowchart)

## Files and Descriptions
### console.py
The console is the entry point of the command interperter. The current commands that are supported are:
* `Exit/EOF` - exits console.
* `create` - Creates a new instance of 'BaseModel', saves it to the JSON file, then prints the id.
* `show` - Prints the string representation of an instance based on the class name and id.
* `destroy` - Deletes an instance based on the class name and id, then saves the changes to the JSON file.
* `all` - Prints all string representions of all instances based on the class name.
* `update` - Updates an instance based on the class name and id by updating or adding attributes, then saves changes to the JSON file.

### models/base_model.py
Contains the BaseModel Class that all other classes inherit from.
#### attributes
* `id` - unique user id using uuid module.
* `created_at` - The time the user was created in isoformat using datetime module.
* `updated_at` - The time any user is updated in isoformat using datetime module.
#### methods
* `def __init__(self, *args, **kwargs)` - Initializes the base model.
* `def __str__(self)` - returns the string representation of the base model.
* `def save(self)` - Updates the "updated_at" attribute with the current isoformatted datetime.
* `def to_dict(self)` - returns a dictionary containing the keys and values of an instance.

### models/amenity.py

### models/city.py

### models/place.py 

### models/review.py

### models/state.py 

### models/user.py

### models/engine/file_storage.py


## Usage
This project uses a cmd module from python. This module helps with running our program by simplifying the commands it takes. To run the program simply type python3 console.py:<br>
![image](https://github.com/user-attachments/assets/47ede6ac-24cc-4419-ad78-34b34ddb3d4e)<br>
From there you can type help to view all the command to run<br>![image](https://github.com/user-attachments/assets/eb81a80e-b8ec-456a-bd11-bf9e64ab9119)
<br>![image](https://github.com/user-attachments/assets/b3fdc70e-f139-4644-975e-4a86278dc0db)<br>



## Flowchart
<br>
