from django import forms
class inputform(forms.Form):
    qty=forms.IntegerField(min_value=1,max_value=8,label="qty")
    input=forms.IntegerField(min_value=1,max_value=200,label="size")