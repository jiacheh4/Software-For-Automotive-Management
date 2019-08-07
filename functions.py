### Retrieves all vehicles ###
def get_vehicles(datasetid, vehicleids):
    v_list = []

    for i in vehicleids:
        vehicle_url = 'http://websiteLink/api/' + datasetid + '/vehicles/' + str(i)
        v_list.append(vehicle_url)

    # Return a list of vehicle urls
    return v_list

### Retrieves all dealers ###
def get_dealers(datasetid, vehicle_list):
    d_list = []

    for i in vehicle_list:
        dealer_url = 'http://websiteLink/api/' + datasetid + '/dealers/' + str(i['dealerId'])
        if dealer_url not in d_list:
            d_list.append(dealer_url)

    # Return a list of dealer urls
    return d_list

### Return desired format of answer ###
def get_answer(dealer_list, vehicle_list):
    dealer_dict = {}
    answer = {'dealers':[]}

    for i in dealer_list:
        i['vehicles'] = []
        dealer_dict[i['dealerId']] = i

    for i in vehicle_list:
    	filtered = {item:i[item] for item in i if item != 'dealerId'}
    	dealer_dict[i['dealerId']]['vehicles'].append(filtered)

    answer['dealers'] = list(dealer_dict.values())
    # Return a dictionary that stores all the dealers
    return answer