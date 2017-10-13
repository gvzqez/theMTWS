# theMTWS
First project of Udacity's Full Stack Web Developer Nanodegree.

It consist on a python generated html responsive webpage that allows visitors to review movies' trailers and ratings for different movie sections. The movie data is provided through **themoviedb.org** API using the python library **pytmdb3**. (See documentation: https://github.com/wagnerrp/pytmdb3)
<br />
<br />
#### Note:
API requests are limited to 30 within 10 seconds, so the first time the programme is executed, it will take a few more time before the page is displayed. Then, the data is stored in the local cache for one hour.
<br />
<br />
## How to open the Movie Trailer Website
The only requirement is to have **Python 2.7** installed. If you don't have python installed, download the most recent release for 2.7 version on https://www.python.org/downloads/. When you are ready, follow the instructions:
<br />
1. Open terminal
2. Move to the choosen directory. Example: ```$ cd Desktop```
3. Clone the project repository ```$ git clone https://github.com/gvzqez/theMTWS```
4. Move to the project root directory ```$ cd theMTWS```
5. Set the "locale" environtment variables to **('en_US', 'UTF-8')**:
> ```$ export LC_ALL=en_US.UTF-8```
> ```$ export LANG=en_US.UTF-8```
6. Execute the main python script ```$ python main.py```

