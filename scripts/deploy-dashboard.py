import os
import subprocess

def deploy_dashboard():
    """
    Deploys the metrics dashboard for the Lavagante project.
    This function builds the dashboard and deploys it to the specified environment.
    """
    try:
        # Step 1: Build the dashboard
        print("Building the dashboard...")
        build_command = ["python", "src/dashboard/visualization.py"]
        subprocess.run(build_command, check=True)

        # Step 2: Deploy the dashboard
        print("Deploying the dashboard...")
        deploy_command = ["docker-compose", "up", "-d"]
        subprocess.run(deploy_command, check=True)

        print("✅ Dashboard deployed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during deployment: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    deploy_dashboard()