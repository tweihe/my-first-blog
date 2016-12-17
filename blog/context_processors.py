def categories_processor(request):
    length = request.POST.get('length')
    complexity = request.POST.get('complexity')
    if length != None:
        lengthval = int(length)
        complexval = int(complexity)
        testatron = lengthval * complexval
        return {'length': length, 'complexity' : complexity, 'testatron': testatron}

    return {'length': length, 'complexity' : complexity}
