📁 ShareYaar — Secure File Sharing App

![image](https://github.com/user-attachments/assets/28f59d14-2747-496f-9a3a-61c8c853a1ff)

ShareYaar is a secure file sharing web app. It lets you upload files, encrypt them in your browser using a password, and share a safe link with others to download and decrypt the file — without the server ever seeing your actual data.

📌 What It Does (Overview)
ShareYaar is a web-based application.

All encryption and decryption happens in the user's browser (client-side), not on the server.

This makes it a "zero-knowledge" app — the server never knows what's in your file.

🔑 Key Features
Client-Side AES Encryption
Files are encrypted in your browser before being uploaded. You choose the password.

Decryption by Recipient
The person receiving the file must enter the same password to decrypt it in their browser.

Clean User Interface
A simple, modern, and mobile-friendly design.

Secure Download Link
Generates a unique link for downloading the file.

File Previews
Shows the file name and size before uploading.

Easy Deletion
You can delete your uploaded file when you're done.

⚙️ How It Works (Step-by-Step)
Select File + Enter Password
The user picks a file and enters a password on the homepage.
![image](https://github.com/user-attachments/assets/28f59d14-2747-496f-9a3a-61c8c853a1ff)

Encrypt in Browser
JavaScript encrypts the file in the browser using AES encryption.

Upload Encrypted File
Only the encrypted file is sent to the Flask server.
![image](https://github.com/user-attachments/assets/a8f7647f-2908-4cc2-ad0c-9d44203fea7b)

Store on Server
The encrypted file is saved in the uploads/ folder.

Share Link
A special link is generated for the recipient to download the file.

Download + Decrypt
The recipient opens the link, enters the password, and the browser decrypts the file and downloads it.
![image](https://github.com/user-attachments/assets/ed537b3e-fcf7-42bd-ae75-ac7f6ef84100)

🛠️ Tech Stack
Backend
Python

Flask – Web server and routes

Werkzeug – For secure file handling

Frontend
HTML5

Tailwind CSS – Styling

JavaScript

Encryption
CryptoJS – For AES encryption in the browser

🚀 How to Run It (Local Setup)
1. Prerequisites
Install Python 3.6+ and pip

2. Installation
bash
Copy
Edit
git clone https://github.com/hussain9347/Share-yaar.git
cd Share-yaar
pip install Flask
3. Run the App
bash
Copy
Edit
cd Backend
python app.py
Open your browser and go to: http://127.0.0.1:5000

📁 Project Folder Structure
pgsql
Copy
Edit
Share-yaar/
│
├── Backend/
│   └── app.py           # Flask backend server
│
├── uploads/             # Stores encrypted files
├── index.html           # Upload + encrypt page
├── download.html        # Download + decrypt page
└── README.md            # Project description
