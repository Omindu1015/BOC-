from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

class RestartAppOnChange(FileSystemEventHandler):
    def __init__(self, filepath):
        self.filepath = filepath
        self.process = subprocess.Popen(["python", self.filepath])

    def on_modified(self, event):
        if event.src_path.endswith(self.filepath):
            print("🔁 Detected change! Restarting app...")
            self.process.kill()
            self.process = subprocess.Popen(["python", self.filepath])

if __name__ == "__main__":
    target_file = "language_ui.py"  # your main GUI script
    handler = RestartAppOnChange(target_file)
    observer = Observer()
    observer.schedule(handler, ".", recursive=False)
    observer.start()

    print(f"👀 Watching for changes in {target_file}...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
