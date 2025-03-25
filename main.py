
import yt_dlp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class DownloadApp(App):
    def build(self):
        self.title = "YouTube Downloader"
        
        # Layout simples
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Título
        title_label = Label(text="Baixar Vídeo do YouTube", font_size=24)
        layout.add_widget(title_label)

        # Campo de URL
        self.url_input = TextInput(hint_text="Cole a URL do YouTube", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.url_input)

        # Botão para iniciar o download
        download_button = Button(text="Baixar Vídeo", on_press=self.start_download, size_hint_y=None, height=50)
        layout.add_widget(download_button)

        # Label de status
        self.status_label = Label(text="Digite uma URL e clique para baixar.")
        layout.add_widget(self.status_label)

        return layout

    def start_download(self, instance):
        video_url = self.url_input.text.strip()
        if not video_url:
            self.status_label.text = "❌ URL inválida!"
            return

        self.status_label.text = "🔄 Baixando..."
        
        # Chama a função de download
        self.download_video(video_url)

    def download_video(self, url):
        ydl_opts = {
            'format': 'best[ext=mp4]',  # Baixar o melhor formato MP4 disponível (vídeo + áudio)
            'outtmpl': '%(title)s.%(ext)s',  # Salva o vídeo com o título correto
            'quiet': False,  # Mostra o processo no console
            'no_warnings': True,
            'ignoreerrors': True,
            'merge_output_format': 'mp4',  # Garante que o arquivo final seja MP4
        }
        
        try:
            # Fazendo o download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)  # Faz o download de fato
                if not info:
                    self.status_label.text = "❌ Vídeo não encontrado ou não disponível"
                    return

                self.status_label.text = f"✅ Baixado: {info['title']}"

        except Exception as e:
            self.status_label.text = f"❌ Err
o: {str(e)}"

if __name__ == "__main__":
    DownloadApp().run()
