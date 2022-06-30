import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


def show_results_of(phone_number):
    ch_number = phonenumbers.parse(phone_number, 'CH')
    r1 = geocoder.description_for_number(ch_number, 'en')
    service_number = phonenumbers.parse(phone_number, "RO")
    r2 = carrier.name_for_number(service_number, 'en')
    p_number = phonenumbers.parse(phone_number)
    r3 = timezone.time_zones_for_number(p_number)
    return list([r1, r2] + list(r3))


def get_phone_number_info(phone_number, operation):
    results = []
    if operation == '1':

        if phone_number[0] == '+':
            cc = '+' + str(phonenumbers.parse(phone_number).country_code)
            return [cc, show_results_of(phone_number)]
        else:
            counter = 0
            country_codes = open('COUNTRY_CODES.txt', 'r').readlines()
            for cc in country_codes:
                try:
                    cc = cc.replace('\n', '')
                    p_number = phonenumbers.parse(f'+{cc}{phone_number}')
                    if phonenumbers.is_possible_number(p_number):
                        if show_results_of(f'+{cc}{phone_number}')[0]:
                            results.append(f'Country Code: +{cc}, {show_results_of("+" + cc + phone_number)}')
                            counter += 1
                except:
                    pass
            return results
    else:
        return show_results_of(phone_number)[2]

for pn in get_phone_number_info(input('Αριθμός τηλεφώνου: '), '1'):
	print(pn)
