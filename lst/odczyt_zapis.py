        dict_data['name'] = 'humidity'
        dict_data['value'] = round(sense.get_humidity(), 2)
        dict_data['unit'] = '%'
        dict_data['sensor'] = 'humidity sensor'
        tmp = dict_data
        tmp_json = json.dumps(tmp)
        # print(tmp_json)
        # save to file
        try:
            file = open("OneByOne/hum_p.json", "w")
            file.write(tmp_json)
        except:
            print("Write Error - RPY")
        finally:
            file.close()