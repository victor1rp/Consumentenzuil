# NS Consumentenzuil
Simple feedback app created with Tkinter from Python

## Table of Contents
* [Introduction](#Introduction)
* [Technologies](#Technologies)
* [Installing](#Installing)
* [Authorts](#Authors)

## Introduction
Many NS(Nederlandse Spoorwegen) travelers want to give their comments about NS services but nobody will listen to them. That is why we made this GUI, where travelers of the NS can send us their comments/compliments about our service. We will get a dictionary json.file of these comments where we can choose which one will we accept/reject. Then we will tweet the accepted comments and display the most recent tweets in a screen at the station hall.

## Technologies
 Project is created with:
* [Jetbrains PyCharm](https://www.jetbrains.com/products.html) version: 192.6262.63
* [Python](https://www.python.org) version: 3.7.4150

## Installing
Each Python file need to be installed in a different computer so that it can work effectively. The [*tweetlijst.json*](https://github.com/victor1rp/Consumentenzuil/blob/master/tweetlijst.json) is a JASON File where the travelers comments will be save as a dictionary with ID, The Tweet, Datum, If it is Accepted and the Rejected Datum.
To let the travelers write their comments, open the [*Invoer_Menu.py*](https://github.com/victor1rp/Consumentenzuil/blob/master/Invoer_Menu.py) in a computer in the stations
To let the NS workers approve or reject the travelers comments, open [*goedkeuren.py*](https://github.com/victor1rp/Consumentenzuil/blob/master/goedkeuren.py) in the office computer
To display the most recent Tweets, open [*scherm.py*](https://github.com/victor1rp/Consumentenzuil/blob/master/scherm.py) in a monitor at the station hall.


## Authors
* **Lucas de Jager** - *Goedkeuren*
* **Tim Kouveld** - *Scherm*
* **Victor Rios Pinto** - *Invoer Menu*
