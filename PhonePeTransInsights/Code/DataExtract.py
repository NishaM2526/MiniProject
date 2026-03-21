# %%


import glob
import json
import pandas as pd

base_path = r"C:\Users\nisha\OneDrive\Desktop\Nisha\GUVI\MiniProject\PhonePeTransInsights\Data\data\**"

# Declare a common function to read the json filenames

def get_json_file_list(required_path):
    base_folder_path = glob.glob(base_path+required_path,recursive=True)
    json_file_list=[]
    for state_folder_name in base_folder_path:
        json_folder_names = glob.glob(state_folder_name+"\\**\\*.json",recursive=True)
        for json_file_names in json_folder_names:
            json_file_list.append(json_file_names)
    return json_file_list

# %%
# Function to get data (state name, year, quarter) from json file path

def get_json_data(json_file):
    state_file_path = json_file.split('\\state\\')
    agg_values = state_file_path[1].split('\\')
    state_name = agg_values[0]
    year = agg_values[1]
    json_file_name = agg_values[2]
    return state_name,year,json_file_name

# function to load the data from 'aggregated/transaction' folder present in pulse dataset
def get_aggregated_trans_load():
    json_file_list = get_json_file_list(r"\\aggregated\\transaction\\country\\india\\state\\")
    aggr_trans_value_dict = {'State':[],'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
        for values in json_data['data']['transactionData']:
            name = values['name']
            trans_count = values['paymentInstruments'][0]['count']
            trans_amount = values['paymentInstruments'][0]['amount']
            aggr_trans_value_dict['Transaction_type'].append(name)
            aggr_trans_value_dict['Transaction_count'].append(trans_count)
            aggr_trans_value_dict['Transaction_amount'].append(trans_amount)
            aggr_trans_value_dict['State'].append(agg_details[0])
            aggr_trans_value_dict['Year'].append(agg_details[1])
            aggr_trans_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(aggr_trans_value_dict)
    return df


# %%

# function to load the data from 'aggregated/user' folder present in pulse dataset
def get_aggregated_user_load():
    json_file_list = get_json_file_list(r"\\aggregated\\user\\country\\india\\state\\")
    aggr_user_value_dict = { 'State':[],'Year':[],'Quarter':[],'User_Device_brand':[], 'User_Device_count':[], 'User_Device_percentange':[]}

    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
        
        try:
            for values in json_data['data']['usersByDevice']:
                    brand = values['brand']
                    count = values['count']
                    perc = values['percentage']
                    aggr_user_value_dict['User_Device_brand'].append(brand)
                    aggr_user_value_dict['User_Device_count'].append(count)
                    aggr_user_value_dict['User_Device_percentange'].append(perc)
                    aggr_user_value_dict['State'].append(agg_details[0])
                    aggr_user_value_dict['Year'].append(agg_details[1])
                    aggr_user_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
        except:
             pass
    df=pd.DataFrame(aggr_user_value_dict)
    return df


# %%
# function to load the data from 'aggregated/insurance' folder present in pulse dataset
def get_aggregated_ins_load():
    json_file_list = get_json_file_list(r"\\aggregated\\insurance\\country\\india\\state\\")
    aggr_ins_value_dict = { 'State':[],'Year':[],'Quarter':[],'Payment_type':[],'Insurance_count':[], 'Insurance_amount':[]}

    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
        for values in json_data['data']['transactionData']:
            name = values['name']
            ins_count = values['paymentInstruments'][0]['count']
            ins_amount = values['paymentInstruments'][0]['amount']
            aggr_ins_value_dict['Payment_type'].append(name)
            aggr_ins_value_dict['Insurance_count'].append(ins_count)
            aggr_ins_value_dict['Insurance_amount'].append(ins_amount)
            aggr_ins_value_dict['State'].append(agg_details[0])
            aggr_ins_value_dict['Year'].append(agg_details[1])
            aggr_ins_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(aggr_ins_value_dict)
    return df


# %%

# function to load the data from 'map/transaction' folder present in pulse dataset
def get_map_trans_load():
    json_file_list = get_json_file_list(r"\\map\\transaction\\hover\\country\\india\\state\\")
    map_trans_value_dict = { 'State':[],'Year':[],'Quarter':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}
    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
        for values in json_data['data']['hoverDataList']:
            name = values['name'].split(' district')[0]
            trans_count = values['metric'][0]['count']
            trans_amount = values['metric'][0]['amount']
            map_trans_value_dict['District'].append(name)
            map_trans_value_dict['Transaction_count'].append(trans_count)
            map_trans_value_dict['Transaction_amount'].append(trans_amount)
            map_trans_value_dict['State'].append(agg_details[0])
            map_trans_value_dict['Year'].append(agg_details[1])
            map_trans_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(map_trans_value_dict)
    return df


# %%

# function to load the data from 'map/user' folder present in pulse dataset 20608
def get_map_user_load():
    json_file_list = get_json_file_list(r"\\map\\user\\hover\\country\\india\\state\\")
    map_user_value_dict = { 'State':[],'Year':[],'Quarter':[],'District':[], 'Total_Registered_users':[], 'Total_App_Opens':[]}
    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
        for key,values in json_data['data']['hoverData'].items():
            district = key.split(' district')[0]
            registered_user_count =values['registeredUsers']
            app_opens_count =values['appOpens']
            map_user_value_dict['District'].append(district)
            map_user_value_dict['Total_Registered_users'].append(registered_user_count)
            map_user_value_dict['Total_App_Opens'].append(app_opens_count)
            map_user_value_dict['State'].append(agg_details[0])
            map_user_value_dict['Year'].append(agg_details[1])
            map_user_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(map_user_value_dict)
    return df

# %%

# function to load the data from 'map/insurance' folder present in pulse dataset
def get_map_ins_load():
    json_file_list = get_json_file_list(r"\\map\\insurance\\hover\\country\\india\\state\\")
    map_ins_value_dict = { 'State':[],'Year':[],'Quarter':[],'District':[], 'Insurance_count':[], 'Insurance_amount':[]}
    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
        for values in json_data['data']['hoverDataList']:
            name = values['name'].split(' district')[0]
            ins_count = values['metric'][0]['count']
            ins_amount = values['metric'][0]['amount']
            map_ins_value_dict['District'].append(name)
            map_ins_value_dict['Insurance_count'].append(ins_count)
            map_ins_value_dict['Insurance_amount'].append(ins_amount)
            map_ins_value_dict['State'].append(agg_details[0])
            map_ins_value_dict['Year'].append(agg_details[1])
            map_ins_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(map_ins_value_dict)
    return df


# %%
# function to load the data from 'top/transaction' folder present in pulse dataset. District values will be loaded.
def get_top_trans_dist_load():
    json_file_list = get_json_file_list(r"\\top\\transaction\\country\\india\\state\\")
    top_trans_dist_value_dict = {'State':[], 'Year':[],'Quarter':[],
                                    'District':[],'District_Transaction_count':[],'District_Transaction_amount':[]}
    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
           
        for values in json_data['data']['districts']:
            district_name =values['entityName']
            dist_trans_count = values['metric']['count']
            dist_trans_amount = values['metric']['amount']
            top_trans_dist_value_dict['District'].append(district_name)
            top_trans_dist_value_dict['District_Transaction_count'].append(dist_trans_count)
            top_trans_dist_value_dict['District_Transaction_amount'].append(dist_trans_amount)
            top_trans_dist_value_dict['State'].append(agg_details[0])
            top_trans_dist_value_dict['Year'].append(agg_details[1])
            top_trans_dist_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(top_trans_dist_value_dict)
    return df


# %%

# function to load the data from 'top/transaction' folder present in pulse dataset. Pincode values will be loaded.
def get_top_trans_pincode_load():
    json_file_list = get_json_file_list(r"\\top\\transaction\\country\\india\\state\\")
    top_trans_pin_value_dict = {'State':[], 'Year':[],'Quarter':[],
                                'PinCode':[],'PinCode_Transaction_count':[],'PinCode_Transaction_amount':[]}
    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
           
        for values in json_data['data']['pincodes']:
            pincode_name =values['entityName']
            pin_trans_count = values['metric']['count']
            pin_trans_amount = values['metric']['amount']
            top_trans_pin_value_dict['PinCode'].append(pincode_name)
            top_trans_pin_value_dict['PinCode_Transaction_count'].append(pin_trans_count)
            top_trans_pin_value_dict['PinCode_Transaction_amount'].append(pin_trans_amount)
            top_trans_pin_value_dict['State'].append(agg_details[0])
            top_trans_pin_value_dict['Year'].append(agg_details[1])
            top_trans_pin_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(top_trans_pin_value_dict)
    return df
    


# %%
# function to load the data from 'top/user' folder present in pulse dataset. District values will be loaded.
def get_top_user_dist_load():
    json_file_list = get_json_file_list(r"\\top\\user\\country\\india\\state\\")
    top_user_dist_value_dict = {'State':[], 'Year':[],'Quarter':[],'District':[],'Registered_users':[]}
    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
           
        for values in json_data['data']['districts']:
            district_name =values['name']
            reg_user = values['registeredUsers']
            top_user_dist_value_dict['District'].append(district_name)
            top_user_dist_value_dict['Registered_users'].append(reg_user)
            top_user_dist_value_dict['State'].append(agg_details[0])
            top_user_dist_value_dict['Year'].append(agg_details[1])
            top_user_dist_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(top_user_dist_value_dict)
    return df
        


# %%

# function to load the data from 'top/user' folder present in pulse dataset. Pincodes values will be loaded.
def get_top_user_pincode_load():
    json_file_list = get_json_file_list(r"\\top\\user\\country\\india\\state\\")
    top_user_pin_value_dict = {'State':[], 'Year':[],'Quarter':[],'Pincodes':[],'Registered_users':[]}
    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
           
        for values in json_data['data']['pincodes']:
            pincodes =values['name']
            reg_user = values['registeredUsers']
            top_user_pin_value_dict['Pincodes'].append(pincodes)
            top_user_pin_value_dict['Registered_users'].append(reg_user)
            top_user_pin_value_dict['State'].append(agg_details[0])
            top_user_pin_value_dict['Year'].append(agg_details[1])
            top_user_pin_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(top_user_pin_value_dict)
    return df
        


# %%

# function to load the data from 'top/insurance' folder present in pulse dataset. District values will be loaded.
def get_top_ins_dist_load():
    json_file_list = get_json_file_list(r"\\top\\insurance\\country\\india\\state\\")
    top_ins_dist_value_dict = {'State':[], 'Year':[],'Quarter':[],
                            'District':[],'District_Insurance_count':[],'District_Insurance_amount':[]}
    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
           
        for values in json_data['data']['districts']:
            district_name =values['entityName']
            dist_ins_count = values['metric']['count']
            dist_ins_amount = values['metric']['amount']
            top_ins_dist_value_dict['District'].append(district_name)
            top_ins_dist_value_dict['District_Insurance_count'].append(dist_ins_count)
            top_ins_dist_value_dict['District_Insurance_amount'].append(dist_ins_amount)
            top_ins_dist_value_dict['State'].append(agg_details[0])
            top_ins_dist_value_dict['Year'].append(agg_details[1])
            top_ins_dist_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(top_ins_dist_value_dict)
    return df
        


# %%

# function to load the data from 'top/insurance' folder present in pulse dataset. Pincodes values will be loaded.
def get_top_ins_pincode_load():
    json_file_list = get_json_file_list(r"\\top\\insurance\\country\\india\\state\\")
    top_ins_pin_value_dict = {'State':[], 'Year':[],'Quarter':[],
                            'Pincode':[],'Pincode_Insurance_count':[],'Pincode_Insurance_amount':[]}
    for json_file in json_file_list:
        agg_details = get_json_data(json_file)
        data = open(json_file,'r')
        json_data = json.load(data)
           
        for values in json_data['data']['pincodes']:
            pincode =values['entityName']
            pin_ins_count = values['metric']['count']
            pin_ins_amount = values['metric']['amount']
            top_ins_pin_value_dict['Pincode'].append(pincode)
            top_ins_pin_value_dict['Pincode_Insurance_count'].append(pin_ins_count)
            top_ins_pin_value_dict['Pincode_Insurance_amount'].append(pin_ins_amount)
            top_ins_pin_value_dict['State'].append(agg_details[0])
            top_ins_pin_value_dict['Year'].append(agg_details[1])
            top_ins_pin_value_dict['Quarter'].append(int(agg_details[2].strip('.json')))
    
    df=pd.DataFrame(top_ins_pin_value_dict)
    return df
        




