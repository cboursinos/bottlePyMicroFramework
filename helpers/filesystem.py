# -*- coding: utf-8 -*-

from datetime import datetime
import time
# import model
import ujson as json
import os
import ujson


def create_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)
        os.chmod(name, 0755)
        os.chown(name, 33, 33)

def delete_path_vacation(data):
    os.remove(data)

def delete_path(data):
    path = data['path'][0]
    path_removed = path[1:]
    os.remove(path_removed)

def upload_custom_photos(save_path, upload):
    if len(upload) > 0:
        create_folder(save_path)
        for key in upload:
            name, ext = os.path.splitext(key.filename)
            if ext not in ('.png', '.jpg', '.jpeg'):
                return 'File extension not allowed.'
            if not os.path.exists(save_path+'/'+name+ext):
                key.save(save_path+'/'+name+ext)
                os.chmod(save_path+'/'+name+ext, 0755)
                os.chown(save_path+'/'+name+ext, 33, 33)