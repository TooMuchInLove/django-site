from django.forms import ModelForm, TextInput, Select, NumberInput, DateTimeInput
from .models import Tender


class TenderForm(ModelForm):
	class Meta:
		model = Tender
		fields = [
			'id', 'userAddFK', 'startsSumT', 'dateAddT', 'dateActionT', 'dateDocT',
			'numT', 'regionFK',
		]

		widgets = {
			'userAddFK' : Select(attrs={
				'class'    : 'select form__select',
				'disabled' : 'disabled',
			}),
			'startsSumT' : NumberInput(attrs={
				'class'    : 'select form__select',
				'disabled' : 'disabled',
			}),
			'dateAddT' : DateTimeInput(attrs={
				'class'    : 'select form__select',
				'disabled' : 'disabled',
				'type'     : 'datetime-local',
			}),
			'dateActionT' : DateTimeInput(attrs={
				'class'    : 'select form__select',
				'disabled' : 'disabled',
				'type'     : 'datetime-local',
			}),
			'dateDocT' : DateTimeInput(attrs={
				'class'    : 'select form__select',
				'disabled' : 'disabled',
				'type'     : 'datetime-local',
			}),
			'numT' : TextInput(attrs={
				'class'    : 'select form__select',
				'disabled' : 'disabled',
			}),
			'regionFK' : Select(attrs={
				'class'    : 'select form__select',
				'disabled' : 'disabled',
			}),
		}