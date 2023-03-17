import unittest
import json 

from asb_mori_paint import app
from asb_mori_paint.historical.models.mixing_process import db

class TestMixingProcess(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

        self.mixingprocess_dict = {
            #"id": 1,
            "id_worker": 1,
            "name_worker": "Arturo",
            "id_formula": 1,
            "id_filter": 1,
            "num_containers": 2,
            "conatiner_base_weight": 8000,
            "t_start": "2020-04-30T02:00:00.000Z",
            "t_end": "2020-04-30T04:00:00.000Z",
            "expected_viscosity_min" : 6,
            "expected_viscosity_max" : 7
        }

    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_upload_user(self):
        response = self.client.post('/api/processes', self.mixingprocess_dict)
        self.assertEqual(response.status_code, 200)
        mixingrocess = json.loads(response.data.decode('utf-8'))
        #self.assertEqual(mixingrocess['email'], 'joe@theodo.fr')
        print(mixingrocess)


if __name__ == '__main__':
    unittest.main()