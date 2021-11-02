from django.views import generic

from news.models import Post
from news.serializers import PostSerializer


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    serializer_class = PostSerializer


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
