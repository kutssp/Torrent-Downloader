
# 📥 Torrent & Magnet Downloader

**Torrent & Magnet Downloader** — это минималистичный Python-клиент для загрузки файлов по протоколу BitTorrent.  
Поддерживает работу как с **.torrent файлами**, так и с **magnet-ссылками**.

---

## 🚀 Возможности

- 📂 Загрузка по `.torrent` файлу  
- 🔗 Загрузка по `magnet:?` ссылке  
- 📊 Отображение скорости загрузки, прогресса и числа пиров  
- 💾 Автоматическое сохранение файлов в папку **Downloads**

---

## 🛠 Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/kutssp/torrent-downloader.git
   cd torrent-downloader
   ````

2. Установите зависимости:

   ```bash
   pip install python-libtorrent
   ```

   ⚠️ На некоторых системах пакет может называться `libtorrent` или `python3-libtorrent`.

---

## ▶️ Использование

1. Укажите путь к `.torrent` файлу **или** magnet-ссылку в коде:

   ```python
   # Пример с .torrent файлом
   torrent_path = os.path.expanduser("~/Desktop/example.torrent")
   download_torrent_or_magnet(torrent_path)

   # Пример с magnet-ссылкой
   magnet_link = "magnet:?xt=urn:btih:YOUR_MAGNET_HASH_HERE"
   download_torrent_or_magnet(magnet_link)
   ```

2. Запустите скрипт:

   ```bash
   python main.py
   ```

---

## 📊 Пример вывода

```
Загружаем по magnet-ссылке: magnet:?xt=urn:btih:...
Скачивание Ubuntu ISO начато...
Скорость: 512.34 kB/s | Прогресс: 32.56% | Пиры: 24
Скорость: 820.10 kB/s | Прогресс: 76.89% | Пиры: 41
✅ Скачивание завершено!
```

---

## ⚖️ Лицензия

Этот проект распространяется под лицензией **MIT**.
См. файл [LICENSE](LICENSE) для подробностей.

```
```
