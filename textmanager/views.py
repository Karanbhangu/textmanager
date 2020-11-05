from django.shortcuts import render

# End points:
def index(request):
    return render(request,'index.html')

def submission(request):
    # Taking values:
    text = request.POST.get('text', 'default')
    remover = request.POST.get('remover', 'off')
    capital = request.POST.get('capital', 'off')
    lower = request.POST.get('lower', 'off')
    counter = request.POST.get('counter', 'off')
    # Logic implementation:
    puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if remover=="on":
        result=""
        for char in text:
            if char not in puncs:
                result = result + char
                text = result
    if capital=="on":
        result = ""
        for char in text:
            result = result + char.upper()
            text =result
    if lower=="on":
        result = ""
        for char in text:
            result = result + char.lower()
            text = result
    if counter=="on":
        resultone = 0
        for char in text:
            resultone = resultone+1
        final = {'clear':resultone}
        return render(request,'submission.html',final)
    if text=="":
        return render(request,'error.html')
    params = {'clear': result}
    return render(request, 'submission.html', params)

def about(request):
    return render(request, 'about.html')