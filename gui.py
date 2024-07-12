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
        self.output_dir = None
        self.tree = None
    
    def choose_input_files(self):
        self.input_files = filedialog.askopenfilenames()
        if not self.input_files:
            messagebox.showerror("Error", "Please select at least one input file.")
        else:
            messagebox.showinfo("Files selected", f"Selected files:\n{'\n'.join(self.input_files)}")

    def compress(self):
        if not self.input_files:
            messagebox.showerror("Error", "Please select at least one input file.")
            return
        method = self.method_var.get()
        self.output_dir = filedialog.askdirectory()
        if not self.output_dir:
            messagebox.showerror("Error", "Please specify an output directory.")
            return
        try:
            output_file = os.path.join(self.output_dir, "compressed_files.tar")
            self.compress_files(self.input_files, output_file, method)
            messagebox.showinfo("Success", f"Files compressed and saved as {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Compression failed: {e}")
    
    def compress_files(self, input_files, output_file, method="huffman"):
        try:
            with tarfile.open(output_file, "w") as tar:
                for input_file in input_files:
                    compressed_file = input_file + ".compressed"
                    if method == "huffman":
                        huffman.compress_file(input_file, compressed_file)
                    elif method == "zlib":
                        compression.compress_file(input_file, compressed_file)
                    tar.add(compressed_file, arcname=os.path.basename(compressed_file))
                    os.remove(compressed_file)
        except Exception as e:
            print(f"Error during compression: {e}")
    
    def decompress_files(self, input_file, output_dir, method="huffman"):
        try:
            with tarfile.open(input_file, "r") as tar:
                tar.extractall(path=output_dir)
                for member in tar.getmembers():
                    compressed_file = os.path.join(output_dir, member.name)
                    decompressed_file = os.path.splitext(compressed_file)[0]
                    if method == "huffman":
                        huffman.decompress_file(compressed_file, decompressed_file)
                    elif method == "zlib":
                        compression.decompress_file(compressed_file, decompressed_file)
                    os.remove(compressed_file)
        except Exception as e:
            print(f"Error during decompression: {e}")
    
    def decompress(self):
        input_file = filedialog.askopenfilename(defaultextension=".tar", filetypes=[("Compressed files", "*.tar")])
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        self.output_dir = filedialog.askdirectory()
        if not self.output_dir:
            messagebox.showerror("Error", "Please specify an output directory.")
            return
        try:
            method = self.method_var.get()
            self.decompress_files(input_file, self.output_dir, method)
            messagebox.showinfo("Success", f"Files decompressed and saved in {self.output_dir}")
        except Exception as e:
            messagebox.showerror("Error", f"Decompression failed: {e}")
    
    def encrypt(self):
        if not self.input_files:
            messagebox.showerror("Error", "Please select at least one input file.")
            return
        self.output_dir = filedialog.askdirectory()
        if not self.output_dir:
            messagebox.showerror("Error", "Please specify an output directory.")
            return
        try:
            for input_file in self.input_files:
                output_file = os.path.join(self.output_dir, os.path.basename(input_file) + ".encrypted")
                encryption.encrypt_file(input_file, output_file, self.key)
            messagebox.showinfo("Success", f"Files encrypted and saved in {self.output_dir}")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {e}")
    
    def decrypt(self):
        input_file = filedialog.askopenfilename(defaultextension=".encrypted", filetypes=[("Encrypted files", "*.encrypted")])
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        self.output_dir = filedialog.askdirectory()
        if not self.output_dir:
            messagebox.showerror("Error", "Please specify an output directory.")
            return
        try:
            output_file = os.path.join(self.output_dir, os.path.basename(input_file).replace(".encrypted", ""))
            encryption.decrypt_file(input_file, output_file, self.key)
            messagebox.showinfo("Success", f"File decrypted and saved as {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")  
    app = CompressionApp(root)
    root.mainloop()
