import fresh_tomatoes
import media

'''This is the driver class to actual create the moive list and render the moive trailer website.'''
'''All the moive storylines are from IMDB.com'''
#Create all the movie objects

socialnetwork = media.Movie("The Social Network",
                        "Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the cofounder who was later squeezed out of the business.",
                        "http://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                        "https://www.youtube.com/watch?v=lB95KLmpLR4")

whiplash = media.Movie("Whiplash",
                        "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
                        "http://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
                        "https://www.youtube.com/watch?v=7d_jQycdQGo")

boyhood = media.Movie("Boyhood",
                        "The life of Mason, from early childhood to his arrival at college.",
                        "http://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
                        "https://www.youtube.com/watch?v=IiDztHS3Wos")

skyfall = media.Movie("Skyfall",
                        "Bond's loyalty to M is tested when her past comes back to haunt her. Whilst MI6 comes under attack, 007 must track down and destroy the threat, no matter how personal the cost.",
                        "http://www.007.com/wp-content/uploads/2012/09/SKYFALL-UK-POSTER_650.jpg",
                        "https://www.youtube.com/watch?v=24mTIE4D9JM")

kingsman = media.Movie("Kingsman: The Secret Service",
                        "A spy organization recruits an unrefined, but promising street kid into the agency's ultra-competitive training program, just as a global threat emerges from a twisted tech genius.",
                        "http://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg",
                        "https://www.youtube.com/watch?v=kl8F-8tR8to")

birdman = media.Movie("Birdman",
                        "A washed-up actor, who once played an iconic superhero, battles his ego and attempts to recover his family, his career and himself in the days leading up to the opening of his Broadway play.",
                        "http://upload.wikimedia.org/wikipedia/en/a/a3/Birdman_poster.jpg",
                        "https://www.youtube.com/watch?v=8jAfBd3g6bA")


#Put all the movies in a movie list
movies = [socialnetwork, whiplash, boyhood, skyfall, kingsman, birdman]

#Use freash_tomatoes to render the website by giving the movie list
fresh_tomatoes.open_movies_page(movies)
