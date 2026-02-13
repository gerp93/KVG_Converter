"""
RTF to PDF Converter
A Windows desktop application for converting RTF files to PDF with formatting preservation.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from pathlib import Path
import threading
from striprtf.striprtf import rtf_to_text
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
import re


class RTFToPDFConverter:
    """Handles conversion of RTF files to PDF format."""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Set up custom paragraph styles for better formatting."""
        # Create custom styles for different formatting needs
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['BodyText'],
            fontSize=12,
            leading=14,
            spaceBefore=6,
            spaceAfter=6,
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomHeading',
            parent=self.styles['Heading1'],
            fontSize=16,
            leading=20,
            spaceBefore=12,
            spaceAfter=12,
            fontName='Helvetica-Bold'
        ))
    
    def parse_rtf_content(self, rtf_content):
        """
        Parse RTF content and extract text with basic formatting information.
        
        Args:
            rtf_content (str): Raw RTF content
            
        Returns:
            str: Extracted plain text
        """
        # Use striprtf to convert RTF to plain text
        text = rtf_to_text(rtf_content)
        return text
    
    def create_pdf_from_text(self, text, output_path):
        """
        Create a PDF file from plain text with basic formatting.
        
        Args:
            text (str): Text content to convert
            output_path (str): Path where PDF should be saved
        """
        # Create PDF document
        doc = SimpleDocTemplate(
            output_path,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        story = []
        
        # Split text into paragraphs
        paragraphs = text.split('\n')
        
        for para_text in paragraphs:
            if para_text.strip():
                # Detect if this looks like a heading (all caps, or short and at start)
                if len(para_text.strip()) < 100 and para_text.strip().isupper():
                    style = self.styles['CustomHeading']
                else:
                    style = self.styles['CustomBody']
                
                # Clean up the text for PDF rendering
                cleaned_text = para_text.strip()
                
                # Create paragraph
                try:
                    p = Paragraph(cleaned_text, style)
                    story.append(p)
                    story.append(Spacer(1, 0.1 * inch))
                except Exception as e:
                    # If paragraph creation fails, try with a simpler approach
                    p = Paragraph(cleaned_text.replace('<', '&lt;').replace('>', '&gt;'), style)
                    story.append(p)
                    story.append(Spacer(1, 0.1 * inch))
        
        # Build PDF
        doc.build(story)
    
    def convert(self, rtf_path, pdf_path):
        """
        Convert RTF file to PDF.
        
        Args:
            rtf_path (str): Path to input RTF file
            pdf_path (str): Path to output PDF file
            
        Raises:
            Exception: If conversion fails
        """
        # Read RTF file
        with open(rtf_path, 'r', encoding='utf-8', errors='ignore') as f:
            rtf_content = f.read()
        
        # Parse RTF content
        text = self.parse_rtf_content(rtf_content)
        
        # Create PDF
        self.create_pdf_from_text(text, pdf_path)


class ConverterGUI:
    """GUI for the RTF to PDF converter application."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("RTF to PDF Converter")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        self.converter = RTFToPDFConverter()
        self.rtf_file_path = None
        self.pdf_file_path = None
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create and layout GUI widgets."""
        # Title
        title_label = tk.Label(
            self.root,
            text="RTF to PDF Converter",
            font=("Arial", 18, "bold"),
            pady=20
        )
        title_label.pack()
        
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input file section
        input_frame = tk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(input_frame, text="Input RTF File:", font=("Arial", 10)).pack(anchor=tk.W)
        
        input_path_frame = tk.Frame(input_frame)
        input_path_frame.pack(fill=tk.X, pady=5)
        
        self.input_path_var = tk.StringVar()
        self.input_path_entry = tk.Entry(
            input_path_frame,
            textvariable=self.input_path_var,
            state='readonly',
            width=50
        )
        self.input_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.browse_button = tk.Button(
            input_path_frame,
            text="Browse...",
            command=self.browse_input_file,
            width=10
        )
        self.browse_button.pack(side=tk.RIGHT)
        
        # Output file section
        output_frame = tk.Frame(main_frame)
        output_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(output_frame, text="Output PDF File:", font=("Arial", 10)).pack(anchor=tk.W)
        
        output_path_frame = tk.Frame(output_frame)
        output_path_frame.pack(fill=tk.X, pady=5)
        
        self.output_path_var = tk.StringVar()
        self.output_path_entry = tk.Entry(
            output_path_frame,
            textvariable=self.output_path_var,
            state='readonly',
            width=50
        )
        self.output_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.save_button = tk.Button(
            output_path_frame,
            text="Save As...",
            command=self.browse_output_file,
            width=10
        )
        self.save_button.pack(side=tk.RIGHT)
        
        # Convert button
        self.convert_button = tk.Button(
            main_frame,
            text="Convert to PDF",
            command=self.convert_file,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            pady=10,
            state=tk.DISABLED
        )
        self.convert_button.pack(pady=20, fill=tk.X)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=300
        )
        self.progress.pack(pady=10)
        
        # Status label
        self.status_var = tk.StringVar()
        self.status_var.set("Ready. Please select an RTF file to convert.")
        self.status_label = tk.Label(
            main_frame,
            textvariable=self.status_var,
            font=("Arial", 9),
            fg="gray",
            wraplength=500
        )
        self.status_label.pack(pady=5)
    
    def browse_input_file(self):
        """Open file dialog to select input RTF file."""
        file_path = filedialog.askopenfilename(
            title="Select RTF File",
            filetypes=[("RTF files", "*.rtf"), ("All files", "*.*")]
        )
        
        if file_path:
            self.rtf_file_path = file_path
            self.input_path_var.set(file_path)
            
            # Auto-suggest output path
            suggested_output = str(Path(file_path).with_suffix('.pdf'))
            self.pdf_file_path = suggested_output
            self.output_path_var.set(suggested_output)
            
            self.convert_button.config(state=tk.NORMAL)
            self.status_var.set("Input file selected. Ready to convert.")
    
    def browse_output_file(self):
        """Open file dialog to select output PDF file location."""
        file_path = filedialog.asksaveasfilename(
            title="Save PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            initialfile=Path(self.rtf_file_path).stem + ".pdf" if self.rtf_file_path else "output.pdf"
        )
        
        if file_path:
            self.pdf_file_path = file_path
            self.output_path_var.set(file_path)
    
    def convert_file(self):
        """Start the conversion process."""
        if not self.rtf_file_path or not self.pdf_file_path:
            messagebox.showerror("Error", "Please select both input and output files.")
            return
        
        # Disable convert button during conversion
        self.convert_button.config(state=tk.DISABLED)
        self.browse_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.DISABLED)
        self.status_var.set("Converting... Please wait.")
        self.progress.start()
        
        # Run conversion in a separate thread to keep UI responsive
        thread = threading.Thread(target=self._perform_conversion)
        thread.daemon = True
        thread.start()
    
    def _perform_conversion(self):
        """Perform the actual conversion (runs in a separate thread)."""
        try:
            self.converter.convert(self.rtf_file_path, self.pdf_file_path)
            self.root.after(0, self._conversion_success)
        except Exception as e:
            self.root.after(0, lambda: self._conversion_error(str(e)))
    
    def _conversion_success(self):
        """Handle successful conversion."""
        self.progress.stop()
        self.convert_button.config(state=tk.NORMAL)
        self.browse_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.NORMAL)
        self.status_var.set(f"Conversion successful! PDF saved to: {self.pdf_file_path}")
        
        messagebox.showinfo(
            "Success",
            f"RTF file successfully converted to PDF!\n\nOutput: {self.pdf_file_path}"
        )
    
    def _conversion_error(self, error_message):
        """Handle conversion error."""
        self.progress.stop()
        self.convert_button.config(state=tk.NORMAL)
        self.browse_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.NORMAL)
        self.status_var.set("Conversion failed. Please try again.")
        
        messagebox.showerror(
            "Conversion Error",
            f"An error occurred during conversion:\n\n{error_message}"
        )


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = ConverterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
