# ChatterBox

**WARNING**: Before hosting ChatterBox on your school's Wi-Fi, please ask for permission from your admin!

## Supported Devices
ChatterBox must be run on a non-Chromebook device. It's been tested on:
- **Windows**
- **Samsung (via Termux)**

It *should* work on Mac, Linux, and other platforms, but we haven’t tested them yet!

## Installation Instructions

### Step 1: Install Git and Python
You'll need Git and Python installed on your device.
- Download Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)
- Download Python: [https://www.python.org](https://www.python.org)

### Step 2: Clone the Repository
Open up your Command Line and run the following commands: git clone https://github.com/soultoast3481/ChatterBox.git 

then cd ChatterBox

### Step 3: Run the App
In the Command Line, start the app by typing: Python app.py

INSTALLATION ON ANDROID

begin by installing termux from the play store

then open the app and update it apt update && apt upgrade

then install git with apt install git openssh

next setup storage with termux-setup-storage
click allow

We need to create the key-pair of SSH using the command:

ssh-keygen -t rsa -C "YOUR_EMAIL_ADDRESS"


Log into your GitHub account using the command:

ssh -T git@github.com
After successful authentication, you can start using Git on your Android device. You can create, pull, push the repositories. This is the easy way to use Git on your smartphone and it is a safe way because the Termux app is installed using Google play store.

after installation of git install Python

type in pkg upgrade
When prompted for Y/N confirmations, tap Enter to go with the defaults

Then, enter the following command to install Python:

pkg install python

then continue the steps from the default installation instructions

## Notes

- This app may be a bit rough around the edges, but it 100% works!
- Built by a 16-year-old—manage your expectations accordingly.
- If these steps are unclear, and you’re still lost, maybe computers aren’t your thing... just sayin’.