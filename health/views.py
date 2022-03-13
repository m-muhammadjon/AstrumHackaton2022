import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse

from .models import Submission, UserSymptom


# Create your views here.
@login_required(login_url='/login')
def diagnos(request):
    return render(request, 'diagnos.html')


def submission_create(request):
    if request.method == 'POST':
        ans = json.loads(request.body)
        data = dict()
        submission = Submission.objects.create(user_id=request.user.id)
        print(submission.id)
        cnt = 0
        for i in range(0, len(ans), 2):
            st = True if ans[i + 1] == 'Ha' else False
            if ans[i + 1] == 'Ha':
                cnt += 1
            user_symptom = UserSymptom.objects.create(symptom_id=int(ans[i]), status=st, submisson=submission)
            data[ans[i]] = ans[i + 1]
        if cnt == 0:
            submission.verdict = "Sog'lom"
        elif 2 <= cnt <= 4:
            submission.verdict = f'{20 * cnt}% Covid'
        elif cnt == 5:
            submission.verdict = '90% Covid'
        else:
            submission.verdict = 'Shamollash'
        submission.save()
        print(submission.verdict)
        return redirect(reverse('account:profile', kwargs={'username': request.user.username}))
    return JsonResponse({'status': 'error'})
