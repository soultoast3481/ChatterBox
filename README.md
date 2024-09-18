# ChatterBox

**WARNING**: Before hosting ChatterBox on your school's Wi-Fi, please get permission from your admin!

---

## Supported Devices
ChatterBox runs on non-Chromebook devices. It’s been tested on:
- **Windows**
- **Samsung (via Termux)**

It *should* also work on macOS, Linux, and other platforms, though they haven't been tested yet.

---

## Installation Instructions

### Desktop Installation (Windows/Mac/Linux)

#### Step 1: Install Git and Python
You’ll need Git and Python installed on your device.
- [Download Git](https://git-scm.com/downloads)
- [Download Python](https://www.python.org)

#### Step 2: Clone the Repository
1. Open your Command Line or Terminal.
2. Run the following command to clone the repository: git clone https://github.com/soultoast3481/ChatterBox.git
3. Navigate into the ChatterBox directory:

#### Step 3: Run the App
Start the app by running the following command: python app.py


---

### Android Installation (via Termux)

#### Step 1: Install Termux
1. Download **Termux** from the [Google Play Store](https://play.google.com/store/apps/details?id=com.termux).
2. Open Termux and update it: apt update && apt upgrade


#### Step 2: Install Git and Set Up Storage
1. Install Git and OpenSSH: apt install git openssh
2. Set up storage:
- You’ll need to grant storage permissions when prompted.

#### Step 3: Set Up SSH Key (Optional but Recommended)
1. Create an SSH key pair: ssh-keygen -t rsa -C "YOUR_EMAIL_ADDRESS"
2. Log into your GitHub account: ssh -T git@github.com

After successful authentication, you’re ready to use Git on your Android device!

#### Step 4: Install Python
1. Upgrade Termux packages: pkg upgrade
- Confirm prompts by pressing Enter.
2. Install Python: pkg install python


#### Step 5: Clone the Repository and Run the App
1. Clone the repository: git clone https://github.com/soultoast3481/ChatterBox.git
2. Navigate into the ChatterBox directory:
3. Start the app: python app.py

---

## Notes

- This app may be a bit rough around the edges, but it works like a charm!
- Built by a 16-year-old—so manage your expectations accordingly.
- If you’re still lost after following these steps, maybe computers aren’t your thing… just sayin’.

