from countryinfo import CountryInfo
count = input("Enter your country: ")
country = CountryInfo(count)
print("Capital is : ", country.capital())
print("Population : ", country.population())
print("Area(in square killometers) : ", country.area())
print("Region : ",country.region())
print("Subregion : ",country.subregion())
print("Demonym : ",country.demonym())
print("Currencies is : ", country.currencies())
print("Language is : ", country.languages())
print("Borders are : ",country.borders())
print("Others names : ", country.alt_spellings())


