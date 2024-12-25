import requests

def get_random_cat_image():
    """Функция для получения случайного изображения кошки с TheCatAPI."""
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data and "url" in data[0]:
                return data[0]["url"]
        return None
    except Exception as e:
        print(f"Ошибка при запросе: {e}")
        return None

def main():
    """Основная программа."""
    print("Получение случайного изображения кошки...")
    cat_image_url = get_random_cat_image()
    if cat_image_url:
        print(f"URL изображения кошки: {cat_image_url}")
    else:
        print("Не удалось получить изображение.")

if __name__ == "__main__":
    main()
