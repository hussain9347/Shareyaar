**ShareYaar**

Secure, Encrypted File Sharing with Client-Side AES Encryption
Note: You should replace the link above with a real screenshot of your running application.

Table of Contents
Overview

Key Features

How It Works

Tech Stack

Getting Started

Prerequisites

Installation

Usage

Project Structure

Overview
ShareYaar is a web-based, secure file transfer application that allows users to upload and share files with end-to-end encryption. The core principle of this project is zero-knowledge hosting, meaning the server has no knowledge of the contents of the files being stored, as all encryption and decryption happens directly in the user's browser (client-side).

This project is an excellent demonstration of combining a Python Flask backend with modern, interactive frontend technologies to create a secure and user-friendly application.

Key Features
🔐 Client-Side AES Encryption: Files are encrypted in the browser with a user-provided password before being uploaded. The server only ever stores the encrypted data.

🙋‍♂️ Recipient Decryption: Files are decrypted in the recipient's browser using the same password, ensuring the original data is never exposed on the server.

🚀 Simple User Interface: A clean, modern, and responsive UI for a seamless user experience.

🔗 Secure Shareable Links: Generate unique links for recipients to access a download page.

🗑️ File Management: Easily delete uploaded files from the server.

👁️ File Previews: See the name and size of a file before initiating the encryption and upload process.

How It Works
Select & Password-Protect: The user selects a file and provides a password on the main page.

Encrypt in Browser: The browser's JavaScript reads the file, encrypts its content using AES with the provided password, and appends .enc to the filename.

Upload Encrypted Data: The encrypted file is sent to the Flask backend.

Store on Server: The Flask server saves the encrypted file to the uploads/ directory without ever reading its contents.

Share Link: The user copies the unique /share link for the encrypted file.

Decrypt & Download: The recipient opens the link, is prompted for the password, and the browser's JavaScript fetches the encrypted file, decrypts it, and initiates the download of the original file.

Tech Stack
Backend:

Python

Flask (for web server and routing)

Werkzeug (for secure filenames)

Frontend:

HTML5

Tailwind CSS (for styling)

JavaScript

Encryption:

CryptoJS (for client-side AES encryption/decryption)

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
You need to have Python and pip installed on your system.

Python (3.6 or higher)

Installation
Clone the repository:

git clone [(https://github.com/hussain9347/Share-yaar.git)
](https://github.com/hussain9347/Shareyaar)
Navigate to the project directory:

cd Share-yaar

Install the required Python packages:

pip install Flask

Usage
Navigate into the Backend directory:

cd Backend

Run the Flask application:

python app.py

Open your web browser and go to:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

The application should now be running locally.

Project Structure
Share-yaar/
├── Backend/
│   └── app.py           # The Flask backend server
├── uploads/             # Directory for stored encrypted files (auto-generated)
├── index.html           # Main page for uploading and encrypting
├── download.html        # Page for recipients to download and decrypt
└── README.md            # This file
