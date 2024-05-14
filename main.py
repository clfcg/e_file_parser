import flet as ft

from utils.efile_stats import get_stats


def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    def view_stats(e):
        list_view_stats.controls.clear()
        stats = get_stats(selected_files.value)
        list_view_stats.controls.append(
            ft.Text(f"Кол-во актов: {stats['akt_count']}")
        )
        list_view_stats.controls.append(
            ft.Text(f"Кол-во записей: {stats['zap_count']}")
        )
        if 'err' in stats:
            list_view_stats.controls.append(
            ft.Text(f"Кол-во множ. актов с неоплатой: {stats['err']}")
        )
        else:
            list_view_stats.controls.append(
            ft.Text(f"Кол-во множ. актов с неоплатой: {stats['not_empty_akts']}")
        )
            list_view_stats.controls.append(
            ft.Text(f"Номера актов: {', '.join(stats['not_empty_akts_num'])}")
        )
        list_view_stats.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    # Путь до файла
    selected_files = ft.TextField(
        width=700
    )
    # Кнопка выбора файла
    pick_file_btn = ft.ElevatedButton(
        text='Выбрать файл',
        icon=ft.icons.SIM_CARD_DOWNLOAD_OUTLINED,
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=False
        )
    )
    # Слой вывода статистики
    list_view_stats = ft.ListView()
    # Кнопка вывода статистики
    view_stats_btn = ft.ElevatedButton(
        text='Статистика',
        on_click=view_stats
    )

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                selected_files,
                pick_file_btn
            ]
        ),
        list_view_stats,
        view_stats_btn
    )

ft.app(target=main)