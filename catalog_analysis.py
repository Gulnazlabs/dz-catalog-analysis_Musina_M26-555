import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    total_rating = 0

    for movie in movies:
        total_rating += movie["rating"]

    average = total_rating / len(movies)
    return round(average, 1)


def catalog_age_stats(movies, current_year=2026):
    ages = []

    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)

    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))

    return (oldest, newest, average_age)


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue

        print(movie["title"])


def find_masterpiece(movies):
    index = 0

    while index < len(movies):
        movie = movies[index]

        if movie["rating"] > 9.0:
            print("Найден шедевр:", movie["title"])
            break

        index += 1

    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count


def normalize_title(title):
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_word = word[0].upper() + word[1:].lower()
        normalized_words.append(normalized_word)

    return " ".join(normalized_words)


def make_slug(title):
    normalized = normalize_title(title)
    slug = normalized.lower().replace(" ", "-")
    return slug


def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])

    genres = sorted(movie["genres"])
    genres_text = ", ".join(genres)

    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres_text}'


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

    titles = []

    for movie in sorted_movies:
        titles.append(movie["title"])

    return titles


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    top_movies = []

    for movie in sorted_movies[:n]:
        top_movies.append((movie["title"], movie["rating"]))

    return top_movies


print("Средний рейтинг:", average_rating(movies))
print("Возраст фильмов:", catalog_age_stats(movies))
print("Продолжительность фильма:", duration_in_hours(155))

print("Рейтинг 9.0:", rating_tier(9.0))
print("Рейтинг 7.0:", rating_tier(7.0))
print("Рейтинг 5.0:", rating_tier(5.0))
print("Рейтинг 4.9:", rating_tier(4.9))

print("Фильм 2021 года:", decade_label(2021))
print("Фильм 2020 года:", decade_label(2020))
print("Фильм 2015 года:", decade_label(2015))
print("Фильм 2014 года:", decade_label(2014))

print("Фильмы без жанра comedy:")
print_non_comedy_movies(movies)

print("Поиск шедевра:")
find_masterpiece(movies)


# Проверяем случай, когда шедевров нет
movies_without_masterpieces = [movie for movie in movies if movie["rating"] <= 9.0]

print("Поиск в каталоге без шедевров:")
find_masterpiece(movies_without_masterpieces)

print("Фильмов длиннее 120 минут:", count_long_movies(movies))
print("Фильмов длиннее 150 минут:", count_long_movies(movies, 150))
print("Фильмов длиннее 200 минут:", count_long_movies(movies, 200))

print("Нормализация названий:")
print(normalize_title("silent hours"))
print(normalize_title("midnight in oslo"))
print(normalize_title("THE QUIET ALGORITHM"))

print("Проверка slug:")
print(make_slug("The Quiet Algorithm"))
print(make_slug("silent hours"))
print(make_slug("midnight in oslo"))

print("Отчёт по фильму:")
print(format_report_line(movies[7]))

print("Фильмы по убыванию рейтинга:")

result = titles_sorted_by_rating(movies)

for title in result:
    print(title)

print("Топ-3 фильмов:")
print(top_n_by_rating(movies))

print("Топ-5 фильмов:")
print(top_n_by_rating(movies, 5))

original_movies = movies.copy()

titles_sorted_by_rating(movies)

print("Исходный список не изменился:", movies == original_movies)
