import os
 
path = "C://Users//varun//OneDrive//Desktop//GALLERY//ALL"   #<ENTER YOUR PHOTOS FOLDER PATH>
dir_list = os.listdir(path)
 

#change the image tag if you have differvent extensions i.e : jpg, jpeg, png 
imgTag = """<a href={{ url_for('static', filename="imgName" ) }} type="image/jpg" data-lightbox="Model" data-title="images"><img src={{ url_for('static', filename="imgName" ) }} type="image/jpg"></a>"""
for word in dir_list:
  #this will generate all html image tags for all photos in a folder 
    print(imgTag.replace("imgName", word))
