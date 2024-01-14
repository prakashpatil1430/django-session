from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt


def set_cokkies(request):
    response = render(request, 'cookie/set_cookie.html')

    # response.set_cookie(key='name', value='patil')
    # response.set_cookie(key='state', value='karnataka')
    # response.set_cookie(key='full_name', value='prakash patil')
    # response.set_cookie(key='name', value='p+patil')

    response.set_cookie(
        key='name',
        value='patil',
        httponly=True,

        # max_age should be in seconds
        # max_age=10

        expires=datetime.now() + timedelta(days=2),

        # only trusted connection allows its does not allow other to manipulate cookie
        secure=True,

        samesite='lax',

    )

    return response


def get_cookie(request):
    name = request.COOKIES.get('name', 'Default Value')
    address = request.COOKIES.get('address', 'Default Value')
    city = request.COOKIES.get('city', 'Default Value')
    profile = request.COOKIES.get('profile', 'Default Value')

    # to get all cokkies
    all_cookies = request.COOKIES
    for key, value in all_cookies.items():
        print(f"Cookie Name: {key}, Value: {value}")

    cookie_details = {
        'name': name,
        'address': address,
        'city': city,
        'profile': profile,
        'all_cookies': all_cookies
    }

    return render(request, 'cookie/get_cookies.html', cookie_details)


def update_cookie(request):
    response = render(request, 'cookie/set_cookie.html')
    response.set_cookie(key='profile', value='active')
    return response


def delete_cookie(request):
    response = render(request, 'cookie/set_cookie.html')
    response.delete_cookie('profile')
    return response


@csrf_exempt
def test_cookies(request):
    color = ''
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            color = 'green'
            request.session.delete_test_cookie()
            return HttpResponse("Your browser can use cookies.")
        color = 'red'
        return HttpResponse("Please enable cookies and try again.")

    context = {
        'color': color
    }
    request.session.set_test_cookie()
    return render(request, 'test_cookie.html', context)

