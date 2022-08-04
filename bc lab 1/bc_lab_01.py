from tkinter import Tk,ttk
from hashlib import sha256

class crypto:

    def __init__(self) -> None:
        self.plaintext = None
        self.sha_1_hash_string = None
        self.md_5_hash_string = None
    
    def hash(self,plaintext):
        self.plaintext = plaintext
        self.sha_256_hash_string = sha256(str(self.plaintext).encode()).hexdigest()
        return self.sha_256_hash_string
    
class GUI:
    def __init__(self) -> None:
        # setting up basics
        self.window = Tk()
        self.widget = ttk
        self.window.state("zoomed")
        self.window.title("Block Chain Lab 1")
        # putting up widgets
        # input label
        self.request_input_label = self.widget.Label(text="Enter the Plaintext",font=("Arial",20))
        self.request_input_label.pack(pady=10)
        self.input_entry = self.widget.Entry(font=("Arial",20),width=50)
        self.input_entry.pack(pady=20)
        self.ok_button = self.widget.Button(text='Get Hash',command=self.getHashButton,width=10)
        self.ok_button.pack(pady=20)
        # Result label
        self.results_label = self.widget.Label(text='',font=("arial",20))
        self.results_label.pack()
        # Copy to clipboard Buttons
        self.copy_sha_hash_button = self.widget.Button(text='Copy sha-256 hash string to clipboard',command=self.copy_sha_hash_button)
        self.copy_sha_hash_button.pack(pady=20)
        # get hash button command
    def getHashButton(self):
        self.get_input = str(self.input_entry.get())
        self.hashira = crypto()
        self.results=self.hashira.hash(plaintext=self.get_input)
        self.result_string = f"""{self.results}"""
        self.results_label['text'] =  self.result_string
    # sha 256 copy Button Command
    def copy_sha_hash_button(self):
        print(f"{self.results[0]}")
        self.window.clipboard_clear()
        self.window.clipboard_append(f"{self.results[0]}")
        # the magic begins here
    def do_the_magic(self)->None:
        self.window.mainloop()

if __name__ == "__main__":
    GUI().do_the_magic()