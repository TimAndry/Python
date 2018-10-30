from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'words' in request.session:
        request.session['words'] = request.session['words']
    else:
        request.session['words'] = []
    return render(request, 'sword_app/index.html')


def update(request):
    if request.method == 'POST':
        if 'words' in request.session:
            temp_word = request.POST['word']
            temp_color = request.POST['color']
            if temp_color == "red":
                color = "red"
            elif temp_color =="green":
                color = "green"
            else:
                color = "blue"
            if 'fontsize' in request.POST:
                print(request.POST['fontsize'])
                font = '2em'
            else:
                font = '1em'
            word = '<h4 style="color:'+ color + '; font-size:' + font + ';">' + temp_word + '</h4>'
            temp_word = word
            request.session['word'] = temp_word
            temp_list = request.session['words']
            temp_list.append(request.session['word'])
            request.session['words'] = temp_list
        else: 
            request.session['word'] = ""  
           
    return redirect('/')

def clear(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect('/')