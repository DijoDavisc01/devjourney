"""
social media post lst of list
"""
# media_post=[
#     [1,"good morning",200,100,120,"varun"],
#     [2,"good after noon",399,233,122,"vibin"],
#     [3,"good evening",123,235,237,"vineesh"],
#     [4,"good night",23,3576,234,"veera"]
# ]
# print(media_post[0][3])#100
# print(media_post[3][2])#23
# print(media_post[0][2])
# for lst in media_post:
#     print(lst[1])
# post=[lst[1]for lst in media_post]
# print(post)
# fb_veiw=[lst[2] for lst in media_post]
# print(fb_veiw)
# ig_view=[lst[3] for lst in media_post]
# print(ig_view)
# x_view=[lst[4] for lst in media_post]
# print(x_view)
# name=[lst[5] for lst in media_post]
# print(name)
# ig_like_fltr=[lst[1]for lst in media_post if lst[3]==233]
# print(ig_like_fltr)
# fb_like=[lst[1]for lst in media_post if lst[3]>100]
# print(fb_like)
# max_like_ig=max([lst[3]for lst in media_post])
# post=[lst[1]for lst in media_post if lst[3]==max_like_ig]
# print(post)
"""
movie dict
# display all movie title
# movie with top rating
# display kannada movies
# display movies whre actor is yash
# which language most number of movies
# movie with max budget
# languages
"""
# movies = [
#     [1, "K.G.F: Chapter 1", "Yash", "Kannada", 8.2, 1234567],
#     [2, "K.G.F: Chapter 2", "Yash", "Kannada", 8.3, 678900],
#     [3, "K.G.F: Chapter 3", "Yash", "Kannada", 9.5, 456789], # Anticipated
#     [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
#     [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], # Hype Rating
#     [6, "Aavesham", "Fahadh Faasil", "Telugu", 7.9, 1234567]
# ]
# all_movie=[lst[1] for lst in movies]
# print(all_movie)
# top_rating=max([lst[4]for lst in movies])
# movie_top_rating=[lst[1] for lst in movies if lst[4]==top_rating]
# print(movie_top_rating)
# kan_movies=[lst[1] for lst in movies if lst[3]=="Kannada"]
# print(kan_movies)
# yash_acted=[lst[1] for lst in movies if lst[2]=="Yash"]
# print(yash_acted)
# budget=max([lst[5]for lst in movies])
# movie_top_budget=[lst[1] for lst in movies if lst[5]==budget]
# print(movie_top_budget)
# langs = [lst[3] for lst in movies]
# lang_count = {lst: langs.count(lst) for lst in langs}
# lang=[[v,k]for k,v in lang_count.items()]
# print(sorted(lang,reverse=True))


"""
"""

# orders={"tea":15,"coffee":21,"dosa":34}
# orders_lst=[[k,v]for k,v in orders.items()]
# print(sorted(orders_lst,reverse=True))
# languages=["thamil","malayalam","kannada","telungu","kannada","telungu","thamil","malayalam","thamil","malayalam"]
# lang={ l:languages.count(l) for l in languages}
# langs=[[v,k]for k,v in lang]

"""

"""
# songs = [
#     {"id": 1, "title": "Mayajalam", "spotify_listen_count": 12000, "yt_music": 15000, "downloads": 5000},
#     {"id": 2, "title": "Neon Nights", "spotify_listen_count": 850000, "yt_music": 1200000, "downloads": 45000},
#     {"id": 3, "title": "Midnight Coffee", "spotify_listen_count": 45000, "yt_music": 32000, "downloads": 1200},
#     {"id": 4, "title": "Velvet Sky", "spotify_listen_count": 1200400, "yt_music": 980000, "downloads": 150000},
#     {"id": 5, "title": "Echoes of You", "spotify_listen_count": 3100, "yt_music": 4500, "downloads": 200},
#     {"id": 6, "title": "Rush Hour", "spotify_listen_count": 560000, "yt_music": 610000, "downloads": 88000},
#     {"id": 7, "title": "Quiet Storm", "spotify_listen_count": 150000, "yt_music": 145000, "downloads": 12000}
# ]
# titles=[di.get("title") for di in songs]
# # print(titles)
# downloads=[di.get("downloads")for di in songs]
# # print(downloads)
# downloads_max=max(downloads)
# song=[ di.get("title")for di in songs if di.get("downloads")==downloads_max]
# # print(song)
# yt=max([di.get("yt_music")for di in songs])
# song_max=[di.get("title")for di in songs if di.get("yt_music")==yt]
# # print(song_max)
"""

"""