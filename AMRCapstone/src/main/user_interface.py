import tkinter as tk
from tkinter import scrolledtext, Label
import requests
import json
import threading
from PIL import Image, ImageTk 
import io
import base64

SERVER_URL = "http://localhost:8080"

def fetch_robot_info():
  try:
      response = requests.get(f"{SERVER_URL}/robot")
      if response.status_code == 200:
          return response.json()
      else:
          print("Failed to fetch robot info")
          return None
  except Exception as e:
      print(f"Error: {e}")
      return None

def update_coordinates():
    robot_info = fetch_robot_info()
    if robot_info:
        x_coord_label.config(text=f"X: {robot_info['x_pos']}")
        y_coord_label.config(text=f"Y: {robot_info['y_pos']}")
    root.after(1000, update_coordinates)  # Update every second

def update_qr_and_destination():
    robot_info = fetch_robot_info()
    if robot_info:
        # Update QR code information
        qr_code_info = robot_info.get('qrScan', 'No QR Code Info')
        qr_label.config(text=f"QR Code: {qr_code_info}")
        # Update destination information
        dest_x_label.config(text=f"X: {robot_info.get('x_destination', 0)}")
        dest_y_label.config(text=f"Y: {robot_info.get('y_destination', 0)}")
    root.after(1000, update_qr_and_destination)
def update_robot_actions():
    robot_info = fetch_robot_info()
    if robot_info:
        current_action = robot_info.get('message', 'No current action')
        actions_log.delete('1.0', tk.END)
        actions_log.insert(tk.END, current_action)
    root.after(1000, update_robot_actions)

def update_log():
    robot_info = fetch_robot_info()
    if robot_info:
        log_info = robot_info.get('loggerList',[])
        log_display.delete('1.0', tk.END)
        for entry in log_info:
            log_display.insert(tk.END, entry + "\n")
    root.after(1000, update_log)
#def update_image():
   # robot_info = fetch_robot_info()
   # if robot_info:
    #    image_data = robot_info['image']
    #    image = Image.open(io.BytesIO(image_data))
    #    photo = ImageTk.PhotoImage(image)

    #    image_label.config(image=photo)
    #    image_label.image = photo
   # else:
    #    image_label.config(image='')
    #root.after(1000, update_image)

#b64 decoding
def update_image():
    robot_info = fetch_robot_info()
    if robot_info and robot_info['image']:
        base64_image = robot_info['image']
        image_data = base64.b64decode(base64_image)
        image = Image.open(io.BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)

        image_label.config(image=photo)
        image_label.image = photo
    else:
        image_label.config(image='')
    root.after(1000, update_image)

# Create the main window
root = tk.Tk()
root.title("AMR Jetson Bot")
# window size
root.geometry("800x600")

# Create a frame for the left side and right side of the interface
left_frame = tk.Frame(root, width=400, height=600)
left_frame.pack(side="left", fill="both", expand=True)

upper_frame_left = tk.Frame(left_frame)
upper_frame_left.pack(side="top", fill="both", expand=True)

lower_frame_left = tk.Frame(left_frame, height=300)
lower_frame_left.pack(side="bottom", fill="x", expand=True)

right_frame = tk.Frame(root, width=400, height=600)
right_frame.pack(side="right", fill="both", expand=True)

upper_frame = tk.Frame(right_frame)
upper_frame.pack(side="top", fill="both", expand=True)

lower_frame = tk.Frame(right_frame, height=300)
lower_frame.pack(side="bottom", fill="x", expand=True)
# Create a label for "Coordinates"
coordinates_label = tk.Label(upper_frame_left, text="Coordinates:")
coordinates_label.pack()

# Create labels for x and y coordinates
x_coord_label = tk.Label(upper_frame_left, text="X: 0")
x_coord_label.pack()
y_coord_label = tk.Label(upper_frame_left, text="Y: 0")
y_coord_label.pack()

# Create a label for destination
destination_label = tk.Label(upper_frame_left, text="Destination:")
destination_label.pack()

# Create labels for x and y coordinates side by side
dest_x_label = tk.Label(upper_frame_left, text="X: 0")
dest_x_label.pack()
dest_y_label = tk.Label(upper_frame_left, text="Y: 0")
dest_y_label.pack()

# Create an empty space (placeholder) for the QR code
#empty_qr_label = tk.Label(qr_frame, text="QR Code Placeholder", padx=50, pady=50, relief="ridge")
#empty_qr_label.pack()
#real qr lablel
qr_label = tk.Label(upper_frame_left, text="QR Code Info:")
qr_label.pack()

title_label = tk.Label(upper_frame, text="Robot Camera View", bg='darkgray')
title_label.pack(fill="x")
image_label = tk.Label(upper_frame)  # Background color for debugging
image_label.pack(fill="both", expand=True)

# Create a scrolled text widget for logging
log_display_label = tk.Label(lower_frame, text="Status:")
log_display_label.pack()
log_display = scrolledtext.ScrolledText(lower_frame, wrap=tk.WORD, width=40, height=10)
log_display.pack(fill="both", expand=True)

#Robot actions log
actions_log_label = tk.Label(lower_frame_left, text="Robot Actions Log:")
actions_log_label.pack()
actions_log = scrolledtext.ScrolledText(lower_frame_left, wrap=tk.WORD, width=40, height=10)
actions_log.pack(fill="both", expand=True)

threading.Thread(target=update_coordinates, daemon=True).start()
threading.Thread(target=update_qr_and_destination, daemon=True).start()
threading.Thread(target=update_image, daemon=True).start()
threading.Thread(target=update_robot_actions, daemon=True).start()
threading.Thread(target=update_log, daemon=True).start()

root.mainloop()
