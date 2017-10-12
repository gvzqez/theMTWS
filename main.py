import media_center
import webbrowser
import os
import re



# -------------------------------------------------- HTML -------------------------------------------------- #

# Styles and scripting for the webpage
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>The MTWS</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background: #f4f4f4;
            font-family: 'Oswald', sans-serif;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .media-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .media-tile:hover {
            background-color: white;
            cursor: pointer;
            opacity: 0.8;
            border-radius: 15px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .icon {
            font-family: 'Material Icons';
        }
        .arrow-icon {
            position: absolute;
            left: -60px;
            width: 40px;
            height: 40px;
            top: calc(50% - 20px);
            font-size: 40px;
            line-height: 40px;
        }
        .arrow-icon.right {
            left: auto;
            right: -60px;
            width: 40px;
            height: 40px;
            top: calc(50% - 20px);
            font-size: 40px;
        }
        .navbar {
            background: #000000;
            height; 200px;
        }
        .navbar-brand img {
            width: 400px;
            height: auto;
            margin-bottom: 20px;
            position: fixed;
            top: -20px;
            left: -50px;
        }
        .container {
            width: 80%;
            margin-bottom: 120px;
        }
        .media-group .row {
            overflow-x: auto;
            white-space: nowrap;
        }
        .media-group .row > .col-xs-6 {
            display: inline-block;
            float: none;
        }
        .media-group img {
            width: 100%;
            height: 100%;
        }
        .media-group hr {
            border-top: 2px solid white;
            margin-bottom: 40px;
        }
        .media-group h3 {
            h3: font-weight: bold;
        }
        .media-list {
            position: relative;
        }
        .media-title h4 {
            height: 30px;
            white-space: initial;
            color: black;
        }
        .rating {
            width: 30px;
            height: 30px;
            position: absolute;
            top: 30px;
            right: 25px;
            background: rgba(0, 0, 0, 0.7);
            color: yellow;
            border-radius: 100px;
            font-size: 14px;
            font-weight: bold;
            line-height: 30px;
            box-shadow: 0 0 0 2px white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.media-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container"></div>
          <div id="media-modal-info"></div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <a class="navbar-brand" href="#">
              <img src="logo.png" alt="TheMTWB logo">
          </a>
        </div>
      </div>
    </div>
    <div class="container media-group">
      <div class="row movie-head">
        <h3>On Theatres</h3>
      </div>
      <div class="text-center media-list">
        <div class="icon arrow-icon">keyboard_arrow_left</div>
        <div class="icon arrow-icon right">keyboard_arrow_right</div>
        <div class="movie-group row">
          {nowplaying_tiles}
        </div>
      </div>
      <hr>
      <div class="row media-head">
        <h3>Coming Soon</h3>
      </div>
      <div class="text-center media-list">
        <div class="icon arrow-icon">keyboard_arrow_left</div>
        <div class="icon arrow-icon right">keyboard_arrow_right</div>
        <div class="serie-group row">
          {upcoming_tiles}
        </div>
      </div>
      <hr>
      <div class="row media-head">
        <h3>Modern Classics</h3>
      </div>
      <div class="text-center media-list">
        <div class="icon arrow-icon">keyboard_arrow_left</div>
        <div class="icon arrow-icon right">keyboard_arrow_right</div>
        <div class="anime-group row">
          {modern_tiles}
        </div>
      </div>
      <hr>
      <div class="row media-head">
        <h3>Classics</h3>
      </div>  
      <div class="text-center media-list">
        <div class="icon arrow-icon">keyboard_arrow_left</div>
        <div class="icon arrow-icon right">keyboard_arrow_right</div>
        <div class="anime-group row">
          {classic_tiles}
        </div>
      </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
media_tile_content = '''
<div class="col-xs-6 col-sm-5 col-md-3 col-lg-2 media-tile movie-cover text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="rating">{media_rating}</div>
    <img src="{poster_image_url}">
    <div class="row media-title">
      <div class="col-md-12 text-center">
        <h4><b>{media_title}</b></h4>
      </div>
    </div>
</div>
'''



# ----------------------------------------------- PROCEDURES ----------------------------------------------- #

# Create HTML content for each movie section
def create_media_tiles_content(media):
    content = ''
    for m in media:
        # Avoid error in case youtube trailer is not available
        if m.trailer_youtube_url is not None:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', m.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', m.trailer_youtube_url)
            trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)

            # Append the tile for the movie with its content filled in
            content += media_tile_content.format(
                media_title=m.title,
                poster_image_url=m.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                media_rating=m.rating
                )
        else:
            content += media_tile_content.format(
                media_title=m.title,
                poster_image_url=m.poster_image_url,
                trailer_youtube_id='',
                media_rating=m.rating
                )

    return content


# Generate or overwrite the output file
def open_movies_page(nowplaying, upcoming, classics, moderns):
    output_file = open('theMTWS.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        nowplaying_tiles=create_media_tiles_content(nowplaying),
        upcoming_tiles=create_media_tiles_content(upcoming),
        classic_tiles=create_media_tiles_content(classics),
        modern_tiles=create_media_tiles_content(moderns),
        )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # Open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)



open_movies_page(media_center.now_playing, media_center.coming_soon, media_center.classics, media_center.modern_classics)

