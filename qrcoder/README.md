# Custom QR Code Generator

A modern and clean desktop application built with Python using **CustomTkinter** that allows you to easily generate eye-catching red QR codes from text inputs or URLs. The application features an advanced tool to optionally overlay your custom brand logo or image right into the center of the QR code without compromising scannability.

---

## 🚀 Features

* **Modern Dark/Light UI:** Built using `customtkinter` for a responsive, sleek, and high-quality appearance.
* **Optional Center Branding:** Browse and place custom image logos (`.png`, `.jpg`, `.jpeg`, `.webp`) at the center of the generated QR code.
* **High Fault Tolerance:** Uses high-level error correction (`ERROR_CORRECT_H`), ensuring your QR code remains fully functional even with a center logo embedded.
* **Live In-App Preview:** Instant rendering of your customized QR code directly inside the application canvas window.
* **Flexible Disk Export:** Export and save your high-resolution QR codes cleanly into PNG, JPEG, or WebP formats.

---

## 🛠️ Prerequisites & Installation

Before running the application, you must install the required dependencies using python's package manager.

```bash
pip install customtkinter qrcode pillow
```

### Linux Users Note 💡
If you are running the project on a Linux system (like Ubuntu/Debian), ensure you have the core system GUI dependencies installed for `tkinter`:

```bash
sudo apt-get update
sudo apt-get install python3-tk
```

---

## 💻 How To Run

1. Clone or save your script file locally as `main.py`.
2. Open your terminal or command prompt in that directory.
3. Launch the desktop GUI program using:

```bash
python QR_gen.py
```

---

## 📋 How To Use

1. **Input Data:** Type or paste your desired text content or URL web address into the entry field block.
2. **Add a Logo (Optional):** Click the **"Browse Images"** button to load an image file from your machine to place in the center. If skipped, a clean standard QR code will generate instead.
3. **Render QR:** Hit **"Generate QR code"** to view your output instantly inside the display pane.
4. **Save File:** Click **"Save your QR"**, pick a file system target destination directory along with your preferred extension format, and save it!

---

## ⚙️ Project Structure Explained

* **`App(ctk.CTk)`**: Root application container responsible for building the window geometry, alignment grids, frames, and styling tags.
* **`Select_img_file`**: Handles secure file explorer dialog access arrays for pulling external graphic assets.
* **`generated_QRCode`**: Calculates dimensions, maps raw text matrices into QR elements, normalizes colors into `RGB` space, automatically scales central emblems down cleanly to a safe **20% size boundary**, and pastes them securely.
* **`save_QR_image_to_disk`**: Directs buffered file streams onto local partitions safely.
