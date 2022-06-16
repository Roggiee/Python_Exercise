import wordcloud
c=wordcloud.WordCloud()
c.generate("wordcloud by Python of Shenzhen Polytecnic")
c.to_file("wordcloud.png")