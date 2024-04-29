import tkinter as tk
import os
from tkinter import filedialog
main_window = tk.Tk()
def select_file():
  file_path = filedialog.askopenfilename(title="เลือกไฟล์รูปภาพ", filetypes=[("รูปภาพ", "*.jpg *.png *.jpeg")])
  if file_path:
    label["text"] = f"รูปภาพที่เลือก: {file_path}"
    move_file(file_path)
select_button = tk.Button( text="เลือกไฟล์", command=select_file)
select_button.pack()

label = tk.Label( text="")
label.pack()
def move_file(path):
  # รับค่าจาก GUI
  source_file = path
  destination_folder = "Project/images"

  # ตรวจสอบว่ามีการป้อนข้อมูล

  # ย้ายไฟล์
  try:
    if not os.path.exists(destination_folder):
      os.makedirs(destination_folder)

    os.rename(source_file, destination_folder + "/" + os.path.basename(source_file))
  except Exception as e:
    print("error")


main_window.mainloop()