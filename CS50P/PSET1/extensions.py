#Extensions
file = input("File Name: ").strip().lower().split('.')

if file[-1] == 'gif':
    print("image/gif")
elif file[-1] == 'jpg' or file[-1] == 'jpeg':
    print("image/jpeg")
elif file[-1] == 'png':
    print("image/png")
elif file[-1] == 'pdf':
    print("image/pdf")
elif file[-1] == 'txt':
    print("image/txt")
elif file[-1] == 'zip':
    print("image/zip")
else:
    print("application/octet-stream")