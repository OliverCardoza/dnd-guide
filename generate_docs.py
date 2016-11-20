import CommonMark
import json
from collections import OrderedDict

ENTRY_PAGE_TEMPLATE = """<html>
<title>{title}</title>
<h1>{title}</h1>
{body}

<div>
  <a href="index.html">Home</a>
  <a href="entry_index.html">Index</a>
</div>
</html>"""

ENTRY_INDEX_TEMPLATE = """<html>
<title>Entry Index</title>
<h1>Entry Index</h1>
<ul>
{items}
</ul>

<div>
  <a href="index.html">Home</a>
  <a href="entry_index.html">Index</a>
</div>
</html>"""


def ConvertTitleToFilename(title):
  return title.lower().replace(" ", "_")


json_data = open("./data/part0_introduction.json").read()
index = {}
entries = json.loads(json_data)
for entry in entries:
  title = entry["title"]
  body = CommonMark.commonmark(entry["body"])
  filename = "{0}.html".format(ConvertTitleToFilename(title))
  filepath = "./docs/{0}".format(filename)
  index[title] = filename

  print("writing {0} to {1}...".format(title, filepath), end="")
  with open(filepath, "w") as entry_page:
    entry_page.write(ENTRY_PAGE_TEMPLATE.format(title=title, body=body))
  print("DONE")

print("writing entry index...", end="")
with open("./docs/entry_index.html", "w") as entry_index_page:
  items = ""
  ordered_index = OrderedDict(sorted(index.items(), key=lambda t: t[0].lower()))
  for title, filename in ordered_index.items():
    items += "<li><a href=\"{0}\">{1}</a></li>".format(filename, title)
  entry_index_page.write(ENTRY_INDEX_TEMPLATE.format(items=items))
print("DONE")
