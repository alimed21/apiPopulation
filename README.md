# apiPopulation
Search for a person in a database and takes as parameters his name, the name of his mother and his date of birth.
_**mysql_configuration**_ is the file which contains the database parameters

To use MySQL and import it into flask follow this tutorial : https://flask-mysqldb.readthedocs.io/en/latest/ 

The _**templates**_ folder contains the different views that will display the responses and the data.

The **_apiPop.py_** file contains the source code of the API and the different urls of the API, it has two endpoints the first is the one that does the search in the database and the second returns the list of people.
