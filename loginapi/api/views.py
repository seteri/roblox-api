from django.shortcuts import render
from django.http import JsonResponse

requestIsSent = False
finalResult = None


def activate(request):
    global requestIsSent
    if requestIsSent is True:
        pass
    else:
        requestIsSent = True

    while finalResult is None:
        print("hey")
        if finalResult is not None:
            break

    return JsonResponse(requestIsSent, safe=False)


def change_status(request):
    global finalResult
    finalResult = request.GET.get('value')
    print(finalResult)

    return JsonResponse(finalResult, safe=False)
