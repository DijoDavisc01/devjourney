from csv import DictReader
fr=open("langauge_fundementels\\task\\operators\\readwrite\\move.csv")
data=list(DictReader(fr))
print(data)

"""
Write a Python program to read the file move.csv and print the first 5 rows
"""
# for r in data[:5]:
# print(r)
"""
2. Write a program to count how many movie records are present in move.csv (excluding the header).
"""
movie_count=[m.get("Name")for m in data]
# print(2 ,len(movie_count))
"""
3. Write a program to read the header row from move.csv and print all column names.
"""
"""
4. Accept a year from the user and display all movie titles released in that year from move.csv.
"""
# year=input("enter year:")
# movie_in_year=years=[m.get("Name")for m in data if year in  m.get("Year of Release") ]
# print(4 ,movie_in_year)
"""
5. Read move.csv and print the movie with the highest rating.
"""
max_rating=max([m. get("Rating")for m in data])
movie_high_rating=[m.get("Name") for m in data if m.get("Rating")==max_rating]
# print(5 ,movie_high_rating)
"""
6. Accept a genre from the user (e.g., Action, Drama, Romance) and print all matching movies from move.csv.
"""
# movie_type=input("enter movie type:")
# movie_by_catogery=[m.get("Name")for m in data if movie_type in m.get("Movie Categories")]
# print(6 ,movie_by_catogery)
"""
7. Create a new CSV file named top_rated.csv and write all movies from move.csv with a rating greater than 8.0.
"""

fw=open("langauge_fundementels\\task\\operators\\readwrite\\top_rated.csv","w")
for m in data:
    max_rating=max(m.get("Rating"))
    if m.get("Rating")==max_rating:
        fw.write(m+"\n")
    