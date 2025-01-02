import subprocess

def baixar_youtube_para_audio(url, pasta_destino):
    try:
        comando = [
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--output", f"{pasta_destino}/%(title)s.%(ext)s",
            url
        ]
        
        print("Baixando e extraindo áudio do vídeo...")
        subprocess.run(comando, check=True)
        print("Download concluído!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

url = input("Digite a URL do vídeo do YouTube: ")
pasta_destino = input("Digite a pasta onde deseja salvar o arquivo (ou deixe vazio para salvar no diretório atual): ") or "."
baixar_youtube_para_audio(url, pasta_destino)
