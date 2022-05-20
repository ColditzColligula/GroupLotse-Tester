<p align="center">
  
<a href="https://grouplotse.com">
         <img alt="Grouplotse" src="https://grouplotse.com/wp-content/uploads/2021/02/gl_logo_runde-ecken-219x36-1.png">
      </a>
</p>


# GroupLotse Tester

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ColditzColligula/GroupLotse-Tester?style=plastic)
![GitHub all releases](https://img.shields.io/github/downloads/ColditzColligula/GroupLotse-Tester/total)
![GitHub](https://img.shields.io/github/license/ColditzColligula/GroupLotse-Tester)

A small GUI Application to test your **GroupLotse** Interfaces

GroupLotse currently supports **Webhook (POST/GET), MQTT, SMS and E-Mail**. This Application will allow you to **test and send messages/images** to GroupLotse's Webhook and MQTT Interfaces. 

Feel free to import the **GroupLotse class from "GroupLotse.py"** into your personal projects. That way you can send messages and images to your Grouplotse from within your application.

<p align="center">
 <img src="https://user-images.githubusercontent.com/79027579/169392145-97ffabc4-20cf-490e-a373-54fd57244c1b.png">
</p>


GroupLotse is a Virtual Assistant for Telegram, Slack and Microsoft Teams.


<a href="https://grouplotse.com/en/grouplotse-for-telegram/" target="_blank">
         <img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">
      </a>

                               
<a href="https://grouplotse.com/en/grouplotse-for-slack/" target="_blank">
         <img alt="Slack" src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white">
      </a>


<a href="https://grouplotse.com/en/grouplotse-for-microsoft-teams/" target="_blank">
  <img alt="Microsoft Teams" src="https://img.shields.io/badge/Microsoft_Teams-6264A7?style=for-the-badge&logo=microsoft-teams&logoColor=white">
      </a>





Learn more about GroupLotse on our [official Website](https://grouplotse.com) and follow us on <a href="https://www.youtube.com/c/GroupLotse/" target="_blank">
  <img alt="Youtube @ GroupLotse" src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white">
      </a> and <a href="https://www.linkedin.com/company/grouplotse/" target="_blank"> <img alt="Linkedin @ Grouplotse" src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white"> </a>






Watch our short Youtube video to find out how **GroupLotse can help you overcome the daily challenges of communicating responsibilities!**

<a href="https://www.youtube.com/watch?v=6mAiQxft26Y" target="_blank">
  <img alt="Youtube @ GroupLotse" src="https://user-images.githubusercontent.com/79027579/168651131-e5fc6b0e-85da-448c-b52f-78736a31d811.png">
      </a>



## Table of contents
* [General info](#general-info)
* [Windows Executable](#windows-executable)
* [Setup and Usage](#setup-and-Usage)
* [Planned Features](#planned-features)
* [Known Bugs](#known-bugs)

## General info

**What is the purpose of this Application?**

The "GroupLotse Interface Tester" was made to quickly check if newly created GroupLotse Interfaces are working. The Application can also be used to send and broadcast Messages to Groups and Channels using your GroupLotse by directly sending a Message to him through one of the available Interfaces.

**What is GroupLotse?**

GroupLotse is a virtual assistant that enables quick clarification of responsibilities and precise device control. Your team can be actively involved in all decision-making processes. Furthermore, it is also possible to fully automate all processes.


Your team can interact with GroupLotse via the common communication and collaboration platforms Slack, Microsoft Teams and Telegram. This ensures that GroupLotse can be productively integrated into workflows and that all relevant information is available at all times. To achieve this, GroupLotse is simply integrated into your existing channels and chat groups.

**Which Messengers can I use with GroupLotse?**

Currently, you can use GroupLotse in Microsoft Teams, Slack and Telegram.

It is also possible to use GroupLotse in several messengers at the same time. However, this is not possible with the free GroupLotse plan.

**What plans are available?**

In addition to our free plan, there are three other paid plans. These differ in the maximum number of GroupLotse, interfaces and messages per day, as well as in additional features such as call notifications and telephone support. To check available plans, follow [this link!](https://grouplotse.com/en/pricing/)

## Windows Executable

You can download a 7zip-File containing all necessary files to run this application [here.](https://www.dropbox.com/s/ojyq7ugeojhyw5m/GroupLotse%20Interface%20Tester.7z?raw=1) After you have extracted the Archive, just run the Shortcut "GroupLotse Interface Tester".

## Setup and Usage

The application works on Windows and Unix/MacOS.

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

You can either [download the prepared 7zip-file](https://www.dropbox.com/s/ojyq7ugeojhyw5m/GroupLotse%20Interface%20Tester.7z?raw=1) containing all necessary files to run and execute the program **or** [download the Github Repository](https://github.com/ColditzColligula/GroupLotse-Tester/archive/refs/heads/main.zip) and open the "main.py" file with Python3.
If you're **not** using the bundled .exe file, make sure to install the required libraries.

You can do this easily by utilizing the "requirements.txt" by opening a CMD/Shell and typing "pip install -r requirements.txt" (You must be in the same directory where the file is located)

Required:
- [PySimpleGUI](https://github.com/PySimpleGUI)
- [paho-mqtt](https://pypi.org/project/paho-mqtt/)
- [requests](https://docs.python-requests.org/en/latest/)


![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) / ![Mac OS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)

[Download the Github Repository](https://github.com/ColditzColligula/GroupLotse-Tester/archive/refs/heads/main.zip) and start "main.py" with Python3.

You can do this by opening a Shell, navigating to the directory that contains "main.py" and typing "python3 main.py".

make sure to install the required libraries above! You can do this easily by utilizing the "requirements.txt" by opening a Terminal/Shell and typing "pip install -r requirements.txt" (You must be in the same directory where the file is located)

## Planned Features

The GroupLotse Interface Tester is, at this stage, considered Feature complete.

## Known Bugs

- Trying to send a message to an unreachable/invalid interface will not throw an error.
