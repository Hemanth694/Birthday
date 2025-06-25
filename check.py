import os
import re

# 1. Extract filenames from HTML
html_block = r"""
<img src="Photos\diet coke.jpg" alt="Photo 1" />
    <img src="Photos\cake.jpg" alt="Photo 2" />
    <img src="Photos\flowerclip.jpg" alt="Photo 3" />
    <img src="Photos\ldr.jpg" alt="Photo 4" />
    <img src="Photos\ravenclawcat.jpg" alt="Photo 5" />
    <img src="Photos\scotland.jpg" alt="Photo 6" />
    <img src="Photos\solar.jpg" alt="Photo 7" />
    <img src="Photos\tacos.jpg" alt="Photo 8" />
    <img src="Photos\lily.jpg" alt="Photo 9" />
    <img src="Photos\parkstreet.jpg" alt="Photo 10" />
    <img src="Photos\christmaskolkata.jpg" alt="Photo 11" />
    <img src="Photos\christmasscotland.jpg" alt="Photo 12" />
    <img src="Photos\purplily.jpg" alt="Photo 13" />
    <img src="Photos\gulabjamun.jpg" alt="Photo 14" />
    <img src="Photos\934.jpg" alt="Photo 15" />
    <img src="Photos\kkr.jpg" alt="Photo 16" />
    <img src="Photos\thali.jpg" alt="Photo 17" />
    <img src="Photos\momos.jpg" alt="Photo 18" />
    <img src="Photos\eduni.jpg" alt="Photo 19" />
    <img src="Photos\lol.jpg" alt="Photo 20" />
    <img src="Photos\papmovie.jpg" alt="Photo 21" />
    <img src="Photos\bts.jpg" alt="Photo 22" />
    <img src="Photos\ga.jpg" alt="Photo 23" />
    <img src="Photos\kitchen.jpg" alt="Photo 24" />
    <img src="Photos\coffee.jpg" alt="Photo 25" />
    <img src="Photos\mall.jpg" alt="Photo 26" />
    <img src="Photos\miniso.jpg" alt="Photo 27" />
    <img src="Photos\house.jpg" alt="Photo 28" />
    <img src="Photos\jhumka.jpg" alt="Photo 29" />
    <img src="Photos\ka.jpg" alt="Photo 30" />
    <img src="Photos\jane.jpg" alt="Photo 31" />
    <img src="Photos\saturn.jpg" alt="Photo 32" />
    <img src="Photos\moon.jpg" alt="Photo 33" />
    <img src="Photos\wowow.jpg" alt="Photo 34" />
    <img src="Photos\wlily.jpg" alt="Photo 35" />
    <img src="Photos\cherrycola.jpg" alt="Photo 36" />
    <img src="Photos\ysl.jpg" alt="Photo 37" />
    <img src="Photos\gavodka.jpg" alt="Photo 38" />
    <img src="Photos\movie.jpg" alt="Photo 39" />
    <img src="Photos\dove.jpg" alt="Photo 40" />
    <img src="Photos\pearlwatc.jpg" alt="Photo 41" />
    <img src="Photos\pearlcat.jpg" alt="Photo 39" />
    <img src="Photos\pearl.jpg" alt="Photo 42" />
    <img src="Photos\lily22.jpg" alt="Photo 43" />
    <img src="Photos\ssr.jpg" alt="Photo 44" />
    <img src="Photos\aww.jpg" alt="Photo 45" />
    <img src="Photos\ssr2.jpg" alt="Photo 46" />
    <img src="Photos\abouttime.jpg" alt="Photo 47" />
    <img src="Photos\before.jpg" alt="Photo 48" />
    <img src="Photos\hg.jpg" alt="Photo 49" />
    <img src="Photos\hg2.jpg" alt="Photo 50" />
    <img src="Photos\band.jpg" alt="Photo 51" />
    <img src="Photos\bandd.jpg" alt="Photo 52" />
    <img src="Photos\lol2.jpg" alt="Photo 53" />
    <img src="Photos\job.jpg" alt="Photo 54" />
    <img src="Photos\linkedin.jpg" alt="Photo 55" />
    <img src="Photos\damn.jpg" alt="Photo 56" />
    <img src="Photos\oh.jpg" alt="Photo 57" />
    <img src="Photos\sea.jpg" alt="Photo 58" />
    <img src="Photos\field.jpg" alt="Photo 59" />
    <img src="Photos\yummy.jpg" alt="Photo 60" />
    <img src="Photos\jalebi.jpg" alt="Photo 61" />
    <img src="Photos\aloo.jpg" alt="Photo 62" />
    <img src="Photos\corndog.jpg" alt="Photo 63" />
    <img src="Photos\friessalad.jpg" alt="Photo 64" />
    <img src="Photos\fries.jpg" alt="Photo 65" />
    <img src="Photos\chai.jpg" alt="Photo 66" />
    <img src="Photos\df.jpg" alt="Photo 67" />
    <img src="Photos\berry.jpg" alt="Photo 68" />
    <img src="Photos\honeymoon.jpg" alt="Photo 69" />
    <img src="Photos\rome.jpg" alt="Photo 70" />
    <img src="Photos\swan.jpg" alt="Photo 71" />
    <img src="Photos\watermelon.jpg" alt="Photo 72" />
    <img src="Photos\combo.jpg" alt="Photo 73" />
    <img src="Photos\rajma.jpg" alt="Photo 74" />
"""

html_files = re.findall(r'Photos\\(.*?)"', html_block)

# 2. Get actual filenames from the Photos folder
folder_path = 'Photos'  # Adjust this path if needed
actual_files = os.listdir(folder_path)

# 3. Normalize both lists
html_files = [f.strip().lower() for f in html_files]
actual_files = [f.strip().lower() for f in actual_files]

# 4. Compare
missing_from_html = sorted(set(actual_files) - set(html_files))
extra_in_html = sorted(set(html_files) - set(actual_files))

print("🟡 Missing in HTML:", missing_from_html)
print("🔴 Files listed in HTML but not found in folder:", extra_in_html)
print("📁 Total in folder:", len(actual_files))
print("📝 Total listed in HTML:", len(html_files))
