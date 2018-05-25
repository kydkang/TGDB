from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import hashlib
from django.utils.crypto import get_random_string

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


def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()
