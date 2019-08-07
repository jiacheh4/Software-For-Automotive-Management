import json
import threading
import requests
import urllib.request
from queue import Queue
from functions import *

### Variables Declaration ###
# Load DatasetId #
datasetid_url = 'http://websiteLink/api/datasetId'
datasetid = json.loads(urllib.request.urlopen(datasetid_url).read().decode('ASCII'))['datasetId']
# Load VehicleIds #
vehicleid_url = 'http://websiteLink/api/' + datasetid + '/vehicles'
vehicleids = json.loads(urllib.request.urlopen(vehicleid_url).read().decode('ASCII'))['vehicleIds']
# POST to API #
answer_url = 'http://websiteLink/api/' + datasetid + '/answer'
headers = {'Content-type' : 'application/json', 'Accept' : 'application/json'}

result_list = [] 
queue = Queue()
number_of_threads = 8

### Main Body ###
def create_threads():
	for _ in range(number_of_threads):
		T = threading.Thread(target = task)
		# Creating Daemon threads (die after program ends)
		T.daemon = True
		T.start()

def create_tasks():
	for i in temp_list:
		queue.put(i)
	queue.join() # Block the queue
	del temp_list[:]
	run()

def task():
	while True:
		quest = queue.get()
		print(quest) # To see how many API requests were made
		item = json.loads(urllib.request.urlopen(quest).read().decode('ASCII'))
		result_list.append(item)
		queue.task_done()

def run():
	if len(temp_list) > 0:
		create_tasks()

if __name__ == '__main__':
	create_threads()
	print("Retrieving data from Id:", datasetid)
	# Get a list of vehicle Ids #
	temp_list = get_vehicles(datasetid, vehicleids)
	run()
	vehicle_list = list(result_list)
	# Get a list of dealer Ids and names #
	temp_list = get_dealers(datasetid, result_list)
	del result_list[:]
	run()
	# Print response from the server
	response = get_answer(result_list, vehicle_list)
	msg = requests.post(url = answer_url, headers = headers, data = str(response))
	print(msg.text)