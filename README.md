# apiPopulation
Search for a person in a database and takes as parameters his name, the name of his mother and his date of birth.

Information on the technology I used :

    Flask version 1.1.2 as framework, version of Python 3.8.5 and MySQL as database

_**mysql_configuration**_ is the file which contains the database parameters.

To use MySQL and import it into flask follow this tutorial : https://flask-mysqldb.readthedocs.io/en/latest/ 

The _**templates**_ folder contains the different views that will display the responses(display information or an error).

The **_apiPop.py_** file contains the source code of the API and the different urls of the API, it has two endpoints the first is the one that does the search in the database and the second returns the list of people.

For the database here is the structure of the table that I used in this scenario :


--
-- structure of the table `person`
--

CREATE TABLE `person` (

  `id` int(11) NOT NULL,

  `name` varchar(255) NOT NULL,

  `cni` int(11) NOT NULL,

  `birth` date NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

If you want to start the server with another address you just have to change **localhost:8080** to the new address of the server:

**app.run (host = 'localhost: 8080')**

Soon I will add its openapi description. I hope you will enjoy this API that I have developed.