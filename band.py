import media
import fresh_tomatoes


ken_mode = media.bands('ken mode','An awesome band','http://www.aux.tv/wp-content/uploads/2013/04/KEN-mode-win-a-Juno.jpg','https://www.youtube.com/watch?v=OeMAWgNskv0')

dillinger_escape_plan = media.bands('Dillinger Escape Plan','Extreme metal at the most Xtreme','http://diymag.com/media/img/Artists/D/Dillinger-Escape-Plan/_1500x1000_crop_center-center_75/dillinger-print.jpg','https://www.youtube.com/watch?v=WUP9E5jJrr4')

ourladypeace = media.bands('Our Lady Peace', 'wonders','https://en.wikipedia.org/wiki/File:OLP_2016.jpg','https://www.youtube.com/watch?v=TFBO7dx4Bes')
bandZ = [ken_mode,dillinger_escape_plan,ourladypeace]

fresh_tomatoes.open_movies_page(bandZ)
