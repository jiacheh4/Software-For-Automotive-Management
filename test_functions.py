import unittest
import functions

class Test(unittest.TestCase):

    def test_get_vehicles(self):
        case1 = functions.get_vehicles('w9liMFiq1gg', [1641409189,921408717,1941497680,432971532,1358130690,169982664,601199527,1235196171,1175157997])
        case2 = functions.get_vehicles('Lm4m7lqq1gg', [1645975477,1673070333,59772868,954761128,1199271554,1603233528,481141026,50609503,1888363826])
        self.assertEqual(case1, ['http://websiteLink/api/w9liMFiq1gg/vehicles/1641409189',
                                  'http://websiteLink/api/w9liMFiq1gg/vehicles/921408717',
                                  'http://websiteLink/api/w9liMFiq1gg/vehicles/1941497680',
                                  'http://websiteLink/api/w9liMFiq1gg/vehicles/432971532',
                                  'http://websiteLink/api/w9liMFiq1gg/vehicles/1358130690',
                                  'http://websiteLink/api/w9liMFiq1gg/vehicles/169982664',
                                  'http://websiteLink/api/w9liMFiq1gg/vehicles/601199527',
                                  'http://websiteLink/api/w9liMFiq1gg/vehicles/1235196171',
                                  'http://websiteLink/api/w9liMFiq1gg/vehicles/1175157997'])
        self.assertEqual(case2, ['http://websiteLink/api/Lm4m7lqq1gg/vehicles/1645975477',
                                  'http://websiteLink/api/Lm4m7lqq1gg/vehicles/1673070333',
                                  'http://websiteLink/api/Lm4m7lqq1gg/vehicles/59772868',
                                  'http://websiteLink/api/Lm4m7lqq1gg/vehicles/954761128',
                                  'http://websiteLink/api/Lm4m7lqq1gg/vehicles/1199271554',
                                  'http://websiteLink/api/Lm4m7lqq1gg/vehicles/1603233528',
                                  'http://websiteLink/api/Lm4m7lqq1gg/vehicles/481141026',
                                  'http://websiteLink/api/Lm4m7lqq1gg/vehicles/50609503',
                                  'http://websiteLink/api/Lm4m7lqq1gg/vehicles/1888363826'])
    def test_get_dealers(self):
        case1 = functions.get_dealers('w9liMFiq1gg', [{'vehicleId': 921408717, 'year': 2016, 'make': 'Bentley', 'model': 'Mulsanne', 'dealerId': 979936376}, {'vehicleId': 1235196171, 'year': 2013, 'make': 'Mitsubishi', 'model': 'Gallant', 'dealerId': 603699148}, {'vehicleId': 1941497680, 'year': 2012, 'make': 'Nissan', 'model': 'Altima', 'dealerId': 979936376}, {'vehicleId': 169982664, 'year': 2014, 'make': 'Ford', 'model': 'F150', 'dealerId': 1931514154}, {'vehicleId': 432971532, 'year': 2009, 'make': 'Ford', 'model': 'F150', 'dealerId': 603699148}, {'vehicleId': 1175157997, 'year': 2016, 'make': 'Honda', 'model': 'Accord', 'dealerId': 1931514154}, {'vehicleId': 1641409189, 'year': 2004, 'make': 'MINI', 'model': 'Cooper', 'dealerId': 1931514154}, {'vehicleId': 1358130690, 'year': 1979, 'make': 'Cheverolet', 'model': 'Corvette', 'dealerId': 979936376}, {'vehicleId': 601199527, 'year': 2016, 'make': 'Kia', 'model': 'Soul', 'dealerId': 603699148}])
        case2 = functions.get_dealers('Lm4m7lqq1gg', [{'vehicleId': 50609503, 'year': 2016, 'make': 'Bentley', 'model': 'Mulsanne', 'dealerId': 1748682542}, {'vehicleId': 1673070333, 'year': 2016, 'make': 'Honda', 'model': 'Accord', 'dealerId': 71566500}, {'vehicleId': 59772868, 'year': 2013, 'make': 'Mitsubishi', 'model': 'Gallant', 'dealerId': 2031206662}, {'vehicleId': 1603233528, 'year': 2014, 'make': 'Ford', 'model': 'F150', 'dealerId': 71566500}, {'vehicleId': 1199271554, 'year': 2012, 'make': 'Nissan', 'model': 'Altima', 'dealerId': 1748682542}, {'vehicleId': 1888363826, 'year': 2009, 'make': 'Ford', 'model': 'F150', 'dealerId': 2031206662}, {'vehicleId': 1645975477, 'year': 2016, 'make': 'Kia', 'model': 'Soul', 'dealerId': 2031206662}, {'vehicleId': 954761128, 'year': 2004, 'make': 'MINI', 'model': 'Cooper', 'dealerId': 71566500}, {'vehicleId': 481141026, 'year': 1979, 'make': 'Cheverolet', 'model': 'Corvette', 'dealerId': 1748682542}])
        case3 = functions.get_dealers('NG_5316q1gg', [{'vehicleId': 582418722, 'year': 2013, 'make': 'Mitsubishi', 'model': 'Gallant', 'dealerId': 341350741}, {'vehicleId': 2098373134, 'year': 2016, 'make': 'Honda', 'model': 'Accord', 'dealerId': 1848425408}, {'vehicleId': 135699757, 'year': 2016, 'make': 'Bentley', 'model': 'Mulsanne', 'dealerId': 161490541}, {'vehicleId': 181620611, 'year': 2012, 'make': 'Nissan', 'model': 'Altima', 'dealerId': 161490541}, {'vehicleId': 850631984, 'year': 2009, 'make': 'Ford', 'model': 'F150', 'dealerId': 341350741}, {'vehicleId': 88614502, 'year': 2014, 'make': 'Ford', 'model': 'F150', 'dealerId': 1848425408}, {'vehicleId': 191512138, 'year': 2016, 'make': 'Kia', 'model': 'Soul', 'dealerId': 341350741}, {'vehicleId': 943745945, 'year': 2004, 'make': 'MINI', 'model': 'Cooper', 'dealerId': 1848425408}, {'vehicleId': 1281667626, 'year': 1979, 'make': 'Cheverolet', 'model': 'Corvette', 'dealerId': 161490541}])
        self.assertEqual(case1, ['http://websiteLink/api/w9liMFiq1gg/dealers/979936376',
                                  'http://websiteLink/api/w9liMFiq1gg/dealers/603699148',
                                  'http://websiteLink/api/w9liMFiq1gg/dealers/1931514154'])
        self.assertEqual(case2, ['http://websiteLink/api/Lm4m7lqq1gg/dealers/1748682542',
                                  'http://websiteLink/api/Lm4m7lqq1gg/dealers/71566500',
                                  'http://websiteLink/api/Lm4m7lqq1gg/dealers/2031206662'])
        self.assertEqual(case3, ['http://websiteLink/api/NG_5316q1gg/dealers/341350741',
                                  'http://websiteLink/api/NG_5316q1gg/dealers/1848425408',
                                  'http://websiteLink/api/NG_5316q1gg/dealers/161490541'])

    def test_get_answer(self):
        ### id = qwosfl-q1gg ###
        case1 = functions.get_answer([{'dealerId': 1265629142, 'name': "Bob's Cars"}, {'dealerId': 1842785779, 'name': "Doug's Doozies"}, {'dealerId': 357686040, 'name': 'House of Wheels'}], 
                                     [{'vehicleId': 1795478997, 'year': 2016, 'make': 'Bentley', 'model': 'Mulsanne', 'dealerId': 1842785779}, {'vehicleId': 1323953228, 'year': 2016, 'make': 'Honda', 'model': 'Accord', 'dealerId': 1265629142}, {'vehicleId': 539873024, 'year': 2013, 'make': 'Mitsubishi', 'model': 'Gallant', 'dealerId': 357686040}, {'vehicleId': 278760250, 'year': 2009, 'make': 'Ford', 'model': 'F150', 'dealerId': 357686040}, {'vehicleId': 2133416123, 'year': 2014, 'make': 'Ford', 'model': 'F150', 'dealerId': 1265629142}, {'vehicleId': 549336, 'year': 2012, 'make': 'Nissan', 'model': 'Altima', 'dealerId': 1842785779}, {'vehicleId': 643534740, 'year': 1979, 'make': 'Cheverolet', 'model': 'Corvette', 'dealerId': 1842785779}, {'vehicleId': 2107238088, 'year': 2016, 'make': 'Kia', 'model': 'Soul', 'dealerId': 357686040}, {'vehicleId': 7702607, 'year': 2004, 'make': 'MINI', 'model': 'Cooper', 'dealerId': 1265629142}])
        case1_result = {'dealers': [{'vehicles': [{'make': 'Mitsubishi', 'model': 'Gallant', 'vehicleId': 539873024, 'year': 2013}, {'make': 'Ford', 'model': 'F150', 'vehicleId': 278760250, 'year': 2009}, {'make': 'Kia', 'model': 'Soul', 'vehicleId': 2107238088, 'year': 2016}], 'dealerId': 357686040, 'name': 'House of Wheels'}, {'vehicles': [{'make': 'Bentley', 'model': 'Mulsanne', 'vehicleId': 1795478997, 'year': 2016}, {'make': 'Nissan', 'model': 'Altima', 'vehicleId': 549336, 'year': 2012}, {'make': 'Cheverolet', 'model': 'Corvette', 'vehicleId': 643534740, 'year': 1979}], 'dealerId': 1842785779, 'name': "Doug's Doozies"}, {'vehicles': [{'make': 'Honda', 'model': 'Accord', 'vehicleId': 1323953228, 'year': 2016}, {'make': 'Ford', 'model': 'F150', 'vehicleId': 2133416123, 'year': 2014}, {'make': 'MINI', 'model': 'Cooper', 'vehicleId': 7702607, 'year': 2004}], 'dealerId': 1265629142, 'name': "Bob's Cars"}]}
        ### id = Io5k42Kq1gg ###
        case2 = functions.get_answer([{'dealerId': 172315737, 'name': "Bob's Cars"}, {'dealerId': 38272333, 'name': "Doug's Doozies"}, {'dealerId': 72491398, 'name': 'House of Wheels'}],
                                     [{'vehicleId': 749048022, 'year': 2016, 'make': 'Bentley', 'model': 'Mulsanne', 'dealerId': 38272333}, {'vehicleId': 1033868780, 'year': 2016, 'make': 'Honda', 'model': 'Accord', 'dealerId': 172315737}, {'vehicleId': 554002136, 'year': 2012, 'make': 'Nissan', 'model': 'Altima', 'dealerId': 38272333}, {'vehicleId': 275756774, 'year': 2014, 'make': 'Ford', 'model': 'F150', 'dealerId': 172315737}, {'vehicleId': 894777743, 'year': 2009, 'make': 'Ford', 'model': 'F150', 'dealerId': 72491398}, {'vehicleId': 1979917392, 'year': 2013, 'make': 'Mitsubishi', 'model': 'Gallant', 'dealerId': 72491398}, {'vehicleId': 2119243805, 'year': 2004, 'make': 'MINI', 'model': 'Cooper', 'dealerId': 172315737}, {'vehicleId': 1622345691, 'year': 1979, 'make': 'Cheverolet', 'model': 'Corvette', 'dealerId': 38272333}, {'vehicleId': 766779581, 'year': 2016, 'make': 'Kia', 'model': 'Soul', 'dealerId': 72491398}])
        case2_result = {'dealers': [{'dealerId': 172315737, 'name': "Bob's Cars", 'vehicles': [{'vehicleId': 1033868780, 'year': 2016, 'make': 'Honda', 'model': 'Accord'}, {'vehicleId': 275756774, 'year': 2014, 'make': 'Ford', 'model': 'F150'}, {'vehicleId': 2119243805, 'year': 2004, 'make': 'MINI', 'model': 'Cooper'}]}, {'dealerId': 38272333, 'name': "Doug's Doozies", 'vehicles': [{'vehicleId': 749048022, 'year': 2016, 'make': 'Bentley', 'model': 'Mulsanne'}, {'vehicleId': 554002136, 'year': 2012, 'make': 'Nissan', 'model': 'Altima'}, {'vehicleId': 1622345691, 'year': 1979, 'make': 'Cheverolet', 'model': 'Corvette'}]}, {'dealerId': 72491398, 'name': 'House of Wheels', 'vehicles': [{'vehicleId': 894777743, 'year': 2009, 'make': 'Ford', 'model': 'F150'}, {'vehicleId': 1979917392, 'year': 2013, 'make': 'Mitsubishi', 'model': 'Gallant'}, {'vehicleId': 766779581, 'year': 2016, 'make': 'Kia', 'model': 'Soul'}]}]}
        self.assertEqual(case1, case1_result)
        self.assertEqual(case2, case2_result)

if __name__ == '__main__':
    unittest.main()