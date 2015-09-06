import markdown
import os
import re
import sys
from bs4 import BeautifulSoup as bs
import shutil


banner_content_template =  """<div class="row main-content">
<div class="col-md-2 col-sm-2 hidden-xs">
  <a href="programming{0}"><img class="img-responsive" src="img/{1}" alt="{1}"></a>
</div>
<div class="col-md-6 col-sm-6 col-xs-12">
  <h3 class="button-align"><a href="programming{0}">{2}</a></h3>
  <p>{3}</p>
</div>
</div>"""




class MarkDownLesson:
	"""param_dict holds the parameters"""

	def __init__(self, file_name):
		f = open("Lesson-Markdowns/" + file_name, "r")
		param_dict = {"index": None,
		"banner_description": None,
		"banner_title": None, 
		"banner_img": None,
		"default_code":None}

		while None in param_dict.values():
			curr_line = f.readline()
			if '#' in curr_line:
				print("Not enough parameters supplied.")
				sys.exit(0)
			else:
				key_value = curr_line.split(":")
				key_value = list( map(lambda x: x.strip(" \n"), key_value) )
				if key_value[0] not in param_dict:
					print("Warning! Unknown parameter " + key_value[0])
				else:
					param_dict[key_value[0]] = key_value[1]

		content = f.read()
		f.close()
		content = markdown.markdown(unicode(content, "utf-8"))
		self.param_dict = param_dict
		self.content = content
		for k, v in param_dict.items():
			setattr(self, k, v)

#Get every mardown file

#Insert custom styling.

markdowns = []
banner_html = []

all_files = os.listdir('Lesson-Markdowns')
all_files = filter(lambda x: ".md" in x, all_files)

for file_name in all_files:
	markdowns.append(MarkDownLesson(file_name))

markdowns.sort(key=lambda x: x.param_dict["index"])


for md in markdowns:

	# Custom styling here
	soup = bs(md.content, "html.parser")
	code_blocks = soup.find_all("code")
	for code in code_blocks:
		code["class"] = "language-" + md.default_code
	img_blocks = soup.find_all("img")
	for img in img_blocks:
		img["class"] = "img-responsive"

	#bring the code over to the website
	jinja_tag = """{%% extends 'same-content.html' %%}
{%% block article_content %%}
%s
{%% endblock %%}
	"""
	end_html = jinja_tag % soup.prettify().encode("utf8")
	end_file = open("metagenomics3004/templates/programming" + md.index + ".html", "w")
	end_file.write(end_html)
	end_file.close()


	#Add the testing tag
	# test_tag = """<meta charset=utf-8>\n"""
	# test_html = open("Test-HTML/programming" + md.index +".html", "w")
	# test_html.write(test_tag +  soup.prettify().encode("utf8"))

	# Create all of the banners
	# Order of params: index, img, title, description
	banner_tuple = (md.index, md.banner_img, md.banner_title, md.banner_description)
	banner_html.append(banner_content_template.format(*banner_tuple))


#Create information banner
all_banners = "\n".join(banner_html)

jinja_banner ="""{%% extends 'programming-content.html' %%}
{%% block banner_content %%}
%s
{%% endblock %%}
"""
end_banner = jinja_banner % all_banners
r_banner = open("metagenomics3004/templates/programming-banners.html", "w")
r_banner.write(end_banner)
r_banner.close()

# test_banner = all_banners.replace('src="img', 'src="../images')
# f_tbanner = open("Test-Banner/banners.html", "w")
# f_tbanner.write(test_banner)
# f_tbanner.close()




#Copy all images over
#Manually copy over in windows because windows is stupid
images = os.listdir("images")
for file_name in images:
	full_file_name = os.path.join("images", file_name)
	if (os.path.isfile(full_file_name)):
		shutil.copy(full_file_name, "metagenomics3004/img")
