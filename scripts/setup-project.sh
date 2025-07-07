#!/bin/bash

# Setup script for the Lavagante project management environment

echo "Setting up the Lavagante project management environment..."

# Create necessary directories
mkdir -p project-artifacts/{planning,tracking,risks,quality}
mkdir -p docs/{architecture/decision-records,architecture/diagrams,project-management,processes,stakeholder-reports}
mkdir -p src/{dashboard,project-tracking,risk-management,communication}
mkdir -p tools/{kanban-board,automation,templates}
mkdir -p reports/{automated,executive}

# Initialize Git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "Initializing Git repository..."
    git init
fi

# Create a README file if it doesn't exist
if [ ! -f "README.md" ]; then
    echo "# Lavagante Project Management" > README.md
    echo "This project manages the Lavagante project lifecycle." >> README.md
fi

# Install required dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing Python dependencies..."
    pip install -r requirements.txt
fi

if [ -f "package.json" ]; then
    echo "Installing Node.js dependencies..."
    npm install
fi

echo "Project setup complete!"