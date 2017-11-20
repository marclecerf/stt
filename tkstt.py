import Tkinter as tk
import microphone

class SpeechToTextApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Microphone Speech To Text (with PocketSphinx)')
        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.stt = microphone.SpeechToText()
        self.after(0, self.poll_stt)

    def poll_stt(self):
        res = self.stt.poll()
        if res is not None:
            self.text.configure(state="normal")
            self.text.insert("end", '%s \n' % res)
            self.text.configure(state="disabled")
            self.after(100, self.poll_stt)

if __name__ == "__main__":
    app = SpeechToTextApp()
    app.mainloop()

