class News:
    '''
    News class to define the properties of News objects
    '''

    def __init__(self, id, name, author, title, description, url,urlToImage, publishedAt, content):
        self.id = id
        self.name =name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = 'https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200' + urlToImage
        self.publishedAt = publishedAt
        self.content = content