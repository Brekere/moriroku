# pip install python-barcode
# pip install pillow
# pip install qrcode

import json
import barcode
from barcode.writer import ImageWriter
import qrcode

def load_json_file(file_path):
    data = {}
    try:
        file = open(file_path)
        data = json.load(file)
        file.close() 
    except Exception as e:
        data = {"error": "No se pudo cargar el archivo", "info_error": str(e)} 
    return data

path_barcodes = "./barcodes/"
path_qrs = "./qrs/"
path_jsons = 'data/'
path_json_qr_components = path_jsons + 'components_qr_info.json'
path_json_containers_barcodes_info = path_jsons + 'containers_barcodes_info.json'

qr_components = load_json_file(path_json_qr_components)
bar_codes = load_json_file(path_json_containers_barcodes_info)
#print(qr_components)
#print(bar_codes)


barcodes = bar_codes["barcodes"]
l_qrs = qr_components["list"]

for code_ in barcodes:
    barcode_ = barcodes[code_]
    code = barcode_["id_barcode"]
    sample_barcode = barcode.get('code128', code, writer=ImageWriter())
    generated_filename = sample_barcode.save(path_barcodes+code)
    print('Generated Code 128 barcode image file name: ' + generated_filename)

for i in range(len(l_qrs)):
    qrs_info = l_qrs[i]
    print(qrs_info)
    info = qrs_info["inf_from_qr"]
    input_data = ""
    for key_line in info:
        input_data += info[key_line] +"\n"
    qr = qrcode.QRCode( version=1,box_size=10,border=5) 
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(path_qrs+"QR-"+str(i)+'.png')
    