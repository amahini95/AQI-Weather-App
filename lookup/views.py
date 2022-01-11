from django.shortcuts import render

# Create your views here.


#typing in website URL = making a REQUEST to the server to bring up the webpage
def home(request):
    #must import libs under specific view they'll be used in
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="
            + zipcode +
            "&distance=5&API_KEY=C90C9BAC-D6C0-473A-BEBD-2AE00BCE88CB")

        try:
            #"Load content from api_req variable into 'api'"
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error!"

        if api[1]['Category']['Name'] == "Good":
            category_description = "AQI: 0 - 50 | Health Implications: Air quality is considered satisfactory, and air pollution poses little or no risk"
            category_color = "good"
        elif api[1]['Category']['Name'] == "Moderate":
            category_description = "AQI: 51 -100 | Health Implications: Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[1]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "AQI: 101-150 | Health Implications: Members of sensitive groups may experience health effects. The general public is not likely to be affected."
            category_color = "usg"
        elif api[1]['Category']['Name'] == "Unhealthy":
            category_description = "AQI: 151-200 | Health Implications: Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[1]['Category']['Name'] == "Very Unhealthy":
            category_description = "AQI: 201-300 | Health Implications: Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "veryunhealthy"
        elif api[1]['Category']['Name'] == "Hazardous":
            category_description = "AQI: 300+ | Health Implications: Health alert: everyone may experience more serious health effects."
            category_color = "hazardous"
        #Now, we can pass api var into our content variable {}
        return render(
            request, 'home.html', {
                'api': api,
                'category_description': category_description,
                'category_color': category_color
            })
    else:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94588&distance=5&API_KEY=C90C9BAC-D6C0-473A-BEBD-2AE00BCE88CB"
        )

        try:
            #"Load content from api_req variable into 'api'"
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error!"

        if api[0]['Category']['Name'] == "Good":
            category_description = "AQI: 0 - 50 | Health Implications: Air quality is considered satisfactory, and air pollution poses little or no risk"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "AQI: 51 -100 | Health Implications: Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "AQI: 101-150 | Health Implications: Members of sensitive groups may experience health effects. The general public is not likely to be affected."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "AQI: 151-200 | Health Implications: Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "AQI: 201-300 | Health Implications: Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "AQI: 300+ | Health Implications: Health alert: everyone may experience more serious health effects."
            category_color = "hazardous"
        #Now, we can pass api var into our content variable {}
        return render(
            request, 'home.html', {
                'api': api,
                'category_description': category_description,
                'category_color': category_color
            })


def about(request):
    return render(request, 'about.html', {})
