import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
import qrcode
from PIL import Image, ImageTk
import pyperclip

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор QR кодов")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.entry_label = ttk.Label(root, text="Введите текст:", font=("Helvetica", 14))
        self.entry_label.pack(pady=5)

        self.entry = ttk.Entry(root, width=30)
        self.entry.pack(pady=5)
        self.entry.bind("<Delete>", self.clear_entry)

        self.generate_button = ttk.Button(root, text="Сгенерировать", command=self.generate_qr)
        self.generate_button.pack(pady=5)

        self.save_button = ttk.Button(root, text="Сохранить", command=self.save_qr)
        self.save_button.pack(pady=5)

        self.theme_label = ttk.Label(root, text="Выберите тему:", font=("Helvetica", 12))
        self.theme_label.pack(pady=5)

        self.theme_combobox = ttk.Combobox(root, values=self.style.theme_names())
        self.theme_combobox.set("clam")
        self.theme_combobox.pack(pady=5)

        self.change_theme_button = ttk.Button(root, text="Применить тему", command=self.change_theme)
        self.change_theme_button.pack(pady=5)

        self.paste_button = ttk.Button(root, text="Вставить из буфера", command=self.paste_from_clipboard)
        self.paste_button.pack(pady=5)

        self.clear_button = ttk.Button(root, text="Очистить данные", command=self.clear_entry)
        self.clear_button.pack(pady=5)

        self.qr_preview_frame = ttk.Frame(root)
        self.qr_preview_frame.pack(pady=10)

        root.bind('<Escape>', self.exit_fullscreen)
        root.bind('<Return>', self.generate_qr)

        self.foreground_color = "black"
        self.background_color = "white"
        self.normal_foreground_color = "black"
        self.normal_background_color = "white"
        self.preview_window = None

    def generate_qr(self, event=None):
        data = self.entry.get()
        if data:
            data_bytes = data.encode('utf-8')
            img = self.generate_qr_image(data_bytes, self.normal_foreground_color, self.normal_background_color)

            if self.preview_window:
                self.preview_window.destroy()

            self.preview_qr(img)

    def generate_qr_image(self, data_bytes, foreground_color, background_color):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data_bytes)
        qr.make(fit=True)

        img = qr.make_image(fill_color=foreground_color, back_color=background_color)
        img = img.resize((300, 300), Image.LANCZOS)

        return img

    def preview_qr(self, img):
        preview_window = tk.Toplevel(self.root)
        preview_window.title("Предпросмотр QR кода")
        preview_window.resizable(False, False)

        self.setup_preview_widgets(preview_window)

        photo = ImageTk.PhotoImage(img)
        qr_label = ttk.Label(preview_window, image=photo)
        qr_label.image = photo
        qr_label.pack(pady=10)

        self.preview_window = preview_window

    def setup_preview_widgets(self, window):
        color_label = ttk.Label(window, text="Выберите цвета QR-кода:")
        color_label.pack(pady=5)

        foreground_color_button = ttk.Button(window, text="Цвет переднего плана", command=self.choose_foreground_color)
        foreground_color_button.pack(pady=5)

        background_color_button = ttk.Button(window, text="Цвет фона", command=self.choose_background_color)
        background_color_button.pack(pady=5)

        reset_colors_button = ttk.Button(window, text="Сбросить к изначальным цветам", command=self.reset_colors)
        reset_colors_button.pack(pady=5)

    def choose_foreground_color(self):
        color = colorchooser.askcolor(initialcolor=self.foreground_color)[1]
        if color:
            self.foreground_color = color
            self.normal_foreground_color = color
            self.generate_qr()

    def choose_background_color(self):
        color = colorchooser.askcolor(initialcolor=self.background_color)[1]
        if color:
            self.background_color = color
            self.normal_background_color = color
            self.generate_qr()

    def reset_colors(self):
        self.foreground_color = "black"
        self.background_color = "white"
        self.normal_foreground_color = "black"
        self.normal_background_color = "white"
        self.generate_qr()

    def save_qr(self):
        data = self.entry.get()
        if data:
            data_bytes = data.encode('utf-8')
            img = self.generate_qr_image(data_bytes, self.normal_foreground_color, self.normal_background_color)

            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

            if filename:
                img.save(filename)
                messagebox.showinfo("Успешно сохранено", "QR код успешно сохранен в формате PNG.")

    def exit_fullscreen(self, event):
        self.root.destroy()

    def paste_from_clipboard(self):
        clipboard_data = pyperclip.paste()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, clipboard_data)

    def change_theme(self):
        selected_theme = self.theme_combobox.get()
        if selected_theme:
            try:
                self.style.theme_use(selected_theme)
                print(f"Тема изменена на {selected_theme}")
            except tk.TclError as e:
                print(f"Ошибка при установке темы: {e}")

    def clear_entry(self, event=None):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.geometry("400x400")
    root.mainloop()
