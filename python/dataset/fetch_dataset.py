import request_functions as rf
import numpy as np
import requests
import json


dataset_size = 500000

def main():

    downloaded = 0
    id_list = np.arange(900000)

    while downloaded < dataset_size:

        next_id = np.random.choice(id_list, replace=False)

        print('Download #{}:\tFetching kitty #{}'.format(downloaded+1, next_id))

        try:
            url = rf.get_url(next_id)
            rf.fetch_file(url, next_id)
            downloaded += 1

        except (requests.exceptions.RequestException, json.decoder.JSONDecodeError) as e:
            print(e)
            continue
        except Exception as e:
            print(e.__doc__)
            print(e.message)
            continue

        #rf.cooldown()



if __name__ == "__main__":
    main()
