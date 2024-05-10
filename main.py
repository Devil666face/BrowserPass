import os

# import csv
# import tempfile
from pathlib import Path
from firefox.decrypt import decrypt as firefox_decrypt
from chrome.decrypt import decrypt as chrome_decrypt

if __name__ == "__main__":
    # temp_dir = tempfile.gettempdir()
    # C:\Users\Docker\AppData\Local\Temp
    # file_path = Path(temp_dir) / "temp.csv"
    # print(file_path)
    chrome_creds = chrome_decrypt()
    firefox_creds = firefox_decrypt()
    # with open(
    #     file_path, mode="w", newline="", encoding="utf-8"
    # ) as decrypt_password_file:
    #     csv_writer = csv.writer(decrypt_password_file, delimiter="\t")
    for cred_dict in chrome_creds + firefox_creds:
        # csv_writer.writerow(
        #     [
        #         cred_dict["url"],
        #         cred_dict["user"],
        #         cred_dict["password"],
        #     ]
        # )
        print(cred_dict)

    print(Path.cwd())
    print(os.getcwd())
    print(os.path.abspath(os.path.curdir))
