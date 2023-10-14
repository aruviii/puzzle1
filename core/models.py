from django.db import models

class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_phrase = models.CharField(max_length=255)

    def __str__(self):
        return self.question_phrase

class Matches(models.Model):
    match_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    match_phrase = models.CharField(max_length=255)

    def __str__(self):
        return self.match_phrase

class Replies(models.Model):
    reply_id = models.AutoField(primary_key=True)  # Primary key as auto-incrementing field
    phrase = models.CharField(max_length=255)
    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return self.phrase
class Possibilities(models.Model):
    possibility_id = models.AutoField(primary_key=True)  # Primary key as auto-incrementing field
    phrase = models.CharField(max_length=255)  # CharField with a maximum length of 255 characters
    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
    def __str__(self):
        return self.phrase
