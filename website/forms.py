from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    daysonmarket = forms.FloatField(required=True, initial=22, widget=forms.NumberInput(attrs={'id': 'form_daysonmarket', 'step': "1"}))
    engine_displacement = forms.FloatField(required=True, initial=3800, widget=forms.NumberInput(attrs={'id': 'form_engine_displacement', 'step': "1"}))
    horsepower = forms.FloatField(required=True, initial=197, widget=forms.NumberInput(attrs={'id': 'form_horsepower', 'step': "1"}))
    latitude = forms.FloatField(required=True, initial=423896, widget=forms.NumberInput(attrs={'id': 'form_latitude', 'step': "1"}))
    listing_id = forms.FloatField(required=True, initial=279567433, widget=forms.NumberInput(attrs={'id': 'form_listing_id', 'step': "1"}))
    longitude = forms.FloatField(required=True, initial=7157, widget=forms.NumberInput(attrs={'id': 'form_longitude', 'step': "1"}))
    mileage = forms.FloatField(required=True, initial=119762, widget=forms.NumberInput(attrs={'id': 'form_mileage', 'step': "1"}))
    savings_amount = forms.FloatField(required=True, initial=2355, widget=forms.NumberInput(attrs={'id': 'form_savings_amount', 'step': "1"}))
    seller_rating = forms.FloatField(required=True, initial=4, widget=forms.NumberInput(attrs={'id': 'form_seller_rating', 'step': "1"}))
    sp_id = forms.FloatField(required=True, initial=389417, widget=forms.NumberInput(attrs={'id': 'form_sp_id', 'step': "1"}))
    year = forms.FloatField(required=True, initial=2010, widget=forms.NumberInput(attrs={'id': 'form_year', 'step': "1"}))

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        daysonmarket = cleaned_data.get('daysonmarket')
        engine_displacement = cleaned_data.get('engine_displacement')
        horsepower = cleaned_data.get('horsepower')
        latitude = cleaned_data.get('latitude')
        listing_id = cleaned_data.get('listing_id')
        longitude = cleaned_data.get('longitude')
        mileage = cleaned_data.get('mileage')
        savings_amount = cleaned_data.get('savings_amount')
        seller_rating = cleaned_data.get('seller_rating')
        sp_id = cleaned_data.get('sp_id')
        year = cleaned_data.get('year')
        if (not name and not daysonmarket and not engine_displacement and not horsepower and not latitude and 
            not listing_id and not longitude and not mileage and not savings_amount and not seller_rating and 
            not sp_id and not year):
            raise forms.ValidationError('Some fields have errors!')
