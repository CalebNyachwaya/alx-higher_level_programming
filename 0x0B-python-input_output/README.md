## 0x0B. Python - Input/Output
*Reading and writing files are fundamental operations in programming used for tasks such as configuration files, data parsing, and data storage/retrieval. File methods, JSON encoder/decoder, and the with statement are essential concepts that provide flexibility, efficiency, and resource management in file operations, data serialization, and clean and error-free resource handling in modern programming.*
<br><br>

**Topics**
* Reading and Writing Files
* Methods of file objects
* Predefined Clean-up Actions
* JSON encoder and decoder
* **``with``** statement
<br><br>


**📄 Tasks**
|#|File|Description|
|:---|:---|:---|
|0|[0-read_file.py](./0-read_file.py)|a function that reads a text file (```UTF8```) and prints it to stdout|
|1|[1-write_file.py](./1-write_file.py)|a function that writes a string to a text file (``UTF8``) and returns the number of characters written|
|2|[2-append_write.py](./2-append_write.py)|a function that appends a string at the end of a text file (```UTF8```) and returns the number of characters added:|
|3|[3-to_json_string.py](./3-to_json_string.py)|a function that returns the JSON representation of an object (string):|
|4|[4-from_json_string.py](./4-from_json_string.py)|a function that returns an object (Python data structure) represented by a JSON string|
|5|[5-save_to_json_file.py](./5-save_to_json_file.py)|a function that writes an Object to a text file, using a JSON representation|
|6|[6-load_from_json_file.py](./6-load_from_json_file.py)| a function that creates an Object from a “JSON file”|
|7|[7-add_item.py](./7-add_item.py)|a script that adds all arguments to a Python list, and then save them to a file|
|8|[8-class_to_json.py](./8-class_to_json.py)|a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object|
|9|[9-student.py](./9-student.py)|a class Student that defines a student by public instances: ```first_name```, ```lastname```, ```age```|
|10|[10-student.py](./10-student.py)| a class Student that defines a student by: (based on 9-student.py), and includes a to_json(attrs=None) method to retrieve a dictionary representation of the Student instance, with optional attribute filtering, without importing any modules|
|11|[11-student.py](./11-student.py)|a class Student that defines a student by: (based on 10-student.py), Public method def reload_from_json(self, json): that replaces all attributes of the Student instance|
|7|[12-pascal_triangle.py](./12-pascal_triangle.py)|a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n|
