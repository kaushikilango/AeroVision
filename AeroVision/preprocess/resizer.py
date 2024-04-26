import cv2,os

class Image():
    def __init__(self, image):
        self.image = image
    
    def shape(self):
        return self.image.shape
    
    def resize(self, width, height):
        self.image = cv2.resize(self.image, (width, height))
        return self.image
    

def batch_processing(method,data,output_data):
    if method == 'resize':
        for i in os.listdir(data):
            appender = '_' + data.split('/')[-1]
            image = Image(cv2.imread(data + '/' + i))
            image.resize(512, 512)
            directory = output_data
            filename = i.split('.')[0] + appender + '.png'
            if not os.path.exists(directory):
                os.makedirs(directory)
            cv2.imwrite(directory + '/' + filename, image.image)
    else:
        return [Image(cv2.imread(data + '/' + i)).shape for i in os.listdir(data)]