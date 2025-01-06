import os
import subprocess

def install_requirements():
    # Frontend dependencies
    print("Installing frontend dependencies...")
    os.system("npm install")

    # Cloud function dependencies (if in cloud-function directory)
    if os.path.exists("cloud-function"):
        print("Installing cloud function dependencies...")
        os.chdir("cloud-function")
        os.system("npm install")
        os.chdir("..")

    # Install Google Cloud CLI if not present
    try:
        subprocess.run(["gcloud", "--version"], check=True)
    except:
        print("Installing Google Cloud SDK...")
        if os.name == 'nt':  # Windows
            os.system("powershell -Command \"(New-Object Net.WebClient).DownloadFile('https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe', 'GoogleCloudSDKInstaller.exe')\"")
            os.system("GoogleCloudSDKInstaller.exe")
        else:  # Unix-like
            os.system("curl https://sdk.cloud.google.com | bash")

if __name__ == "__main__":
    install_requirements()
    print("Setup complete! 🎉")