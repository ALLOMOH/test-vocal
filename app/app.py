from  speech_recognition import Recognizer,Microphone  


recognizer = Recognizer()


#on enregistre le son

with Microphone() as source:
        
        print("Reglage du bruit ambiant... Patientez...")

        recognizer.adjust_for_ambient_noise(source)

        print("vous pouvez parlez")

        audio = recognizer.listen(source)
        
        print("Engrestrement Terminé!")

        with open('record.mp3','mp3') as f:
                f.write(audio.get_wav_data());

        # Reconnaissance de l'audio

        try:
                print("Reconnaissance du texte...")

                text = recognizer.recognize_google(
                        audio,
                        language="fr-FR"
                )

                print(f"Vous avez dir: {text}")
        except Exception as e:
                print(e)