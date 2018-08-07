import json
import os.path

def preAction():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, 'template','parameters.json')
    if os.path.exists(filename):
         with open(filename,'r' ) as f:
                json_data=json.loads(f.read())
                json_data['parameters']['virtualMachines_image_id']['value'] = "sa"
                json_data['parameters']['deployer_tag']['value'] = "2434"
                print(json_data)
                f.close()
         with open(filename,'w' ) as f:
                json.dump(json_data,f)
                f.close
                
    else:
        print('Error: file parameter.json not exists')
preAction()     
