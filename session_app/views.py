from django.shortcuts import render, redirect

# Create your views here.


def set_item(request):
    request.session['animal_1'] = 'tiger'
    request.session['animal_2'] = 'rabbit'
    request.session['animal_3'] = 'cow'
    request.session['animal_4'] = 'lion'
    request.session['animal_5'] = 'cat'

    return render(request, 'sessions/set_session.html')


def get_item(request):
    animal_1 = request.session.get('animal_1', 'd1')
    animal_2 = request.session.get('animal_2', 'd2')
    animal_3 = request.session.get('animal_3', 'd3')
    animal_4 = request.session.get('animal_4', 'd4')
    animal_5 = request.session.get('animal_5', 'd5')

    context = {
        'animal_1': animal_1,
        'animal_2': animal_2,
        'animal_3': animal_3,
        'animal_4': animal_4,
        'animal_5': animal_5
    }

    return render(request, 'sessions/get_session.html', context)


def del_item(request):
    if 'animal_5' in request.session:
        del request.session['animal_5']
    return redirect('get-item')


def session_methods(request):
    # all keys in session
    keys = request.session.keys()
    values = request.session.values()

    items = request.session.items()

    # clearing session
    # request.session.clear()

    # using set default
    # animal_5 = request.session.setdefault('animal_5', 'chita')
    # animal_6 = request.session.setdefault('animal_6', 'chita')

    # removing all sessions
    # request.session.flush()

    # setting session to expiry
    request.session.set_expiry(10)  # -->10 seconds

    # get session expiry age
    sesion_expiry_time = request.session.get_expiry_age()

    # get sestion expiry at browser close it return true or false
    # expiry_at_browser_close = request.session.get_expiry_at_browser_close()

    # seting session cookie age SET IN settings.py

    context = {
        'keys': keys,
        'values': values,
        'items': items,
        # 'animal_5': animal_5,
        # 'animal_6': animal_6,
        'sesion_expiry_time': sesion_expiry_time,
        # 'expiry_at_browser_close': expiry_at_browser_close
    }

    return render(request, 'sessions/other_sessions.html', context)


# page_count_project
def page_count(request):
    p_count = request.session.get('count', 0)
    new_count = p_count + 1
    request.session['count'] = new_count

    context = {
        'p_count': p_count
    }

    return render(request, 'sessions/page_count.html', context)
