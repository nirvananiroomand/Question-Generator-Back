from django.db import models

from user.models import CustomUser


# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    difficulty = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True)

    @property
    def chat_questions(self):
        return ChatQuestion.objects.filter(chat_id=self.id)


class ChatQuestion(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=30)
    quantity = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['chat', 'question_type'], name='unique_chat_question_type')
        ]
