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


def demonstrate_stage_3(movies):
    print("Фильмы без жанра comedy:")
    print_non_comedy_movies(movies)

    print("\nПоиск шедевра:")
    find_masterpiece(movies)

    movies_without_masterpieces = [movie for movie in movies if movie["rating"] <= 9.0]

    print("\nПоиск в каталоге без шедевров:")
    find_masterpiece(movies_without_masterpieces)

    print("\nФильмов длиннее 120 минут:", count_long_movies(movies))


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


def count_by_genre(movies):
    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts


def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, [])
            filmography[actor].append(movie["title"])

    return filmography


def movies_above_average(movies):
    avg_rating = average_rating(movies)

    high_rated = {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > avg_rating
    }

    return high_rated


def all_genres(movies):
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres


def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])

    return actors1 & actors2


def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    return genres_a - genres_b


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def demonstrate_stage_8(movies):
    print("Фильмы с рейтингом не ниже 8.0:")

    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

    total_duration = sum(
        movie["duration_min"] for movie in movies if movie["rating"] > 7
    )

    print("\nСуммарная длительность фильмов с рейтингом выше 7:")
    print(total_duration, "минут")


def build_report(movies):
    print("ОТЧЁТ ПО КАТАЛОГУ")

    avg_rating = average_rating(movies)
    avg_age = catalog_age_stats(movies)[2]

    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет")

    print("\nТоп-3 фильма:")

    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    for movie in sorted_movies[:3]:
        print(f"  {format_report_line(movie)}")

    print("\nФильмов по жанрам:")

    genre_counts = count_by_genre(movies)

    sorted_genres = sorted(
        genre_counts.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")

    genres = all_genres(movies)
    genres_text = ", ".join(sorted(genres))

    print(f"\nВсе жанры каталога: {genres_text}")


if __name__ == "__main__":
    build_report(movies)
