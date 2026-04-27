def city_country(city, country, population=None, language=None):
    city_and_country = (f'{city.title()}, {country.title()}')

    if population:
        city_and_country += f' - population {population}'
    if language:
        city_and_country += f', {language}'
    return city_and_country


city_1 = city_country('Santiago', 'Chile', 5000000, 'Spanish')
city_2 = city_country('paris', 'france')
city_3 = city_country('tokyo', 'japan', 14000000)
print(city_2)
print(city_3)
print(city_1)