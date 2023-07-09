from django.shortcuts import render
from django.views import View
from .forms import InvestmentForm

# Create your views here.
class Index(View):
 	def get(self, request):
 				form= InvestmentForm()
 				print('in get')
 				return render(request, 'calc/index.html', {'form':form})


 	def post(self, request):
 				form= InvestmentForm(request.POST)
 				print("in post")

 				if form.is_valid():
 					total_result = form.cleaned_data['starting_amount']
 					total_interest = 0
 					yearly_results ={}
 					print("in post1")

 					for i in range(1, int(form.cleaned_data['number_of_years'] +1)):
	 					yearly_results[i] = {}

	 					# cal interest
	 					interest = total_result*(form.cleaned_data['return_rate'] /100)
	 					print("interes1",i," ",interest)
	 					total_result+=interest
	 					total_interest +=interest
	 					print("Total interest",total_interest)

	 					#add additional contri
	 					total_result+= form.cleaned_data['annual_additional_contribution']

	 					#set yearly result
	 					yearly_results[i]['interest'] = round(total_interest,2)
	 					yearly_results[i]['total'] = round(total_result,2)

	 					print('calculation:', total_result)

 					#create context 
 					context ={
 						'years':'',
 						'total_result': round(total_result,2),
 						'yearly_results': yearly_results,
 						'number_of_years': int(form.cleaned_data['number_of_years'])
 					}

 					#render template
 				return render(request, 'calc/result.html', context)







