# NS Consumentenzuil
Simple feedback app created with Tkinter from Python

## Table of Contents
* [Introduction](#Introduction)
* [Technologies](#Technologies)
* [Installing](#Installing)
* [Authorts](#Authors)

## Introduction
Many NS(Nederlandse Spoorwegen) travelers want to give their feedback about NS services but nobody will listen to them. That is why we made this GUI, where travelers of the NS can send us their feedback about our services. We will get a dictionary json.file of these feedback where we can choose which one we will accept or reject. Then we will tweet the accepted feedback and display the most recent tweets on a screen in the station hall.

## Technologies
 Project is created with:
* [Jetbrains PyCharm](https://www.jetbrains.com/products.html) version: 192.6262.63
* [Python](https://www.python.org) version: 3.7.4150

## Installing
Each Python file need to be installed in a different computer so that it can work effectively. The [*tweetlijst.json*](https://github.com/victor1rp/Consumentenzuil/blob/master/tweetlijst.json) is a JASON File where the travelers' comment will be save as a dictionary with ID, The Tweet, Date, if it is Accepted or Rejected with the Rejected Date.
* To let the travelers write their comments, open the [*Invoer_Menu.py*](https://github.com/victor1rp/Consumentenzuil/blob/master/Invoer_Menu.py) in a computer in the stations
* To let the NS workers approve or reject the travelers' comment, open [*goedkeuren.py*](https://github.com/victor1rp/Consumentenzuil/blob/master/goedkeuren.py) in the office computer
* To display the most recent Tweets, open [*scherm.py*](https://github.com/victor1rp/Consumentenzuil/blob/master/scherm.py) in a monitor in the station hall.

### Preview
**Invoer_Menu.py**
![Invoer_Menu.py](https://github.com/victor1rp/Consumentenzuil/blob/master/Screenshots/Invoer_Menu_screenshot.png)

**goedkeuren.py**
![goedkeuren.py](https://github.com/victor1rp/Consumentenzuil/blob/master/Screenshots/Goedkeuren_screenshot.png)

**scherm.py**

![scherm.py](https://github.com/victor1rp/Consumentenzuil/blob/master/Screenshots/Scherm_screenshot.png)

## Authors
* **Lucas de Jager** - *Goedkeuren*
* **Tim Kouveld** - *Scherm*
* **Victor Rios Pinto** - *Invoer Menu*
