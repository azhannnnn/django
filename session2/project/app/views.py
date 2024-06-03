from django.shortcuts import render

def set(request):
    request.session['name'] = "Azhan"
    request.session['city']="Bhopal"
    # request.session.set_expiry(600)       # 600 sec or 10 minutes
    # request.session.set_expiry(20)        # 20 sec
    # request.session.set_expiry(10)          # 10 sec

    request.session.set_expiry(0)         # session die when browser close
    return render(request,'set.html')

def get(request):
    name = request.session['name']
    name = request.session.get('name','Guest')
    return render(request,'get.html',{"name":name})
    
#     keys()
#     keys = request.session.keys()
#     return render(request,'get.html',{"name":name,'keys':keys})

#     values()
#     keys = request.session.values()
#     return render(request,'get.html',{"name":name,'keys':keys})

#     items()
#     keys = request.session.items()
#     return render(request,'get.html',{"name":name,'keys':keys})

#     setdefault()
#     keys = request.session.setdefault('age','35')
#     return render(request,'get.html',{"name":name,'keys':keys})

# def get(request):
    name = request.session['name']
    session_age = request.session.get_session_cookie_age()                  # It used to get session-cookie age in second (By-Default 14 days)
    expiry_age = request.session.get_expiry_age()                           # It used to get expiry age in second (By-Default 14 days)
    expiry_date = request.session.get_expiry_date()                         # It used to get expiry date (By-Default 14 days)
    expire_at_browser_close =request.session.get_expire_at_browser_close()  # It gives either True of False (By-Default false)
    data = {"name":name,
            "session_age":session_age,
            "expiry_age":expiry_age,
            "expiry_date":expiry_date,
            "expire_at_browser_close":expire_at_browser_close
            }
    return render(request,'get.html',{'data':data})

# def delete(request):
#     if 'name'in request.session:
#         del request.session['name']
#         request.session.flush()           # completly remove from our system
#     return render(request,'app/delete.html')


def delete(request):
    # del request.session['name']           # Delete specific session data from server database
    # request.session.clear()               # remove all sessions from server database
    request.session.clear_expired()         # remove only expired sessions from server database
    return render(request,'delete.html')