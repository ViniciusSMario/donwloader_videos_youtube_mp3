import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

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
        messagebox.showinfo("Sucesso", "Download concluído!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entrada_pasta.delete(0, tk.END)
        entrada_pasta.insert(0, pasta)

def iniciar_download():
    url = entrada_url.get()
    pasta_destino = entrada_pasta.get()

    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira a URL do vídeo do YouTube.")
        return

    if not pasta_destino:
        messagebox.showwarning("Aviso", "Por favor, selecione a pasta de destino.")
        return

    baixar_youtube_para_audio(url, pasta_destino)

# Criação da janela principal
janela = tk.Tk()
janela.title("Baixador de Áudio do YouTube")
janela.geometry("1000x400")

# Rótulo e entrada para a URL
tk.Label(janela, text="URL do vídeo do YouTube:").pack(pady=5)
entrada_url = tk.Entry(janela, width=60)
entrada_url.pack(pady=5)

# Rótulo e entrada para a pasta
tk.Label(janela, text="Pasta de destino:").pack(pady=5)
frame_pasta = tk.Frame(janela)
frame_pasta.pack(pady=5)

entrada_pasta = tk.Entry(frame_pasta, width=45)
entrada_pasta.pack(side=tk.LEFT)
btn_selecionar_pasta = tk.Button(frame_pasta, text="Selecionar", command=selecionar_pasta)
btn_selecionar_pasta.pack(side=tk.LEFT, padx=5)

# Botão para iniciar o download
btn_download = tk.Button(janela, text="Baixar Áudio", command=iniciar_download)
btn_download.pack(pady=20)

# Iniciar a interface
janela.mainloop()
