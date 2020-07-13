import urllib.request
import json

# Step 1: Download JSON
# Step 2: Parse and extract properties
# Step 3: Generate TSV file
# Step 4: Provide automated test cases


keys = ["id", "url", "name", "type", "language", "status", "runtime", "premiered", "rating_average", "summary",
        "network_name", "image_original"]


def download_json():
    file = open('tv_show_urls.txt', 'r')
    shows = []
    for x in file:
        with urllib.request.urlopen(x) as url:
            d = json.loads(url.read().decode())
            shows.append(d)
    file.close()
    return shows


def parse_json(dict_data):
    json_list = []
    for key in keys:
        if key in dict_data:
            if '_' in key:
                json_list.append(dict_data[key.split('_')[0]][key.split('_')[1]])
            else:
                json_list.append(dict_data[key])

    return json_list


def generate_tsv(show_data):
    f = open('output_tv_shows.tsv', 'w')

    for x in keys:
        print(x, end='', file=f)
        if x != keys[len(keys) - 1]:
            print("\t", end='', file=f)

    for y in show_data:
        print(file=f)
        for z in y:
            print(z, end='', file=f)
            if z != y[len(y) - 1]:
                print("\t", end='', file=f)

    f.close()
    return


if __name__ == '__main__':
    tv_shows = download_json()
    parsed_shows = []
    for single_show in tv_shows:
        parsed_shows.append(parse_json(single_show))
    generate_tsv(parsed_shows)

    test_dict = {
        "rating": [{
            "average": "1"
        }],
        "network": [{
            "name": "2"
        }],
        "image": [{
            "original": "3"
        }]
    }
    print(test_dict)

    print(parse_json(test_dict))
