from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pg_records(request, list, num):
    paginator = Paginator(list, num)
    page = request.GET.get('page')      # [[ post_list.html 에서 href="?page={{ posts.previous_page_number }} ]] 
    try:
        page_object = paginator.page(page)
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)
    return page_object
