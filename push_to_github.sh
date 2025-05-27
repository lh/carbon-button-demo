#!/bin/bash

# Replace YOUR_USERNAME with your GitHub username
# This script assumes you've already created the repository on GitHub

echo "Please enter your GitHub username:"
read username

echo "Please enter your repository name (default: streamlit-carbon-button):"
read repo_name
repo_name=${repo_name:-streamlit-carbon-button}

# Add the remote origin
git remote add origin https://github.com/$username/$repo_name.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main

echo "✅ Repository pushed to GitHub!"
echo "🔗 View at: https://github.com/$username/$repo_name"