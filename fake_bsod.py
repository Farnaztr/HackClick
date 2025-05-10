import tkinter as tk

def fake_bsod():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background='blue')
    label = tk.Label(root, text="""
:(
Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.

For more information about this issue and possible fixes, visit https://windows.com/stopcode

If you call a support person, give them this info:
Stop code: CRITICAL_PROCESS_DIED
    """, fg="white", bg="blue", font=("Consolas", 15), justify="left")
    label.pack(padx=90, pady=150, anchor="nw")

    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()

if __name__ == "__main__":
    fake_bsod()
