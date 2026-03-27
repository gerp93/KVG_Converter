"""
KVG Converter (KVG = Konvertierungstool/versatile file converter)
A desktop application for converting files:
  - RTF to PDF
  - MP4 to GIF
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
from mp4_to_gif_converter import MP4ToGIFConverter


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
    """GUI for the multi-format converter application."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("KVG Converter")
        self.root.geometry("620x500")
        self.root.resizable(False, False)
        
        self.rtf_converter = RTFToPDFConverter()
        self.gif_converter = MP4ToGIFConverter()

        self._create_widgets()
    
    def _create_widgets(self):
        """Create and layout GUI widgets."""
        # Title
        title_label = tk.Label(
            self.root,
            text="KVG Converter",
            font=("Arial", 18, "bold"),
            pady=15
        )
        title_label.pack()

        # Notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

        # Tab 1 – RTF to PDF
        rtf_tab = tk.Frame(self.notebook, padx=20, pady=10)
        self.notebook.add(rtf_tab, text="  RTF → PDF  ")
        self._build_rtf_tab(rtf_tab)

        # Tab 2 – MP4 to GIF
        gif_tab = tk.Frame(self.notebook, padx=20, pady=10)
        self.notebook.add(gif_tab, text="  MP4 → GIF  ")
        self._build_gif_tab(gif_tab)

    # ------------------------------------------------------------------
    # RTF → PDF tab
    # ------------------------------------------------------------------

    def _build_rtf_tab(self, parent):
        """Build widgets for the RTF-to-PDF tab."""
        self.rtf_file_path = None
        self.pdf_file_path = None

        # Input file section
        input_frame = tk.Frame(parent)
        input_frame.pack(fill=tk.X, pady=10)

        tk.Label(input_frame, text="Input RTF File:", font=("Arial", 10)).pack(anchor=tk.W)

        input_path_frame = tk.Frame(input_frame)
        input_path_frame.pack(fill=tk.X, pady=5)

        self.rtf_input_var = tk.StringVar()
        tk.Entry(
            input_path_frame,
            textvariable=self.rtf_input_var,
            state='readonly',
            width=50
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        self.rtf_browse_button = tk.Button(
            input_path_frame,
            text="Browse...",
            command=self._rtf_browse_input,
            width=10
        )
        self.rtf_browse_button.pack(side=tk.RIGHT)

        # Output file section
        output_frame = tk.Frame(parent)
        output_frame.pack(fill=tk.X, pady=10)

        tk.Label(output_frame, text="Output PDF File:", font=("Arial", 10)).pack(anchor=tk.W)

        output_path_frame = tk.Frame(output_frame)
        output_path_frame.pack(fill=tk.X, pady=5)

        self.rtf_output_var = tk.StringVar()
        tk.Entry(
            output_path_frame,
            textvariable=self.rtf_output_var,
            state='readonly',
            width=50
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        self.rtf_save_button = tk.Button(
            output_path_frame,
            text="Save As...",
            command=self._rtf_browse_output,
            width=10
        )
        self.rtf_save_button.pack(side=tk.RIGHT)

        # Convert button
        self.rtf_convert_button = tk.Button(
            parent,
            text="Convert to PDF",
            command=self._rtf_convert,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            pady=10,
            state=tk.DISABLED
        )
        self.rtf_convert_button.pack(pady=15, fill=tk.X)

        # Progress bar
        self.rtf_progress = ttk.Progressbar(parent, mode='indeterminate', length=300)
        self.rtf_progress.pack(pady=5)

        # Status label
        self.rtf_status_var = tk.StringVar(value="Ready. Please select an RTF file to convert.")
        tk.Label(
            parent,
            textvariable=self.rtf_status_var,
            font=("Arial", 9),
            fg="gray",
            wraplength=500
        ).pack(pady=5)

    def _rtf_browse_input(self):
        file_path = filedialog.askopenfilename(
            title="Select RTF File",
            filetypes=[("RTF files", "*.rtf"), ("All files", "*.*")]
        )
        if file_path:
            self.rtf_file_path = file_path
            self.rtf_input_var.set(file_path)
            suggested_output = str(Path(file_path).with_suffix('.pdf'))
            self.pdf_file_path = suggested_output
            self.rtf_output_var.set(suggested_output)
            self.rtf_convert_button.config(state=tk.NORMAL)
            self.rtf_status_var.set("Input file selected. Ready to convert.")

    def _rtf_browse_output(self):
        file_path = filedialog.asksaveasfilename(
            title="Save PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            initialfile=Path(self.rtf_file_path).stem + ".pdf" if self.rtf_file_path else "output.pdf"
        )
        if file_path:
            self.pdf_file_path = file_path
            self.rtf_output_var.set(file_path)

    def _rtf_convert(self):
        if not self.rtf_file_path or not self.pdf_file_path:
            messagebox.showerror("Error", "Please select both input and output files.")
            return
        self.rtf_convert_button.config(state=tk.DISABLED)
        self.rtf_browse_button.config(state=tk.DISABLED)
        self.rtf_save_button.config(state=tk.DISABLED)
        self.rtf_status_var.set("Converting... Please wait.")
        self.rtf_progress.start()
        thread = threading.Thread(target=self._rtf_perform_conversion)
        thread.daemon = True
        thread.start()

    def _rtf_perform_conversion(self):
        try:
            self.rtf_converter.convert(self.rtf_file_path, self.pdf_file_path)
            self.root.after(0, self._rtf_success)
        except Exception as e:
            self.root.after(0, lambda: self._rtf_error(str(e)))

    def _rtf_success(self):
        self.rtf_progress.stop()
        self.rtf_convert_button.config(state=tk.NORMAL)
        self.rtf_browse_button.config(state=tk.NORMAL)
        self.rtf_save_button.config(state=tk.NORMAL)
        self.rtf_status_var.set(f"Conversion successful! PDF saved to: {self.pdf_file_path}")
        messagebox.showinfo(
            "Success",
            f"RTF file successfully converted to PDF!\n\nOutput: {self.pdf_file_path}"
        )

    def _rtf_error(self, error_message):
        self.rtf_progress.stop()
        self.rtf_convert_button.config(state=tk.NORMAL)
        self.rtf_browse_button.config(state=tk.NORMAL)
        self.rtf_save_button.config(state=tk.NORMAL)
        self.rtf_status_var.set("Conversion failed. Please try again.")
        messagebox.showerror(
            "Conversion Error",
            f"An error occurred during conversion:\n\n{error_message}"
        )

    # ------------------------------------------------------------------
    # MP4 → GIF tab
    # ------------------------------------------------------------------

    def _build_gif_tab(self, parent):
        """Build widgets for the MP4-to-GIF tab."""
        self.mp4_file_path = None
        self.gif_file_path = None

        # Input file section
        input_frame = tk.Frame(parent)
        input_frame.pack(fill=tk.X, pady=8)

        tk.Label(input_frame, text="Input MP4 File:", font=("Arial", 10)).pack(anchor=tk.W)

        input_path_frame = tk.Frame(input_frame)
        input_path_frame.pack(fill=tk.X, pady=4)

        self.mp4_input_var = tk.StringVar()
        tk.Entry(
            input_path_frame,
            textvariable=self.mp4_input_var,
            state='readonly',
            width=50
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        self.mp4_browse_button = tk.Button(
            input_path_frame,
            text="Browse...",
            command=self._mp4_browse_input,
            width=10
        )
        self.mp4_browse_button.pack(side=tk.RIGHT)

        # Output file section
        output_frame = tk.Frame(parent)
        output_frame.pack(fill=tk.X, pady=8)

        tk.Label(output_frame, text="Output GIF File:", font=("Arial", 10)).pack(anchor=tk.W)

        output_path_frame = tk.Frame(output_frame)
        output_path_frame.pack(fill=tk.X, pady=4)

        self.mp4_output_var = tk.StringVar()
        tk.Entry(
            output_path_frame,
            textvariable=self.mp4_output_var,
            state='readonly',
            width=50
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        self.mp4_save_button = tk.Button(
            output_path_frame,
            text="Save As...",
            command=self._mp4_browse_output,
            width=10
        )
        self.mp4_save_button.pack(side=tk.RIGHT)

        # Options frame
        options_frame = tk.Frame(parent)
        options_frame.pack(fill=tk.X, pady=4)

        tk.Label(options_frame, text="FPS:", font=("Arial", 10)).grid(
            row=0, column=0, sticky=tk.W, padx=(0, 5)
        )
        self.gif_fps_var = tk.StringVar(value="10")
        tk.Entry(options_frame, textvariable=self.gif_fps_var, width=6).grid(
            row=0, column=1, sticky=tk.W, padx=(0, 20)
        )

        tk.Label(options_frame, text="Max Width (px):", font=("Arial", 10)).grid(
            row=0, column=2, sticky=tk.W, padx=(0, 5)
        )
        self.gif_max_width_var = tk.StringVar(value="640")
        tk.Entry(options_frame, textvariable=self.gif_max_width_var, width=6).grid(
            row=0, column=3, sticky=tk.W
        )

        # Convert button
        self.mp4_convert_button = tk.Button(
            parent,
            text="Convert to GIF",
            command=self._mp4_convert,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            pady=10,
            state=tk.DISABLED
        )
        self.mp4_convert_button.pack(pady=12, fill=tk.X)

        # Progress bar
        self.mp4_progress = ttk.Progressbar(parent, mode='indeterminate', length=300)
        self.mp4_progress.pack(pady=4)

        # Status label
        self.mp4_status_var = tk.StringVar(value="Ready. Please select an MP4 file to convert.")
        tk.Label(
            parent,
            textvariable=self.mp4_status_var,
            font=("Arial", 9),
            fg="gray",
            wraplength=500
        ).pack(pady=4)

    def _mp4_browse_input(self):
        file_path = filedialog.askopenfilename(
            title="Select MP4 File",
            filetypes=[
                ("Video files", "*.mp4 *.m4v *.mov *.avi *.mkv"),
                ("All files", "*.*"),
            ]
        )
        if file_path:
            self.mp4_file_path = file_path
            self.mp4_input_var.set(file_path)
            suggested_output = str(Path(file_path).with_suffix('.gif'))
            self.gif_file_path = suggested_output
            self.mp4_output_var.set(suggested_output)
            self.mp4_convert_button.config(state=tk.NORMAL)
            self.mp4_status_var.set("Input file selected. Ready to convert.")

    def _mp4_browse_output(self):
        file_path = filedialog.asksaveasfilename(
            title="Save GIF As",
            defaultextension=".gif",
            filetypes=[("GIF files", "*.gif"), ("All files", "*.*")],
            initialfile=Path(self.mp4_file_path).stem + ".gif" if self.mp4_file_path else "output.gif"
        )
        if file_path:
            self.gif_file_path = file_path
            self.mp4_output_var.set(file_path)

    def _mp4_convert(self):
        if not self.mp4_file_path or not self.gif_file_path:
            messagebox.showerror("Error", "Please select both input and output files.")
            return

        try:
            fps = float(self.gif_fps_var.get())
        except ValueError:
            messagebox.showerror("Error", "FPS must be a valid number.")
            return

        max_width_str = self.gif_max_width_var.get().strip()
        max_width = None
        if max_width_str:
            try:
                max_width = int(max_width_str)
            except ValueError:
                messagebox.showerror("Error", "Max Width must be a whole number.")
                return

        self.mp4_convert_button.config(state=tk.DISABLED)
        self.mp4_browse_button.config(state=tk.DISABLED)
        self.mp4_save_button.config(state=tk.DISABLED)
        self.mp4_status_var.set("Converting... this may take a moment. Please wait.")
        self.mp4_progress.start()

        thread = threading.Thread(
            target=self._mp4_perform_conversion,
            args=(fps, max_width),
        )
        thread.daemon = True
        thread.start()

    def _mp4_perform_conversion(self, fps, max_width):
        try:
            self.gif_converter.convert(
                self.mp4_file_path,
                self.gif_file_path,
                fps=fps,
                max_width=max_width,
            )
            self.root.after(0, self._mp4_success)
        except Exception as e:
            self.root.after(0, lambda: self._mp4_error(str(e)))

    def _mp4_success(self):
        self.mp4_progress.stop()
        self.mp4_convert_button.config(state=tk.NORMAL)
        self.mp4_browse_button.config(state=tk.NORMAL)
        self.mp4_save_button.config(state=tk.NORMAL)
        self.mp4_status_var.set(f"Conversion successful! GIF saved to: {self.gif_file_path}")
        messagebox.showinfo(
            "Success",
            f"MP4 file successfully converted to GIF!\n\nOutput: {self.gif_file_path}"
        )

    def _mp4_error(self, error_message):
        self.mp4_progress.stop()
        self.mp4_convert_button.config(state=tk.NORMAL)
        self.mp4_browse_button.config(state=tk.NORMAL)
        self.mp4_save_button.config(state=tk.NORMAL)
        self.mp4_status_var.set("Conversion failed. Please try again.")
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
