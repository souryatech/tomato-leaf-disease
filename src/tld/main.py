import os
import socket
import subprocess
import time
import webbrowser

from src.tld.helpers import get_file_path


def is_port_in_use(port):
    """Check if a specific port is in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(("localhost", port)) == 0


def run():
    PORT = 8080
    if not is_port_in_use(PORT):
        # Launch Streamlit app without opening a browser
        process = subprocess.Popen(
            [
                "streamlit",
                "run",
                get_file_path("src/tld/streamlit.py"),
                "--server.headless=true",
                f"--server.port={PORT}",
                "--server.address=0.0.0.0",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print("Running server on port", PORT)
        # Wait until the server is ready
        for _ in range(30):  # Timeout after 30 seconds
            if is_port_in_use(PORT):
                break
            time.sleep(1)
        else:
            print("Streamlit server failed to start.")
            process.terminate()
            return

        # Open the app in a single browser instance
        webbrowser.open(f"http://localhost:{PORT}")

        # Wait for the process to finish
        process.communicate()
    else:
        print(f"Port {PORT} is already in use. Is another instance running?")


if __name__ == "__main__":
    run()
