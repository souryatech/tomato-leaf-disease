import subprocess
import webbrowser
import socket
import time

def is_port_in_use(port):
    """Check if a specific port is in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(("localhost", port)) == 0

def run():
    port = 8501  # Default Streamlit port
    if not is_port_in_use(port):
        # Launch Streamlit app without opening a browser
        process = subprocess.Popen(
            ["streamlit", "run", "src/tld/streamlit.py", "--server.headless=true"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Wait until the server is ready
        for _ in range(30):  # Timeout after 30 seconds
            if is_port_in_use(port):
                break
            time.sleep(1)
        else:
            print("Streamlit server failed to start.")
            process.terminate()
            return

        # Open the app in a single browser instance
        webbrowser.open(f"http://localhost:{port}")

        # Wait for the process to finish
        process.communicate()
    else:
        print(f"Port {port} is already in use. Is another instance running?")