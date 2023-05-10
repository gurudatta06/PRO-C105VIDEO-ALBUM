import cv2
import os

path = "C:/Users/suraj/Downloads/PRO-C105-Project-Images-main/PRO-C105-Project-Images-main/Images"

images = []

for file in os.listdir(path):
    
    name, ext = os.path.splitext(file)
    
    if ext in [".jpg", ".jpeg", ".png"]:
        
        file_name = os.path.join(path, file)
        
        print(file_name)
        
        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])

height, width, channels = frame.shape

size = (width, height)

print(size)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count):
    
    img = cv2.imread(images[i])
    
    out.write(img)


print("All Done")

