from resizer import Image, batch_processing
from dotenv import load_dotenv
from io import BytesIO

if __name__ == '__main__':
    load_dotenv()
    databj = 'data/bj'
    output_data = 'preprocessed_data/'
    dataca = 'data/ca'
    batch_processing('resize', databj, output_data)
    batch_processing('resize', dataca, output_data)