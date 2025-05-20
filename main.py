import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from transformers import pipeline
import os

# Initialize the vision agent
agent = pipeline("image-classification", model="google/vit-base-patch16-224")

class VisionAnalyzer:
    def __init__(self):
        self.min_confidence = 0.1  # Minimum confidence threshold (10%)
        
    def analyze_image(self, image_path):
        """Analyze image with confidence filtering"""
        if not os.path.exists(image_path):
            return None, "Error: Image file not found"
        
        try:
            img = Image.open(image_path)
            results = agent(img)
            
            # Filter out low-confidence results
            filtered_results = [r for r in results if r['score'] >= self.min_confidence]
            
            if not filtered_results:
                return None, "No confident identifications found (adjust confidence threshold)"
            
            return filtered_results, None
            
        except Exception as e:
            return None, f"Error: {str(e)}"
    
    def create_visualization(self, img, results):
        """Generate matplotlib visualization"""
        try:
           plt.figure(figsize=(10, 5))
          
          # Show image
           plt.subplot(1, 2, 1)
           plt.imshow(img)
           plt.axis('off')
           plt.title("Your Image")
          
           # Show results as bar chart
           plt.subplot(1, 2, 2)
           labels = [r['label'] for r in results]
           scores = [r['score'] for r in results]
          
           if not scores:  # Handle empty results
               plt.text(0.5, 0.5, "No results meet confidence threshold",
                       ha='center', va='center')
               plt.axis('off')
           else:
               colors = plt.cm.viridis([s/max(scores) for s in scores])
               bars = plt.barh(labels, scores, color=colors)
               plt.xlabel('Confidence Score')
               plt.title('Analysis Results')
               plt.xlim(0, 1)
             
               # Add value labels with robust positioning
               for bar in bars:
                   width = bar.get_width()
                   plt.text(min(width + 0.01, 0.99),  # Prevent overflow
                           bar.get_y() + bar.get_height()/2, 
                           f'{width:.0%}', 
                           va='center', 
                           ha='left')
         
           plt.tight_layout()
           plt.show()
         
        except Exception as e:
          messagebox.showerror("Visualization Error", 
                             f"Could not create visualization:\n{str(e)}")
          plt.close('all')

class VisionGUI:
    def __init__(self, root):
        self.root = root
        self.analyzer = VisionAnalyzer()
        self.setup_gui()
        
    def setup_gui(self):
        """Create the GUI interface"""
        self.root.title("Vision Analyzer")
        self.root.geometry("500x600")
        
        # Main container
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Image display
        self.img_label = tk.Label(main_frame)
        self.img_label.pack(pady=10)
        
        # Confidence threshold slider
        tk.Label(main_frame, text="Confidence Threshold:").pack()
        self.confidence_slider = tk.Scale(
            main_frame, from_=0, to=100, orient=tk.HORIZONTAL,
            command=self.update_threshold_and_refresh)
        self.confidence_slider.set(10)  # Default 10%
        self.confidence_slider.pack(fill=tk.X)
        
        # Buttons
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Select Image", command=self.load_image).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Show Visualization", command=self.show_visualization).pack(side=tk.LEFT, padx=5)
        
        # Results display
        results_frame = tk.LabelFrame(main_frame, text="Analysis Results", padx=5, pady=5)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        self.results_text = tk.Text(results_frame, height=10, wrap=tk.WORD)
        scrollbar = tk.Scrollbar(results_frame, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
    def update_threshold_and_refresh(self, value):
        """Update confidence threshold and refresh results"""
        self.analyzer.min_confidence = float(value)/100
        if hasattr(self, 'current_image'):
            self.refresh_results()
            
    def refresh_results(self):
        """Refresh the results display"""
        results, error = self.analyzer.analyze_image(self.current_image)
        
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        
        if error:
            self.results_text.insert(tk.END, error)
        else:
            self.results_text.insert(tk.END, 
                f"Minimum Confidence: {self.analyzer.min_confidence:.0%}\n\n")
            
            for i, result in enumerate(results, 1):
                self.results_text.insert(tk.END, 
                    f"{i}. {result['label']} ({result['score']:.0%} confidence)\n")
        
        self.results_text.config(state=tk.DISABLED)
        
    def load_image(self):
        """Load image file"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.current_image = file_path
            img = Image.open(file_path)
            img.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(img)
            self.img_label.config(image=photo)
            self.img_label.image = photo
            self.refresh_results()
            
    def show_visualization(self):
        """Show matplotlib visualization"""
        if hasattr(self, 'current_image'):
            img = Image.open(self.current_image)
            results, error = self.analyzer.analyze_image(self.current_image)
            
            if error:
                messagebox.showerror("Error", error)
            else:
                self.analyzer.create_visualization(img, results)
        else:
            messagebox.showwarning("Warning", "Please select an image first")

if __name__ == "__main__":
    root = tk.Tk()
    app = VisionGUI(root)
    root.mainloop()
