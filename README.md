# Soccer top teams
_Udacity's Item Catalog Project_
A simple web application that provides a list of items within a variety of categories and integrate third party user authentication. Authenticated users have the ability to add, edit, and delete items.

## prerequisites
> python 2.7
> sqlite
 ## installation
 1. clone the fullstack-nanodegree-vm repository.from [here](https://github.com/udacity/fullstack-nanodegree-vm)
 2. replace catalog folder contents with contents of this repository
 
 ## add your favourite leagues [optional]
 1. remove the existing database file *teams.db*
 2. run *database_setup.py* file to generate new database
 3. run *fill_database.py* file and follow instructions
 
 
 ## run the application
 run vagrant and login 
 ```
 vagrant up
 vagrant ssh
 cd /vagrant/catalog
 ```
 then run the application
 `python application.py`
 lastly open **http://localhost:8000** in your browser
 **_enjoy_**