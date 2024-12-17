import libtorrent as lt
import time
import os

def download_torrent():
    # Указываем путь к файлу .torrent на рабочем столе
    desktop_path = os.path.expanduser("~/Desktop")
    torrent_file = os.path.join(desktop_path, "example.torrent")  # Замените 'example.torrent' на имя вашего файла

    # Проверяем существование файла
    if not os.path.exists(torrent_file):
        print("Файл .torrent не найден на рабочем столе!")
        return

    # Настройка сессии
    session = lt.session()
    session.listen_on(6881, 6891)

    # Читаем .torrent файл
    info = lt.torrent_info(torrent_file)
    params = {
        "save_path": os.path.expanduser("~/Downloads"),  # Скачивает в папку "Загрузки"
        "storage_mode": lt.storage_mode_t.storage_mode_sparse,
        "ti": info,
    }
    handle = session.add_torrent(params)

    print(f"Скачивание {handle.name()} начато...")

    # Ожидание завершения загрузки
    while not handle.is_seed():
        status = handle.status()
        print(
            f"Скорость: {status.download_rate / 1000:.2f} kB/s | Прогресс: {status.progress * 100:.2f}%"
        )
        time.sleep(1)

    print("Скачивание завершено!")

if __name__ == "__main__":
    download_torrent()
