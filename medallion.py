import os

def create_layer(names, path):
    for name in names:
        if f'{name}_layer' not in os.listdir(path=path):
            os.mkdir(path=f'{path}/{name}_layer')


if __name__ == '__main__':
    pass