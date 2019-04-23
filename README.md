## INTRODUCTION

A basic Result Viewing Application built in Django with PostgreSQL Database designed to help the beginners struggling to get a head start in Django.
Stakeholders are :
1. An Admin : The superuser adding student information records and their marks.
2. Student/End User: A student can enter their Roll number and Date of Birth to view their result

## INSTALLATIONS
> Recommended : Download Pycharm IDE for better understanding and setting up your django configs

Run ```$ sudo apt-get update ```

Installing PostgreSQL and its dependencies

``` $ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib ```

Start postgresql and check if installed properly

``` $ service postgresql start ``` 

Login to postgres shell as root user and enter your system's password at the next prompt

``` $ sudo -u postgres psql postgres ```

Create a Superuser for your database by running

``` $ CREATE USER <username> WITH SUPERUSER PASSWORD <password>; ```

Create your database and connect to it. 

``` $ CREATE DATABASE <db_name> ```

``` $ \c <db_name> ```

You can also login to postgres shell by running
``` $ psql -d <db_name> -U <username> ```


## Getting Started

Clone the repository in your workspace. This will setup the project in your system.
``` $ git clone https://github.com/tavleen13/ViewYourResult.git ```



