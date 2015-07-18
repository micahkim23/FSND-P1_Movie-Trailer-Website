import media
import fresh_tomatoes

# create 6 different instances of Movie objects to be used in webpage
the_interview = media.Movie(
    "The Interview",
    "Two TV hosts travel to North Korea to kill Kim Jong Un",
    "https://upload.wikimedia.org/wikipedia/en/2/27/The_Interview_2014_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=KpyVENBPj5c")
avengers = media.Movie(
    "Avengers Age of Ultron",
    "The Avengers have to defeat Ultron",
    "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",  # noqa
    "https://www.youtube.com/watch?v=JAUoeqvedMo")
t1_jump_street = media.Movie(
    "21 Jump Street",
    "Two undercover officers have to shut down a drug operation at a high school",  # noqa
    "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/21JumpStreetfilm.jpg/220px-21JumpStreetfilm.jpg",  # noqa
    "https://www.youtube.com/watch?v=RLoKtb4c4W0")
inside_out = media.Movie(
    "Inside Out", 
    "Meet the voices inside a young girl's head",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_(2015_film)_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=seMwpP0yeu4")
transformers_age_of_extinction = media.Movie(
    "Transformers Age of Extinction", 
    "The Autobots must defeat the Decepticons",
    "https://upload.wikimedia.org/wikipedia/en/9/94/Transformers_Age_of_Extinction_Poster.jpeg",  # noqa
    "https://www.youtube.com/watch?v=pbI980iUb78")
mockingjay = media.Movie(
    "Mockingjay", 
    "The capitol needs to be destroyed",
    "https://upload.wikimedia.org/wikipedia/en/6/63/MockingjayPart1Poster3.jpg",  # noqa
    "https://www.youtube.com/watch?v=3PkkHsuMrho")

# array of movies
movies = [the_interview, avengers, t1_jump_street, inside_out, transformers_age_of_extinction, mockingjay]  # noqa
# opens movie page with the array of movies
fresh_tomatoes.open_movies_page(movies)

