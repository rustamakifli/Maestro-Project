from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from core.utils import tools

User = get_user_model()

SERVICE_TYPE = (
    ('hourly','Hourly Price'),
    ('standart', 'Standart Price'),
)   

INPUT_CHOICES = (
    ('Radio','Radio'),
    ('Checkbox', 'Checkbox'),
    ('Input', 'Input'),
)

STATUS_CHOICES = (
    ('new','New'),
    ('accepted', 'Accepted'),
    ('progress','Progress'),
    ('completed','Completed'),
    ('closed','Closed'),
)
REGION = [
    ("absheron", "Absheron"), ("agjabadi", "Aghjabadi"), 
    ("agdam", "Agdam"), ("agdash", "Agdash"), ("agsu", "Agsu"),
    ("shirvan", "Shirvan"), ("astara", "Astara"), ("baku", "Baku"),
    ("balakan", "Balakan"), ("barda", "Barda"), ("beylagan", "Beylagan"),
    ("bilasuvar", "Bilasuvar"), ("jabrayil", "Jabrayil"),
    ("jalilabad", "Jalilabad"), ("dashkasan", "Dashkasan"),
    ("shabran", "Shabran"), ("fuzuli", "Fuzuli"), ("gadabay", "Gadabay"), 
    ("ganja", "Ganja"), ("goranboy", "Goranboy"), ("goychay", "Goychay"), 
    ("hajigabul", "Hajigabul"), ("imishli", "Imishli"), ("ismayilli", "Ismayilli"),
    ("kalbajar", "Kalbajar"), ("kurdamir", "Kurdamir"), ("lachin", "Lachin"),
    ("lankaran", "Lankaran"), ("lerik", "Lerik"), ("masally", "Masally"),
    ("mingachevir", "Mingachevir"), ("naftalan", "Naftalan"), 
    ("neftchala", "Neftchala"), ("oguz", "Oghuz"), ("qabala", "Qabala"), 
    ("qakh", "Qakh"), ("gobustan", "Gobustan"), ("quba", "Quba"), 
    ("qubadli", "Qubadli"), ("qusar", "Qusar"), ("saatly", "Saatly"), 
    ("sabirabad", "Sabirabad"), ("shaki", "Shaki"), ("salyan", "Salyan"),
    ("shamakhi", "Shamakhi"), ("shamkir", "Shamkir"), ("samukh", "Samukh"), 
    ("siyazan", "Siyazan"), ("sumqayit", "Sumqayit"), ("shusha", "Shusha"), 
    ("tovuz", "Tovuz"), ("ujar", "Ujar"), ("khankendi", "Khankendi"),
    ("goygol", "Goygol"), ("khizi", "Khizi"), ("khojaly", "Khojaly"),
    ("khojavend", "Khojavend"), ("yardimli", "Yardimli"), ("yevlakh", "Yevlakh"),
    ("zaqatala", "Zaqatala"), ("zardab", "Zardab")
    ]

# Create your models here.
class City(models.Model):

    name = models.CharField(max_length=50,choices=REGION)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
    
class Blog(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, verbose_name="user_blog", on_delete=models.CASCADE)
    description = RichTextField()
    image = models.ImageField(upload_to=tools.get_blogs_image)
    is_active = models.BooleanField(default=True)

    # moderation
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title
    
class Service(models.Model):
    
    title = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to=tools.get_services_image)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    # moderation
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title

class AltServices(models.Model):
    service = models.ForeignKey(Service, verbose_name="service", related_name='sub_services', on_delete=models.CASCADE) 
    title = models.CharField( max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to=tools.get_services_image)
    services= models.CharField(max_length=50, choices=SERVICE_TYPE)
    is_active = models.BooleanField(default=True)

    # moderation
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "AltServices"
        verbose_name_plural = "AltServicess"

    def __str__(self):
        return self.title
    
class ServiceChoices(models.Model):

    subService = models.ForeignKey(AltServices, related_name='altservice_choce', on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    type = models.CharField(choices=INPUT_CHOICES, default='Radio', max_length=50)
    is_active = models.BooleanField(default=True)

    # moderation
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ServiceChoice"
        verbose_name_plural = "ServiceChoices"

    def __str__(self):
        return self.title
    
class Pros(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to=tools.get_services_image)
    bio = RichTextField()
    completedtasks = models.IntegerField(default=0)
    city = models.ManyToManyField(City, blank=True)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    # moderation
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField( auto_now=True)

    class Meta:
        verbose_name = "Pro"
        verbose_name_plural = "Pros"

    def __str__(self):
        return self.user.get_full_name()
    
class Order(models.Model):
    customer = models.ForeignKey(User,related_name='orders', on_delete=models.CASCADE)
    pro = models.ForeignKey(Pros, related_name='pro_orders', on_delete=models.CASCADE)
    service = models.ForeignKey(AltServices,  related_name='altservice_orders', on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=150)
    status = models.CharField(choices=STATUS_CHOICES, default='new', max_length=50)
    detail = models.TextField()
    totalAmount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    # moderation
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.service