from django.shortcuts import render
from .models import Post

def index(request):
    post_list = Post.objects.order_by('-pub_date')[:5]
    for post in post_list:
        post.tags = post.tag_set.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)

