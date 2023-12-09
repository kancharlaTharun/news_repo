from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request, 'testapp/index.html')
def movies_view(request):
    head_msg = 'Movie Information'
    sub_msg1 = 'Jailer is very good movie'
    sub_msg2 = 'planning for ashiqui-3 with alluarjun & srileela'
    sub_msg3 = 'Dont go for movies....practice django...'
    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2': sub_msg2, 'sub_msg3': sub_msg3}
    return render(request, 'testapp/news.html', my_dict)
def sports_view(request):
    head_msg = 'Sports information'
    sub_msg1 = 'yesterday india won the match'
    sub_msg2 = 'yesterday match india vs ausis'
    sub_msg3 = 'Next match also ind vs aus'
    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2': sub_msg2, 'sub_msg3': sub_msg3}
    return render(request, 'testapp/news.html', my_dict)
def politics_view(request):
    head_msg = 'Politics information'
    sub_msg1 = 'India PM is Modi'
    sub_msg2 = 'Telangana CM K.C.R'
    sub_msg3 = 'Telanagana next CM...?'
    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2': sub_msg2, 'sub_msg3': sub_msg3}
    return render(request, 'testapp/news.html', my_dict)