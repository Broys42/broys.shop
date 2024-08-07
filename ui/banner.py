import flet as ft
import asyncio
from ui.main_btn import MainButton

class Banner(ft.Stack):
    def __init__(self, page: ft.Page, video: ft.Video):
        super().__init__()
        self.video = video
        self.page = page
        self.height = self.page.height
        self.width = self.page.width
        self.alignment = ft.alignment.center

        self.title = ft.Text(
            value="Пусть музыка станет ближе",
            size=40,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL,
        )

        self.subtitle = ft.Text(
            value="Новая коллекция игровых наушников ниже!",
            size=20,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL
        )

        self.button = MainButton(button_text="Перейти к товару", width=300)

        #Stack dont support click event so button also plased in container
        self.container_for_button = ft.Container(
            content=self.button,
        )

        self.text_column = ft.Column(
            controls=[
            self.title,
            self.subtitle,
            ],
            spacing=-10,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.text_and_button_column = ft.Column(
            controls=[
            self.text_column,
            self.container_for_button
            ],
            spacing=40,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.container = ft.Container(
            content=self.text_and_button_column,
            alignment=ft.alignment.center
        )

        self.controls = [
            self.video,
            self.container,
        ]

        self.page.on_resized = self.page_on_resize

    def page_on_resize(self, e: ft.WindowResizeEvent):
        self.height = e.page.height
        self.width = e.page.width
        self.page.update()

#Test launch (python -m ui.banner)
if __name__ == "__main__":
    print("Сработал")
    from ui.video import Video
    import asyncio
    async def main(page: ft.Page):
        video = Video(page)
        banner = Banner(page, video)
        page.add(banner)
        video.add_video_in_playlist()
        page.update()
        await video.start_loop_play()
    app = asyncio.run(ft.app_async(main))
