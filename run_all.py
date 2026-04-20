import subprocess
import os
import time
import sys
import webbrowser

# Paths to the project directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_A_DIR = os.path.join(BASE_DIR, "ProjectA")
PROJECT_B_DIR = os.path.join(BASE_DIR, "ProjectB")
PROJECT_C_DIR = os.path.join(BASE_DIR, "ProjectC")
PROJECT_D_DIR = os.path.join(BASE_DIR, "ProjectD", "files")

def start_project_a():
    print("🚀 Starting Project A (Streamlit on 5001)...")
    return subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", "5001", "--server.headless", "true"],
        cwd=PROJECT_A_DIR,
        shell=True
    )

def start_project_b():
    print("🚀 Starting Project B (Flask on 5004)...")
    return subprocess.Popen(
        [sys.executable, "app.py"],
        cwd=PROJECT_B_DIR,
        shell=True
    )

def start_project_c():
    print("🚀 Starting Project C (Flask on 5002)...")
    return subprocess.Popen(
        [sys.executable, "app.py"],
        cwd=PROJECT_C_DIR,
        shell=True
    )

def start_project_d():
    print("🚀 Starting Project D (Node on 5003)...")
    return subprocess.Popen(
        ["node", "server.js"],
        cwd=PROJECT_D_DIR,
        shell=True
    )

def main():
    processes = []
    try:
        # Start all projects
        processes.append(start_project_a())
        processes.append(start_project_c())
        processes.append(start_project_d())
        processes.append(start_project_b())

        print("\n✅ All projects are starting up...")
        print("🔗 Dashboard will be available at: " + os.path.join(BASE_DIR, "dashboard", "index.html"))
        
        # Wait a few seconds for servers to initialize
        time.sleep(5)
        
        # Open the dashboard in the default browser
        dashboard_path = "file://" + os.path.join(BASE_DIR, "dashboard", "index.html").replace("\\", "/")
        print(f"🌍 Opening Dashboard: {dashboard_path}")
        webbrowser.open(dashboard_path)

        print("\nPress Ctrl+C to stop all servers.")
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Stopping all servers...")
        for p in processes:
            p.terminate()
        print("Done.")

if __name__ == "__main__":
    main()
