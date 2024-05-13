import flet as ft


def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.TextField(
        width=700
    )
    pick_file_btn = ft.ElevatedButton(
        text='Выбрать файл',
        icon=ft.icons.SIM_CARD_DOWNLOAD_OUTLINED,
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=False
        )
    )

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                selected_files,
                pick_file_btn
            ]
        )
    )

ft.app(target=main)