from django.shortcuts import render
from django.http import JsonResponse
import time

requestIsSent = False
finalResult = None
finalResultInString = None


def activate(request):
    global finalResult
    global requestIsSent
    global finalResultInString
    if requestIsSent is True:
        pass
    else:
        requestIsSent = True

    while finalResult is None:
        print("hey")
        if finalResult is not None:
            break

    requestIsSent = False

    return JsonResponse(finalResultInString, safe=False)


def change_status(request):

    global requestIsSent
    global finalResult
    if requestIsSent is False:
        return JsonResponse("session is not started", safe=False)
    else:
        global finalResult
        global finalResultInString

        if request.GET.get('value') == 'False':
            print("lol1")
            finalResultInString = "Username or password is incorrect. Try again"
            finalResult = request.GET.get('value')
            time.sleep(1.5)
            finalResult = None
            return JsonResponse('success', safe=False)

        else:
            print("lol2")
            finalResult = request.GET.get('value')
            finalResultInString = True
            time.sleep(1.5)
            finalResult = None
            return JsonResponse(True, safe=False)



