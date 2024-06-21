import feedparser

feed = feedparser.parse("https://hellocoding.de/feed.xml")
path = "./profile/"

def copyReadme():
  with open(path + "README.template.md", "r") as file:
    data = file.read()

    with open(path + "README.md", "w") as file:
      file.write(data + "\n")

def update():
  copyReadme()

  for entry in feed.entries:
    mdLink = f"- [{entry.title}]({entry.link})"

    with open(path + "README.md", "a") as file:
      file.write(mdLink + "\n")
    
if __name__ == "__main__":
  update()