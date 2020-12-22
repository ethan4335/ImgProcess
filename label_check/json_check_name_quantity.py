import os


# read json home to dict
def read_json_path(json_path):
    json_dict = {}
    for root, dirs, files in os.walk(json_path):
        for file in files:
            json = os.path.join(root, file)
            if 'invalid' in json:
                continue
            name = os.path.splitext(os.path.basename(json))[0]
            json_dict[name] = json
    print('total valied json file quantity: %s' % len(json_dict.keys()))
    return json_dict


# read img home to dict
def read_img_path(img_home):
    img_dict = {}
    for root, dirs, files in os.walk(img_home):
        for file in files:
            img = os.path.join(root, file)
            name = os.path.splitext(os.path.basename(img))[0]
            img_dict[name] = img
    print('total valied img quantity: %s' % len(img_dict.keys()))
    return img_dict


def main():
    img_home = r'D:\work_source\CV_Project\datasets\label_check\img\20201211'
    img_home1 = r'D:\work_source\CV_Project\datasets\label_check\img\20201215'
    json_home = r'D:\work_source\CV_Project\datasets\label_check\label\5'


    json_dict = read_json_path(json_home)
    img_dict = read_img_path(img_home)
    img_dict.update(read_img_path(img_home1))
    print('img quantity: ',len(img_dict))
    count = 0
    for jk in json_dict.keys():
        if jk in img_dict:
            count = count + 1
        else:
            # print(jk)
            pass
    print(count)

if __name__ == '__main__':
    main()
