from Shrink_App.models import Record
import cv2
from django.core.files.base import ContentFile

def image_size_reducer(id):
    record = Record.objects.get(pk=id)
    record_img = record.image
    img_file = record_img.file

    # reading the image in opencv format
    img = cv2.imread(img_file.name, cv2.IMREAD_UNCHANGED)
    
    img_file.close()
    # storage, path = record_img.storage, record_img.path
    # storage.delete(path)

    # closing the image file for deletion
    img_file.close()

    width = 140
    height = 140
    dim = (width, height)

    # resizing the image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    # print(resized.shape)
    # saving the resizezd image
    ret, buf = cv2.imencode('.jpg', resized)
    content = ContentFile(buf.tobytes())
    img_name = "shrinked_image_" + str(id) + ".jpg"
    record.image.save(img_name, content)
    
    # deleting the original image file
    

def hook_size_reducer(task):
    print(task.result)