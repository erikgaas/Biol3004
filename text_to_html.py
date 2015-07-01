from bs4 import BeautifulSoup

CURR_LANGUAGE = "bash"
finished_section = True

text_file = open("prog_tutorial2.txt", "r")


def starts_with(text, subtext):
	if text[0:len(subtext)] == subtext:
		return True
	else:
		return False

final_text = """<div class="container">"""
for line in text_file:
	line = line.replace("<", "&lt;")
	line = line.replace(">", "&gt;")
	if starts_with(line, "title:"):
		extra = ""
		if finished_section == False:
			extra = """</div></div>"""
		header = """<div class="row"><div class="col-md-12"><h4>"""
		ender = "</h4></div></div>"
		finished_section = True
		final_text = final_text + header + line[len("title:"):-1] + ender + extra
	elif starts_with(line, "code:"):
		extra = ""
		if finished_section == True: #make new paragraph area
			finished_section = False
			extra =  """<div class="row"><div class="col-md-12">"""
		header = """<pre><code class="language-"""+CURR_LANGUAGE+"""">"""
		ender = """</code></pre>"""
		final_text = final_text + extra + header + line[len("code:"):-1] + ender
	else:
		extra = ""
		if finished_section == True: #make new paragraph area
			finished_section = False
			extra =  """<div class="row"><div class="col-md-12">"""
		header = """<p>"""
		ender = """</p>"""
		final_text = final_text + extra + header + line + ender


final_text = final_text + """</div></div></div>"""

new_file = open("prog_tutorial2.html", "w")

soup = BeautifulSoup(final_text)

pretty_text = soup.prettify()

print(final_text)

new_file.write(pretty_text)

new_file.close()
text_file.close()