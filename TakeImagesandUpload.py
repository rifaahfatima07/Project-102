import cv2
import random
import dropbox

def TakeImage():
    number = random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imName = 'Image' + str(number) + '.jpg'
        cv2.imwrite(imName,frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return imName

def upload_file(files_name):
    access_token = 'sl.A5YZggV2S9HAfUhD6DOa_zk3Uo3-s9Q7WzyuaXtd19mdkmuGtqEkhghOc5rCNgGHJIvKppmzZBGNkffIwE7keaCUwYr_OaEDDPhBGibyNqzR6EV0UdtuZ2roP9fo1pjdvhGQXhmprek'
    file = files_name
    file_from = file
    file_to="/First Class/"+(files_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

while(True):
    img = TakeImage()
    upload_file(img)