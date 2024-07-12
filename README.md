# Compression & Encryption
# A Python Application for Compress and Encrypt files
## برنامه فشرده سازی و رمزنگاری فایل ها به زبان پایتون

## سینا بهرامی `9900442201`

این پروژه شامل فشرده‌سازی و رمزنگاری فایل‌ها با استفاده از دو الگوریتم مختلف برای فشرده‌سازی (Huffman و zlib) و یک روش رمزنگاری متقارن است.

### ` در این پروژه مدیریت ارور ها در هر بخش بصورت کامل هندل و پیام های مشخصی قرار داده ایم `

### فشرده‌سازی و باز کردن فشرده‌سازی با استفاده از zlib

فایل `compression.py` وظیفه فشرده‌سازی و باز کردن فشرده‌سازی فایل‌ها را با استفاده از کتابخانه zlib برعهده دارد.

#### تابع `compress_file`

این تابع یک فایل را با استفاده از الگوریتم فشرده‌سازی zlib فشرده می‌کند.

```python
import zlib

def compress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        compressed_data = zlib.compress(data, level=9)
        with open(output_file, 'wb') as f:
            f.write(compressed_data)
    except Exception as e:
        print(f"Error during zlib compression: {e}")
```

- **وارد کردن zlib**: کتابخانه `zlib` برای فشرده‌سازی استفاده می‌شود.
- **خواندن فایل ورودی**: فایل ورودی به صورت باینری باز و محتویات آن خوانده می‌شود.
- **فشرده‌سازی داده‌ها**: داده‌ها با استفاده از `zlib.compress` و سطح فشرده‌سازی ۹ فشرده می‌شوند.
- **نوشتن فایل خروجی**: داده‌های فشرده‌شده در فایل خروجی به صورت باینری نوشته می‌شوند.
- **مدیریت خطا**: هرگونه استثنا که در طول فرآیند رخ دهد، گرفته شده و چاپ می‌شود.

#### تابع `decompress_file`

این تابع فایل فشرده‌شده با zlib را باز می‌کند.

```python
def decompress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            compressed_data = f.read()

        data = zlib.decompress(compressed_data)
        with open(output_file, 'wb') as f:
            f.write(data)
    except Exception as e:
        print(f"Error during zlib decompression: {e}")
```

- **خواندن فایل فشرده‌شده**: فایل ورودی به صورت باینری باز و محتویات فشرده‌شده آن خوانده می‌شود.
- **باز کردن فشرده‌سازی داده‌ها**: داده‌ها با استفاده از `zlib.decompress` باز می‌شوند.
- **نوشتن فایل خروجی**: داده‌های باز شده در فایل خروجی به صورت باینری نوشته می‌شوند.
- **مدیریت خطا**: هرگونه استثنا که در طول فرآیند رخ دهد، گرفته شده و چاپ می‌شود.

### رمزنگاری و رمزگشایی

فایل `encryption.py` وظیفه رمزنگاری و رمزگشایی فایل‌ها را با استفاده از رمزنگاری متقارن Fernet از کتابخانه cryptography برعهده دارد.

#### تابع `generate_key`

یک کلید رمزنگاری جدید تولید و آن را در یک فایل ذخیره می‌کند.

```python
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
```

- **وارد کردن Fernet**: از ماژول `cryptography.fernet`.
- **تولید کلید**: یک کلید رمزنگاری جدید با استفاده از `Fernet.generate_key` تولید می‌شود.
- **ذخیره کلید**: کلید تولید‌شده در فایل `key.key` به صورت باینری نوشته می‌شود.

#### تابع `load_key`

این تابع کلید رمزنگاری ذخیره‌شده را بارگذاری می‌کند.

```python
def load_key():
    return open("key.key", "rb").read()
```

- **بارگذاری کلید**: فایل `key.key` به صورت باینری باز و کلید خوانده می‌شود.

#### تابع `encrypt_file`

این تابع یک فایل را با استفاده از کلید داده‌شده رمزنگاری می‌کند.

```python
def encrypt_file(input_file, output_file, key):
    f = Fernet(key)
    with open(input_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
```

- **ایجاد شیء Fernet**: از کلید داده‌شده برای ایجاد یک شیء Fernet استفاده می‌شود.
- **خواندن فایل ورودی**: فایل ورودی به صورت باینری باز و داده‌های آن خوانده می‌شوند.
- **رمزنگاری داده‌ها**: داده‌های فایل با استفاده از روش Fernet رمزنگاری می‌شوند.
- **نوشتن فایل خروجی**: داده‌های رمزنگاری‌شده در فایل خروجی به صورت باینری نوشته می‌شوند.

#### تابع `decrypt_file`

این تابع یک فایل رمزنگاری‌شده را با استفاده از کلید داده‌شده رمزگشایی می‌کند.

```python
def decrypt_file(input_file, output_file, key):
    f = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
```

- **ایجاد شیء Fernet**: از کلید داده‌شده برای ایجاد یک شیء Fernet استفاده می‌شود.
- **خواندن فایل ورودی**: فایل ورودی به صورت باینری باز و داده‌های رمزنگاری‌شده آن خوانده می‌شود.
- **رمزگشایی داده‌ها**: داده‌های رمزنگاری‌شده با استفاده از روش Fernet رمزگشایی می‌شوند.
- **نوشتن فایل خروجی**: داده‌های رمزگشایی‌شده در فایل خروجی به صورت باینری نوشته می‌شوند.

### رابط کاربری گرافیکی (GUI)

فایل `gui.py` یک رابط کاربری گرافیکی با استفاده از کتابخانه tkinter برای فشرده‌سازی، باز کردن فشرده‌سازی، رمزنگاری و رمزگشایی فایل‌ها ایجاد می‌کند.

#### کلاس `CompressionApp`

این کلاس رابط کاربری برنامه را مدیریت می‌کند.

```python
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkthemes import ThemedTk
import huffman
import compression
import encryption
import os
import tarfile
import webbrowser
from PIL import Image, ImageTk

class CompressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Compression and Encryption")
        self.root.geometry("500x450")

        # Load logo image
        self.load_logo()

        self.method_var = tk.StringVar(value="huffman")
        encryption.generate_key()
        self.key = encryption.load_key()

        self.create_widgets()

    def load_logo(self):
        try:
            self.logo_image = Image.open("logo.png")
            self.logo_image = self.logo_image.resize((100, 100), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        except Exception as e:
            print(f"Error loading logo: {e}")
            self.logo_photo = None

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Display logo
        if self.logo_photo:
            logo_label = tk.Label(frame, image=self.logo_photo)
            logo_label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Select Compression Method:", font=("Helvetica", 14)).grid(row=1, column=0, columnspan=2, pady=10)
        
        tk.Radiobutton(frame, text="Huffman", variable=self.method_var, value="huffman", font=("Helvetica", 12)).grid(row=2, column=0, sticky="e", padx=5)
        tk.Radiobutton(frame, text="Zlib", variable=self.method_var, value="zlib", font=("Helvetica", 12)).grid(row=2, column=1, sticky="w", padx=5)
        
        tk.Button(frame, text="Import File(s)", command=self.choose_input_files, width=20, font=("Helvetica", 10)).grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Button(frame, text="Compress", command=self.compress, width=20, font=("Helvetica", 10)).grid(row=4, column=0, pady=5, padx=5)
        tk.Button(frame, text="Encrypt", command=self.encrypt, width=20, font=("Helvetica", 10)).grid(row=4, column=1, pady=5, padx=5)
        
        tk.Button(frame, text="Decompress", command=self.decompress, width=20, font=("Helvetica", 10)).grid(row=5, column=0, pady=5, padx=5)
        tk.Button(frame, text="Decrypt", command=self.decrypt, width=20, font=("Helvetica", 10)).grid(row=5, column=1, pady=5, padx=5)

        # Add GitHub link
        github_label = tk.Label(frame, text="GitHub: meta-syfu", font=("Helvetica", 12), fg="blue", cursor="hand2")
        github_label.grid(row=6, column=0, columnspan=2, pady=20)
        github_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/meta-syfu/compression"))

        self.input_files = []
        self.output_file = None

    def choose_input_files(self):
        self.input_files = filedialog.askopenfilenames(title="Select File(s)")
        if not self.input_files:
            messagebox.showwarning("Warning", "No files selected!")
    
    def compress(self):
        if not self.input_files:
            messagebox.showwarning("Warning", "No files selected!")
            return

        for input_file in self.input_files:
            output_file = input_file + ".huff" if self.method_var.get() == "huffman" else input_file + ".zlib"
            try:
                if self.method_var.get() == "huffman":
                    huffman.compress_file(input_file, output_file)
                else:
                    compression.compress_file(input_file, output_file)
                messagebox.showinfo("Success", f"File compressed successfully: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Compression failed: {e}")

    def decompress(self):
        if not self.input_files:
            messagebox.showwarning("Warning", "No files selected!")
            return

        for input_file in self.input_files:
            if input_file.endswith(".huff"):
                output_file = input_file.replace(".huff", "")
                try:
                    huffman.decompress_file(input_file, output_file)
                    messagebox.showinfo("Success", f"File decompressed successfully: {output_file}")
                except Exception as e:
                    messagebox.showerror("Error", f"Decompression failed: {e}")
            elif input_file.endswith(".zlib"):
                output_file = input_file.replace(".zlib", "")
                try:
                    compression.decompress_file(input_file, output_file)
                    messagebox.showinfo("Success", f"File decompressed successfully: {output_file}")
                except Exception as e:
                    messagebox.showerror("Error", f"Decompression failed: {e}")
            else:
                messagebox.showwarning("Warning", "Unsupported file format for decompression!")

    def encrypt(self):
        if not self.input_files:
            messagebox.showwarning("Warning", "No files selected!")
            return

        for input_file in self.input_files:
            output_file = input_file + ".enc"
            try:
                encryption.encrypt_file(input_file, output_file, self.key)
                messagebox.showinfo("Success", f"File encrypted successfully: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Encryption failed: {e}")

    def decrypt(self):
        if not self.input_files:
            messagebox.showwarning("Warning", "No files selected!")
            return

        for input_file in self.input_files:
            if input_file.endswith(".enc"):
                output_file = input_file.replace(".enc", "")
                try:
                    encryption.decrypt_file(input_file, output_file, self.key)
                    messagebox.showinfo("Success", f"File decrypted successfully: {output_file}")
                except Exception as e:
                    messagebox.showerror("Error", f"Decryption failed: {e}")
            else:
                messagebox.showwarning("Warning", "Unsupported file format for decryption!")

    def open_github(self, event):
        webbrowser.open_new("https://github.com/meta-syfu/compression")
```

- **وارد کردن کتابخانه‌های لازم**: کتابخانه‌های مختلفی از جمله tkinter، filedialog، messagebox، ttkthemes، huffman، compression، encryption، os، tarfile، webbrowser، PIL برای ایجاد رابط کاربری گرافیکی و عملیات مختلف فایل وارد می‌شوند.
- **تعریف کلاس `CompressionApp`**: این کلاس تمام عملکردهای رابط کاربری برنامه را مدیریت می‌کند.
- **تابع `__init__`**: این تابع اصلی است که تمام ویجت‌های رابط کاربری را ایجاد و تنظیم می‌کند.
- **تابع `load_logo`**: این تابع لوگوی برنامه را بارگذاری و تنظیم می‌کند.
- **تابع `create_widgets`**: این تابع ویجت‌های مختلف مانند دکمه‌ها، لیبل‌ها و رادیوباتن‌ها را ایجاد می‌کند.
- **تابع `choose_input_files`**: این تابع فایل‌های ورودی را انتخاب می‌کند.
- **تابع `compress`**: این تابع فایل‌های انتخاب‌شده را فشرده می‌کند.
- **تابع `decompress`**: این تابع فایل‌های انتخاب‌شده را باز می‌کند.
- **تابع `encrypt`**: این تابع فایل‌های انتخاب‌شده را رمزنگاری می‌کند.
- **تابع `decrypt`**: این تابع فایل‌های انتخاب‌شده را رمزگشایی می‌کند.
- **تابع `open_github`**: این تابع لینک مخزن GitHub را باز می‌کند.

### نتیجه‌گیری

این پروژه شامل پیاده‌سازی الگوریتم‌های فشرده‌سازی و رمزنگاری فایل‌ها با استفاده از کتابخانه‌های مختلف پایتون است. رابط کاربری گرافیکی ایجاد شده با استفاده از tkinter به شما اجازه می‌دهد تا به سادگی فایل‌های خود را فشرده‌سازی، باز کردن فایل های فشرده‌سازی شده، رمزنگاری و رمزگشایی کنند.
