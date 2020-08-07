from django import forms 
from .models import CarCreate
from .models import Order
from .models import Subscription
from .models import TaskList

class CarCreateForm (forms.ModelForm):
    class Meta:
        model = CarCreate 
        fields = ['Car Company', 'Car Model', 'License Plate Number', 'Car Image', 'Passenger Seats', 'Per Day Cost', 'Car Description']

class OrderForm (forms.ModelForm):
    class Meta:
        model = Order
        fields = ['User Name','Employee Name'[ Note: Appear Automatically with Car Selection ], 'Email Address', 'Contact Number', 'Car' [Note: Drop Down], 'Order Period' [Note: Date Picker]]

class SubcriptionForm (forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['Name', 'Email Address', 'Message']
