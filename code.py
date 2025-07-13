import os
import whisper

# Ruta principal donde están las carpetas de clase
base_folder = r"C:/Users/piter/OneDrive/Escritorio/UNI/8VO CICLO/SUSTIS/SIE/Audios"

# Cargar modelo de Whisper
model = whisper.load_model("base")

# Tipos de archivo de audio aceptados
audio_extensions = (".m4a", ".mp3", ".wav", ".flac")

# Recorrer todas las carpetas
for root, dirs, files in os.walk(base_folder):
    for file in files:
        if file.lower().endswith(audio_extensions):
            audio_path = os.path.join(root, file)
            txt_output = os.path.splitext(audio_path)[0] + ".txt"

            print(f"Transcribiendo: {audio_path}")

            try:
                result = model.transcribe(audio_path)
                with open(txt_output, "w", encoding="utf-8") as f:
                    f.write(result["text"])
                print(f"Guardado en: {txt_output}")
            except Exception as e:
                print(f"Error con {audio_path}: {e}")