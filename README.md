# MyZodiacMindSorter
Another personal hack. Basically allowing tagging on the zodiacmind.com site. The site lags tagging and it is very tiresome 
to find sun sign readings for your own sign. The Python Scripts read the images using PyTess, then based on the OCR readings,
categorizes them into the twelve sun signs.

I first used a Tumblr Downloader tool to download images off the tumblr blog, there were about 16000 images

Then I setup Tessearact library for Python

The first code I wrote was very basically and it read the text in the image and directly matched it with the name
of the sun sign. I realized that this method won't really give a nice output. I started with a test sample of about 
1000 images, then I studied the output according to the signs. There were patterns in them.

Like Sagittarius will sometimes have a '~' in between, so I generalized the regex for it as 'sa[a-z]{2,3}~([a-z]{4}us)?'

Similarly, Virgo would be '(v|w)[a-z]{2}o?o'

I also set up basic Hamming Distance code for the base Sun Signs. A Hamming distance of 1 resulted in corrected sorting and 
increased overall percentage significantly. 

So I ended up doing these three matches:

1. Basic Name Match
2. Hamming Distance of 1
3. Observed and Generalized Regexs


In the end, I had about 700 unsorted images, which would be roughly 6%. I was very happy to achieve an overall success of 94%


The unsorted images renditions are there in a file called out.txt

The main scripts are in finalRipperScript.py and finalBrutusScript.py

All other are Tesseract dependencies.
