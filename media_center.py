import media
# Visit https://github.com/wagnerrp/pytmdb3 for more info
from tmdb3 import set_key
from tmdb3 import set_cache
from tmdb3 import set_locale
from tmdb3 import List


# Set personal key to API access
set_key('0ba74440350bf374cee4a9b89f7249a8')

# Caches data to limit excessive usage against API server
set_cache('null')
set_cache(filename='/full/path/to/cache')
set_cache(filename='tmdb3.cfrom random import randintache')
set_cache(engine='file', filename='~/.tmdb3cache')

# Set language and country configuration for API data
set_locale('en', 'us')


now_playing = []
coming_soon = []
modern_classics = []
classics = []


for x in range(0, len(List(35555).members)):
    media_title = List(35555).members[x].title.replace(' ', '_')
    media_title = media.Media(
        List(35555).members[x].title,
        List(35555).members[x].poster.geturl().replace(
            'original', 'w300_and_h450_bestv2'),
        List(35555).members[x].youtube_trailers[0].geturl(),
        List(35555).members[x].userrating
        )

    now_playing.append(media_title)


for y in range(0, len(List(35556).members)):
    media_title = List(35556).members[y].title.replace(' ', '_')
    media_title = media.Media(
        List(35556).members[y].title,
        List(35556).members[y].poster.geturl().replace(
            'original', 'w300_and_h450_bestv2'),
        List(35556).members[y].youtube_trailers[0].geturl(),
        List(35556).members[y].userrating
        )

    coming_soon.append(media_title)


for x in range(0, len(List(35558).members)):
    media_title = List(35558).members[x].title.replace(' ', '_')
    media_title = media.Media(
        List(35558).members[x].title,
        List(35558).members[x].poster.geturl().replace(
            'original', 'w300_and_h450_bestv2'),
        List(35558).members[x].youtube_trailers[0].geturl(),
        List(35558).members[x].userrating
        )

    modern_classics.append(media_title)


for k in range(0, len(List(35557).members)):
    media_title = List(35557).members[k].title.replace(' ', '_')
    media_title = media.Media(
        List(35557).members[k].title,
        List(35557).members[k].poster.geturl().replace(
            'original', 'w300_and_h450_bestv2'),
        List(35557).members[k].youtube_trailers[0].geturl(),
        List(35557).members[k].userrating
        )

    classics.append(media_title)
