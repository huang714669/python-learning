import json
import os.path

def preAction():
#     fileDir = os.path.dirname(os.path.realpath('__file__'))
#     filename = os.path.join(fileDir, 'template','parameters.json')//this will work on windows
    parameters_path = os.path.join(os.path.dirname(__file__), 'template', 'parameters.json') #work on linux

    if os.path.exists(parameters_path):
         with open(parameters_path,'r' ) as f:
                json_data=json.loads(f.read())
                json_data['parameters']['virtualMachines_image_id']['value'] = "sa"
                json_data['parameters']['deployer_tag']['value'] = "2434"
                print(json_data)
                f.close()
         with open(parameters_path,'w' ) as f:
                json.dump(json_data,f)
                f.close
                
    else:
        print('Error: file parameter.json not exists')
preAction()     
