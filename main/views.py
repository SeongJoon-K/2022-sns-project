from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.


def showmain(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,5) # 객체들의 목록을 끊어줄거다, 몇개까지
    pagnum = request.GET.get('page') # 페이지에 해당하는 밸류의 키값을 반환하기 위해서 GET 요청을 함
    posts = paginator.get_page(pagnum) # 페이지네이터에서 짜른 객체가 posts에 요청이 갈꺼고, 담길것임
    return render(request, 'main/mainpage.html', {'posts': posts})


def intro(request):
    return render(request, 'main/show.html')


def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post':post, 'comments':all_comments})



def new(request):
    return render(request, 'main/new.html')


def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail', new_post.id)


def edit(request, id):
    edit_blog = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post': edit_blog})


def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('main:detail', update_post.id)


def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:showmain')


def create_comment(request, post_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post, pk=post_id)
    new_comment.save()

    return redirect('main:detail', post_id)

# 댓글 delete 구현
def delete_comment(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()

    return redirect('/'+str(post_id))

def update_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        post_id = comment.post.id
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('main:detail', post_id)
    
    else:
        return render(request, 'main/update_comment.html', {'post':post, 'comment':comment})

