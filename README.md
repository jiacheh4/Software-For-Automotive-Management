
### Software for Automative Management ###

### Overview ###
The purpose of this program is to retrieve a datasetID, retrieves all vehicles and dealers for that dataset, and successfully posts to the answer endpoint **only**.
This program simulates a bridge that connects the database and other programs in the system by parsing the data from the database and return important information, and it can be further used for purposes such as displaying information on the UI, calculating statistics, improving efficiency and workflow.

### Prerequisites ###
Note: Please use Python 3 to run this program. 
      Please install the "requests" module in order to sucessfully submit/POST the answer   

    pip3 install requests

### Getting Started ###
The first naive solution takes significantly longer than 30 sec. Therefore, optimization is needed. Since there is no optimization can be done on server's side (The better solution: make only one API request to retrieve all the data), I decided to use Multi-threading and Queue to optimize/decrease the total time. The time this program takes is around 8 to 11 secs. If the datasetId may be repetitious, then it can be optimized further by implementing a cache to store the result of the datasetId with an O(1) time to fetch.

### Running the tests ###
To run the unittest after you executed the program. Type the line below on the terminal.

    python test_functions.py

### Author ###

Jason Huang 

### Links ###
http://websiteLink
http://websiteLink/swagger/ui/index

