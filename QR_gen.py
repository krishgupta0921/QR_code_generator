import qrcode
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x700")
        self.title("Custom QR code generator")

        self.logo_path = None
        self.generated_img = None
# input for qr code info
        self.data_lbl=ctk.CTkLabel(self,text="Enter text or URL: ",font=('Arial',14,'bold'))
        self.data_lbl.pack(pady=(20,5))
        self.data=ctk.CTkEntry(self, width=450, placeholder_text="Type here...")
        self.data.pack(pady=5)
# optional logo input
        self.logo_lbl=ctk.CTkLabel(self,text="Optional Logo for QR",font=('Arial',14,'bold'))
        self.logo_lbl.pack(pady=(20,5))
        self.btn_for_logo=ctk.CTkButton(self,text="Browse Images",command=self.Select_img_file)
        self.btn_for_logo.pack(pady=5)
        self.logo_status=ctk.CTkLabel(self,text="No logo selected(Standard QR)",text_color='gray')
        self.logo_status.pack(pady=2)
# generate qr
        self.generated_img_btn=ctk.CTkButton(self,text="Generate QR code",fg_color='green',hover_color='darkgreen',command=self.generated_QRCode)
        self.generated_img_btn.pack(pady=20)

        self.display_qr=ctk.CTkLabel(self,text="Your QR will display here", width=250, height=250, fg_color=("gray90", "gray20"))
        self.display_qr.pack(pady=15)

        self.save_QR_image=ctk.CTkButton(self, text="Save your QR",state='disabled',command=self.save_QR_image_to_disk)
        self.save_QR_image.pack(pady=21)

    def Select_img_file(self):
        """Logo Image file select"""
        file_name=filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files","*.jpg; *.jpeg; *.png; *.webp;")]
        )
        if file_name:
            self.logo_path=file_name
            filename=file_name.split('/')[-1]
            self.logo_status.configure(text_color='cyan',text=f"Selected: {filename}")
    
    def generated_QRCode(self):
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            border=4,
            box_size=10
        )
        user_input=self.data.get().strip()
        qr.add_data(user_input)
        qr.make(fit=True)
        img = qr.make_image(fill_color="red", back_color="black").convert("RGB")
        try:
            if self.logo_path:
                logo = Image.open(self.logo_path)
                logo_size =int(img.size[0]* 0.2)
                logo = logo.resize((logo_size,logo_size))

                pos = ((img.size[0] - logo.size[0]) // 2,
                    (img.size[1] - logo.size[1]) // 2)

                img.paste(logo, pos)
            self.generated_img=img

            ctk_visible_img = ctk.CTkImage(light_image=img, dark_image=img, size=(250, 250))
            self.display_qr.configure(image=ctk_visible_img, text="")
            self.save_QR_image.configure(state='normal')
        except Exception as e:
            messagebox.showerror(f"Error, error occured: {e}")
        
    def save_QR_image_to_disk(self):
        if self.generated_img:
            savefile=filedialog.asksaveasfilename(
                defaultextension=".png"
                ,filetypes=[("PNG IMAGE",'*.png'),("JPEG IMAGE",'*.jpg'),("WEBP ImAGE",'*.webp')]
            )
            if savefile:
                self.generated_img.save(savefile)
                messagebox.showinfo("Success","QR code generated and Saved Successfully!😊")



if __name__ =="__main__":
    App().mainloop()
