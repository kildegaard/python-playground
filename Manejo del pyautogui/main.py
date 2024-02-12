import tkinter as tk
import pyautogui
import csv


class MousePositionPopup:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Position")
        self.label = tk.Label(root, font=("Helvetica", 16))
        self.label.pack(padx=20, pady=20)
        self.positions = []
        self.update_mouse_position()

        # Bind left mouse click event to save position
        self.root.bind('<Button-1>', self.save_mouse_position)

    def update_mouse_position(self):
        x, y = pyautogui.position()
        self.label.config(text=f"Mouse Position: ({x}, {y})")
        self.root.after(500, self.update_mouse_position)

    def save_mouse_position(self, event):
        x, y = pyautogui.position()
        self.positions.append((x, y))

    def on_close(self):
        # Save positions to a CSV file
        with open('mouse_positions.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['X', 'Y'])
            csv_writer.writerows(self.positions)


if __name__ == "__main__":
    root = tk.Tk()
    app = MousePositionPopup(root)
    # Handle window close event
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
