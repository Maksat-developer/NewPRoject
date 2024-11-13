from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests



from .forms import MethodSelectionForm, ParsingForm



def choose_method(request):
	if request.method == "POST":
		form = MethodSelectionForm(request.POST)
		if form.is_valid():
			method = form.cleaned_data['method']
			return redirect('start_parsing', method=method)
	else:
		form = MethodSelectionForm()

	return render(request, 'base_app/choose_method.html', {'form':form})



def start_parsing(request, method):
	if request.method == 'POST':
		form = ParsingForm(request.POST)
		if form.is_valid():
			url = form.cleaned_data['url']
			selector = form.cleaned_data['selector']

			parsed_data = None


			if method == 'requests':
				response = requests.get(url)
				soup = BeautifulSoup(response.content, 'html.parser')
				parsed_data = soup.select(selector)

			elif method == 'selenium':
				options = Options()
				options.headless = True
				driver = webdriver.Chrome(options=options)
				driver.get(url)
				elements = driver.find_elements(By.CSS_SELECTOR, selector)
				parsed_data = [element.get_attribute('outerHTML') for element in elements]
				driver.quit()


			return render(request, 'base_app/result.html', {'data': parsed_data})

	else:
		form = ParsingForm()
	return render(request, 'base_app/start_parsing.html', {"form":form, "method": method})







# {'form': form, 'method': method})