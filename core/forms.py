from django import forms

class AnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your answer here'}))

    def clean_answer(self):
        answer = self.cleaned_data.get('answer')
        # You can add validation for the answer field here if needed
        return answer