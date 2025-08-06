import json
import os
import random
import requests

# ----------------------------
# Task 1: JSON Parsing
# ----------------------------

def parse_students_json():
    filename = "students.json"
    if not os.path.exists(filename):
        print(f"{filename} not found.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        try:
            students = json.load(f)
            for i, student in enumerate(students, start=1):
                print(f"\nStudent {i}:")
                for key, value in student.items():
                    print(f"{key.capitalize()}: {value}")
        except json.JSONDecodeError:
            print("Invalid JSON format in file.")

# ----------------------------
# Task 2: Weather API
# ----------------------------

def fetch_weather(city="Tashkent"):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print(f"\nWeather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Weather: {data['weather'][0]['description']}")
        else:
            print("Error fetching weather:", data.get("message", "Unknown error"))
    except Exception as e:
        print("Request failed:", e)

# ----------------------------
# Task 3: JSON Modification
# ----------------------------

def manage_books():
    filename = "books.json"

    def load_books():
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except:
                    return []
        return []

    def save_books(books):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(books, f, indent=4, ensure_ascii=False)

    books = load_books()

    while True:
        print("\nBook Manager:")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Show All Books")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            books.append({"title": title, "author": author, "year": year})
            save_books(books)
            print("Book added.")

        elif choice == "2":
            title = input("Enter title to update: ")
            for book in books:
                if book["title"].lower() == title.lower():
                    book["author"] = input("New author: ")
                    book["year"] = input("New year: ")
                    save_books(books)
                    print("Book updated.")
                    break
            else:
                print("Book not found.")

        elif choice == "3":
            title = input("Enter title to delete: ")
            books = [book for book in books if book["title"].lower() != title.lower()]
            save_books(books)
            print("Book deleted if it existed.")

        elif choice == "4":
            print("\nCurrent books:")
            for book in books:
                print(f"{book['title']} by {book['author']} ({book['year']})")

        elif choice == "0":
            break
        else:
            print("Invalid choice.")

# ----------------------------
# Task 4: Movie Recommendation
# ----------------------------

def movie_recommendation():
    api_key = "YOUR_API_KEY"  # Replace with your OMDb API key
    genre = input("Enter movie genre (e.g., action, comedy): ").lower()

    # Sample movie titles per genre for demo (since OMDb doesn't support genre-based search directly)
    genre_movies = {
        "action": ["Mad Max: Fury Road", "Gladiator", "The Dark Knight"],
        "comedy": ["Superbad", "Step Brothers", "The Mask"],
        "drama": ["Forrest Gump", "The Shawshank Redemption", "Fight Club"],
        "sci-fi": ["Inception", "Interstellar", "The Matrix"],
        "romance": ["The Notebook", "Pride & Prejudice", "La La Land"]
    }

    if genre not in genre_movies:
        print("Genre not found in sample database.")
        return

    movie_title = random.choice(genre_movies[genre])
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        if data.get("Response") == "True":
            print(f"\nRecommended {genre.title()} Movie: {data['Title']}")
            print(f"Year: {data['Year']}")
            print(f"Genre: {data['Genre']}")
            print(f"Plot: {data['Plot']}")
            print(f"IMDB Rating: {data['imdbRating']}")
        else:
            print("Movie not found.")
    except Exception as e:
        print("Error fetching movie:", e)

# ----------------------------
# Menu to Run All Tasks
# ----------------------------

def main():
    while True:
        print("\n--- JSON/API Homework Tasks ---")
        print("1. JSON Parsing - students.json")
        print("2. Weather API - Tashkent")
        print("3. JSON Book Manager")
        print("4. Movie Recommendation System")
        print("0. Exit")

        choice = input("Choose a task (0-4): ")
        if choice == "1":
            parse_students_json()
        elif choice == "2":
            fetch_weather()
        elif choice == "3":
            manage_books()
        elif choice == "4":
            movie_recommendation()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
