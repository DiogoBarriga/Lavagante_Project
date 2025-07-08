import os
import json

def setup_project():
    """
    Automates the setup of the Lavagante project environment.
    This includes creating necessary directories, initializing files,
    and setting up configurations.
    """
    
    # Define project structure
    directories = [
        "src",
        "docs",
        "project-artifacts",
        "reports",
        "tests",
        "tools",
        "config"
    ]
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Initialize configuration files
    config_files = {
        "project-settings.json": {},
        "team-configuration.json": {},
        "notification-rules.json": {}
    }
    
    for filename, content in config_files.items():
        with open(os.path.join("config", filename), 'w') as f:
            json.dump(content, f, indent=4)
            print(f"Initialized config file: {filename}")
    
    # Create README and CHANGELOG
    with open("README.md", 'w') as f:
        f.write("# Lavagante Project\n\nThis project aims to provide...\n")
        print("Initialized README.md")
    
    with open("CHANGELOG.md", 'w') as f:
        f.write("# Changelog\n\nAll notable changes to this project will be documented.\n")
        print("Initialized CHANGELOG.md")
    
    print("Project setup completed successfully!")

if __name__ == "__main__":
    setup_project()