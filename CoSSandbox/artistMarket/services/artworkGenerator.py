from django.conf import settings

from ..models import ArtWork, ArtworkCollection
import datetime, random, requests, json, os

"""
Generate x number of Artworks entities

Artwork fields to generate:
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField()
    published_date = models.DateField(auto_now_add=True)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ManyToManyField(ArtworkCollection)
    image = models.ImageField(upload_to='uploads/images/', null=True)
"""

class ArtworkGenerator():
    def __init__(self, start_date, end_date, user):
        self.collections = ArtworkCollection.objects.all()
        self.start_date = start_date
        self.end_date = end_date
        self.user = user
        self.images = self.getImages()

    def getImages(self):
        image_path = 'uploads/images/'
        images = [
            'pigsfly.jpg',
            'whiteyford.jpg',
            'willie_dont_care.webp',
        ]

        return [image_path + image for image in images]

    def getRandomDate(self):
        date_range = self.start_date - self.end_date
        random_date = self.start_date + datetime.timedelta(days=random.randrange(date_range.days))
        
        return random_date

    def getTitle(self):
        resource_path = settings.BASE_DIR / 'artistMarket' / 'services' / 'resources'
        with open(resource_path / 'titles.json', 'r') as titlesFile:
            titlesJson = titlesFile.read()

        titles = json.loads(titlesJson)

        return random.choice(titles)

    def getDescription(self):
        paragraphs = str(random.randint(1,3))
        url = 'https://loripsum.net/api/' + paragraphs + '/short/plaintext'
        r = requests.get(url)

        return r.text

    def getCreatedDate(self):
        return self.getRandomDate()

    def getCollection(self):
        return random.choice(self.collections)
    
    def getImage(self):
        return random.choice(self.images)
    
    def getArtist(self):
        return self.user

    def makeArtwork(self):
        artwork = ArtWork()
        artwork.title = self.getTitle()
        artwork.description = self.getDescription()
        artwork.created_date = self.getCreatedDate()
        artwork.collection = self.getCollection()
        artwork.image.name = self.getImage()
        artwork.artist = self.user
        
        return artwork

    def generateArtworks(self, numArtworks):
        for i in range(numArtworks):
            artwork = self.makeArtwork()
            artwork.save()
