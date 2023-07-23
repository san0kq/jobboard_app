from typing import Any

from django import forms


class AddSocialLinkForm(forms.Form):
    platform = forms.CharField(label="Platform", max_length=100, required=False, strip=True)
    url = forms.URLField(label="Url", max_length=200, required=False)

    def clean(self) -> Any:
        cleaned_data = super().clean()
        platform = cleaned_data.get('platform')
        url = cleaned_data.get('url')

        if platform and not url:
            raise forms.ValidationError("If you enter Platform, you must also enter Url.")
        elif not platform and url:
            raise forms.ValidationError("If you enter Url, you must also enter Platform.")

        return cleaned_data
