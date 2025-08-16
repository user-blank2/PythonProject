"""
file_name="apple.py"

with open(file_name,"w") as file:
    file.write("bankai")
    print("done")

"""
import json
file_name="C:\\Users\\deepa\\OneDrive\\Desktop\\new.json"
info={"1":1,"2":2,"3":3,"4":4}

with open(file_name,"a") as file:
    json.dump(info,file)

    print("THE file was created")