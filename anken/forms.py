from django import forms
from .models import Anken


class AnkenForm(forms.ModelForm):
    class Meta:
        # どのモデルをフォームにするか指定
        model = Anken
        
        # そのフォームの中から表示するフィールドを指定
        fields = ('pub_date',
                'ankenmei',
                'iraibusho',
                'iraisha',
                'nouki',
                'mitumorikousu',
                'naiyou',
                'genjouchi', 
                'kitaikouka', 
                'tantousha',  
                'koumoku', 
                'joutai', 
                'jissekikousu',
                )

    # フォームを綺麗にするための記載
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'