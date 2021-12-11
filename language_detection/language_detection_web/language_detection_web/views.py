from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(strval):
    import pickle
    model = pickle.load(open("/home/jawad/Documents/extra1/language_detection/language_detection_web/language_detection_web/language_detection_ml_model.sav", "rb"))
    scaled = pickle.load(open("/home/jawad/Documents/extra1/language_detection/language_detection_web/language_detection_web/countvector.sav", "rb"))
    prediction = model.predict(scaled.transform([strval]))
    
    if prediction == 0:
        return "english"
    elif prediction == 1:
        return "Malayalam"
    elif prediction == 2:
        return "Hindi"
    elif prediction == 3:
        return "Tamil"
    elif prediction == 4:
        return "Portugeese"
    elif prediction == 5:
        return "french"
    elif prediction == 6:
        return "Dutch"
    elif prediction == 7:
        return "Spanish"
    elif prediction == 8:
        return "Greek"
    elif prediction == 9:
        return "Russian"
    elif prediction == 10:
        return "Danish"
    elif prediction == 11:
        return "Italian"
    elif prediction == 12:
        return "Turkish"
    elif prediction == 13:
        return "Sweedish"
    elif prediction == 14:
        return "Arabic"
    elif prediction == 15:
        return "German"
    elif prediction == 16:
        return "Kannada"
    else:
        return "error"
        

# our result page view
def result(request):
    text = request.GET['strval2']

    result = getPredictions(text)

    #return render(request, 'result.html', {'result':result})
    return render(request, 'index.html', {'result':result})
