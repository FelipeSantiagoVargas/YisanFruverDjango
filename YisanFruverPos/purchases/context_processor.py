def total_purchase(request):
    total = 0
    if request.user.is_authenticated:
        if 'purchase' in request.session.keys():
            for key, value in request.session['purchase'].items():
                total += int(value['price'])
    return {'total_purchase':total}