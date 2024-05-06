from tqdm import tqdm
import os,cv2
import numpy as np
import random

def create_dataset(dir,classe,resize=True,resize_shape=(225,225),save=True,save_path='dataset.npz',normalize=False,augmentations=None,color_space='RGB'):
    '''
    Help on _synthesizer in AeroVision.dataset.synthesizer object:
    
    Parameters:
    dir : str
        Path to the directory containing the images.
    classe : str
        Name of the class to labelled to the images.
    resize : bool
        Whether to resize the images or not. Default is True.
    resize : tuple
        Size to which the images should be resized. Default is (225,225). Square inputs only.
    save : bool
        Whether to save the dataset or not. Default is True.
    save_path : str
        Path to save the dataset. Default is 'dataset.npz'.
    normalize : bool
        Normalization of images by numpy division. Default is False. Uses resize. If not square images, use False.
    augmentations : list
        List of augmentations to be applied. Default is None. Possible values are ['flip','rotate','blur','noise','brightness','contrast','saturation','hue'].
    color_space : str
        Color space of the images. Default is 'RGB'. Possible values are ['RGB','BGR','GRAY'].
    
    Returns:
        None
        Specify save or path to save the dataset.
    '''
    
    images = os.listdir(dir)
    master_data = []
    for i in tqdm(images):
        image_path = os.path.join(dir +'/' +i)
        img = cv2.imread(image_path)
        resized_images = cv2.resize(img,(225,225))
        if normalize:
            resized_images = resized_images/255.0
        if augmentations:
            for aug in augmentations:
                if aug == 'flip':
                    resized_images = cv2.flip(resized_images,1)
                elif aug == 'rotate':
                    resized_images = __augmentations(resized_images,'rotate')
                elif aug == 'blur':
                    resized_images = __augmentations(resized_images,'blur')
                elif aug == 'noise':
                    resized_images = __augmentations(resized_images,'noise')
                elif aug == 'brightness':
                    resized_images = __augmentations(resized_images,'brightness')
                elif aug == 'contrast':
                    resized_images = __augmentations(resized_images,'contrast')
                elif aug == 'saturation':
                    resized_images = __augmentations(resized_images,'saturation')
                elif aug == 'hue':
                    resized_images = __augmentations(resized_images,'hue')
        if color_space == 'BGR':
            pass
        elif color_space == 'GRAY':
            pass            
        master_data.append(resized_images)
    master_data = np.array(master_data)
    labels = [classe * master_data.shape[0]]
    np.savez('dataset.npz',data=master_data,labels=labels)
    

def __normalize(image):
    return image/255.0

def __color_space(image,color_space):
    pass
    
def __augmentations(image,type):
    match type:
        case 'flip':  
            hf_chance = random.randint(0,10000) / 10000
            vf_chance = random.randint(0,10000) / 10000
            if hf_chance > 0.5:
                aug_image = cv2.flip(image,1)
            if vf_chance > 0.5:
                aug_image = cv2.flip(image,0)
            return aug_image
        case 'rotate':
            rotate_angle = random.randint(0,360)
            rotate_chance = random.randint(0,10000) / 10000
            print(rotate_chance)
            print(rotate_angle)
            if rotate_chance > 0.2:
                rows,cols = image.shape[:-1]
                M = cv2.getRotationMatrix2D((cols/2,rows/2),rotate_angle,1)
                aug_image = cv2.warpAffine(image,M,(cols,rows))
                return aug_image
            return image
        case 'blur':
            blur_chance = random.randint(0,1)
            if blur_chance > 0.2:
                aug_image = cv2.GaussianBlur(image,(5,5),0)
                return aug_image
            return image
        case 'noise':
            noise_level = random.randint(0,10)
            noise = np.random.randn(*image.shape) * noise_level
            aug_image = image + noise
            return aug_image        
        case 'brightness':
            pass
        case 'contrast':
            pass
        case 'saturation':
            pass
        case 'hue':
            pass
