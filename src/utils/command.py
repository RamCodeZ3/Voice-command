import speech_recognition as sr
import subprocess
import re 
import shutil

class CommandVoice:
    def __init__(self):
        self.r = sr.Recognizer()
        self.text = None
        self.listenVoice()

    def listenVoice(self):
         with sr.Microphone() as source:
            print('Puedes hablar')
            while True:
                print('-------------------')
                audio = self.r.listen(source)

                try:
                    self.text = self.r.recognize_google(audio, language="es-ES")
                    print(self.text)
                    if self.text == 'cerrar': break
                    
                    elif self.text.startswith('Open') or self.text.startswith('open'):
                        file_name = re.sub("open ", "", self.text.lower())
                        self.open_file(file_name)
  
                except sr.UnknownValueError:
                     print("No se entendio el audio")
                
                except Exception as e:
                    print('Hubo un error: ', e)
    
    def open_file(self, name):
         file_path = shutil.which(name)
         print(name)
         if file_path:
            print("file_path")
            subprocess.run([
                "powershell",
                "Start-Process",
                r"'{}'".format(file_path),
                "-Verb RunAs"
            ])
         else: print('No se encontro la ruta del archivo')
    