from django.shortcuts import render

from django.views import View

from paint.forms import ColorPickerForm

# Create your views here.

class ColorPickerView(View):
    def get(self, request):
        form = ColorPickerForm()

        context = {
            'form': form,
            'red': 100,
            'green': 50,
            'blue': 50,
            }
        return render(
            request=request, template_name='color_picker.html', context=context
        )
    def post(self,request):
        red = int(request.POST['red_amount'])
        green = int(request.POST['red_amount'])
        blue = int(request.POST['red_amount'])

        form = ColorPickerForm()


        context = {
            'form': form,
            'red': red,
            'green': green,
            'blue': blue,
            }
        return render(
            request=request, template_name='color_picker.html', context=context
        )