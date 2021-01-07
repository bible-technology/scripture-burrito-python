#!/usr/bin/env python3

import fileinput
import hashlib
import json
import os.path


def main():

    with fileinput.input() as f:
        data = json.load(f)

        for ingredient_path, ingredient_data in data["ingredients"].items():
            md5_checksum = ingredient_data["checksum"]["md5"]
            mime_type = ingredient_data["mimeType"]
            file_size = ingredient_data["size"]

            # @@@ check file exists first
            actual_size = os.path.getsize(ingredient_path)

            actual_md5_hash = hashlib.md5()
            actual_md5_hash.update(open(ingredient_path, "rb").read())
            actual_checksum = actual_md5_hash.hexdigest()

            print(ingredient_path)
            print(f"\tmimetype: {mime_type}")
            print(f"\tfilesize: {file_size} {actual_size}")
            print(f"\tchecksum: {md5_checksum} {actual_checksum}")
