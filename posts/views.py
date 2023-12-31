from django.shortcuts import render, get_object_or_404

from posts.models import Post


# Create your views here.
def posts(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, template_name='index.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context=context)


# def about(request):
#     return render(request, 'about.html')

def base_navbar(request):
    return render(request, 'base.html')
