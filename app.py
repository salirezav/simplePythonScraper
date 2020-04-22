# /usr/bin/python3
import bs4 as bs
import urllib.request

file1 = open("out.csv", "a")
url = "http://zipatlas.com/us/zip-code-comparison/population-density."
extension = ".html"
for i in range(1, 319):
    print("retrieving page: ", i)

    source = urllib.request.urlopen(
        url+str(i)+extension).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    table = soup.find("table", {"rules": "all"})
    tableRows = table.findChildren("tr")

    for row in tableRows:
        cols = row.findChildren("td")
        if cols[0].getText() == "#":
            continue

        output = "\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",%s\n" % (
            cols[0].getText(), cols[1].getText(), cols[2].getText(), cols[3].getText(), cols[4].getText(), cols[5].getText(), cols[6].getText())
        file1.write(output)
file1.close()
