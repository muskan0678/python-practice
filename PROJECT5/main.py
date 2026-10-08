import tkinter as tk
import time
from PIL import Image, ImageTk

# Main Window
root= tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("800x600")

# List of Image Paths
image_paths= [
    r"C:\Users\Ansari Muskan\Downloads\OIP (3).jpg",
    r"C:\Users\Ansari Muskan\Downloads\OIP (2).jpg",
    r"C:\Users\Ansari Muskan\Downloads\OIP (1).jpg",
    r"C:\Users\Ansari Muskan\Downloads\OIP.jpg",
]

image_size= (700, 700)
images= []
for path in image_paths:
    img= Image.open(path)
    img= img.resize(image_size)
    images.append(img)

# Convert PIL Images into Tkinter Compatible Image
final_images= []
for img in images:
    photo= ImageTk.PhotoImage(img)
    final_images.append(photo)

# Lable widget to keep photo
image_label= tk.Label(root)
image_label.pack(pady=30)

# Slideshow Function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image= photo
        root.update()
        time.sleep(2)

# Button
play_button=tk.Button(
    root,
    text= "Play the Slideshow",
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop()