from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ChatForm
from .models import ChatMessage
from .ai_engine import farming_ai


@login_required
def chatbot_view(request):

    if request.method == "POST":

        form = ChatForm(request.POST, request.FILES)

        if form.is_valid():

            chat = form.save(commit=False)
            chat.user = request.user

            # AI generates answer
            answer = farming_ai(chat.question)

            chat.answer = answer
            chat.save()

    else:
        form = ChatForm()

    # Show chat history
    messages = ChatMessage.objects.filter(
        user=request.user
    ).order_by("created_at")

    return render(
        request,
        "chatbot/chat.html",
        {
            "form": form,
            "messages": messages
        }
    )