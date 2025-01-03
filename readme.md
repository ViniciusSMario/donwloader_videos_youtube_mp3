# Baixador de Áudio do YouTube

Este é um projeto simples em Python que permite baixar o áudio de vídeos do YouTube diretamente no formato MP3, com uma interface gráfica amigável criada usando Tkinter.

## Funcionalidades
- Inserção da URL do vídeo do YouTube para download.
- Seleção da pasta de destino para salvar o arquivo MP3.
- Download automático do áudio no formato MP3.
- Mensagens de erro ou sucesso exibidas em pop-ups.

## Requisitos

### Dependências do Python
- Python 3.7 ou superior.
- Módulos necessários:
  - `yt-dlp`
  - `tkinter`

### Instalação das Dependências
Certifique-se de instalar o módulo `yt-dlp` antes de executar o projeto:
```bash
pip install yt-dlp
```
O módulo `tkinter` é embutido na maioria das instalações do Python. Caso não esteja presente, consulte a documentação do seu sistema operacional para instalá-lo.

## Como Usar
1. Clone ou baixe este repositório.
2. Execute o arquivo principal do projeto:
   ```bash
   python nome_do_arquivo.py
   ```
3. Insira a URL do vídeo do YouTube no campo indicado.
4. Clique em **Selecionar** para escolher a pasta onde o áudio será salvo.
5. Clique em **Baixar Áudio** para iniciar o download.
6. Uma mensagem de sucesso ou erro será exibida ao final do processo.

## Estrutura do Projeto
```
baixador-audio-youtube/
├── youtube_audio_gui.py   # Script principal do projeto
├── README.md              # Documentação do projeto
```

## Captura de Tela
Adicione aqui uma captura de tela do projeto para mostrar a interface gráfica.

## Recursos Utilizados
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Biblioteca para download de áudio/vídeo do YouTube.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Biblioteca embutida no Python para criação de interfaces gráficas.

## Limitações Conhecidas
- Este projeto não inclui suporte para conversão de formatos de áudio diferentes do MP3.
- O funcionamento depende da disponibilidade da ferramenta `yt-dlp` e de acesso à internet.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas no repositório.

## Licença
Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

