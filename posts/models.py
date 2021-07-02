from django.db import models
from django.utils.text import slugify

# TODO: sposta sta merda da qui (e rifalla pure)
def generate_unique_slug(klass, field, instance=None):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`
    :param `klass` is Class model.
    :param `field` is specific field for title.
    :param `instance` is instance object for excluding specific object.
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    if instance is not None:
        while klass.objects.filter(slug=unique_slug).exclude(id=instance.id).exists():
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
    else:
        while klass.objects.filter(slug=unique_slug).exists():
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
    return unique_slug

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=40, unique=True, editable=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.SlugField(max_length=120, unique=True, editable=False)
    pub_date = models.DateTimeField('date published')
    image = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_unique_slug(Post, self.title, self)
        super(Post, self).save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=20)
    posts = models.ManyToManyField(Post)