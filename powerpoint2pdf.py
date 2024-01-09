import os
import comtypes.client
import win32com.client
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class PowerPointToPDFConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("PowerPoint to PDF Converter")
        
        # Create label for directory path
        self.label_path = tk.Label(self.master, text="Please select the directory path where the PowerPoint files are located:")
        self.label_path.pack()
        
        # Create button to select directory
        self.button_select_dir = tk.Button(self.master, text="Select directory", command=self.select_directory)
        self.button_select_dir.pack(pady=10)
        
        # Create button to start conversion
        self.button_convert = tk.Button(self.master, text="Convert to PDF", command=self.convert_to_pdf, state=tk.DISABLED)
        self.button_convert.pack(pady=10)
        
        # Create message box for success message
        self.message_box = tk.messagebox
    
    def select_directory(self):
        # Prompt the user to select the directory where the PowerPoint files are located
        self.input_directory = filedialog.askdirectory(title="Select directory")
        if self.input_directory:
            self.button_convert.config(state=tk.NORMAL)
        
    def convert_to_pdf(self):
        # Iterate through all ppt and pptx files in the input directory and convert them to pdfs
        for filename in os.listdir(self.input_directory):
            if filename.endswith(".ppt") or filename.endswith(".pptx"):
                input_path = os.path.join(self.input_directory, filename)
                output_path = os.path.join(self.input_directory, os.path.splitext(filename)[0])
                self.ppt_to_pdf(input_path, output_path)
                
        # Show success message
        self.message_box.showinfo("Conversion Complete", "PowerPoint to PDF conversion is complete!")
    
    def ppt_to_pdf(self, input_path, output_path):
        # Create PowerPoint application object
        powerpoint = win32com.client.Dispatch("Powerpoint.Application")
        
        # Change the extension of input and output paths to .ppt and .pdf respectively
        input_ppt = os.path.abspath(input_path)
        output_pdf = os.path.abspath(output_path + ".pdf")
        
        # Open the presentation
        presentation = powerpoint.Presentations.Open(input_ppt)
        
        # Save the presentation as PDF
        presentation.SaveAs(output_pdf, 32)  # 32 is the value for PDF format
        
        # Close the presentation and PowerPoint application
        presentation.Close()
        powerpoint.Quit()

if __name__ == "__main__":
    # Create the GUI window
    root = tk.Tk()
    app = PowerPointToPDFConverter(root)
    root.mainloop()
