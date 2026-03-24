from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback


@login_required
def feedback_view(request):

    if request.method == "POST":

        form = FeedbackForm(request.POST)

        if form.is_valid():

            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()

            return redirect("feedback")

    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all().order_by("-created_at")

    return render(request, "feedback/feedback.html", {
        "form": form,
        "feedbacks": feedbacks
    })