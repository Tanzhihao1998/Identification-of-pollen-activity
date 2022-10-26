# Identification-of-pollen-activity
Run the platform / operating system: windows 10

![image-20211230184036296](https://user-images.githubusercontent.com/96815625/147744635-d797a534-9a05-4e44-8e0b-f135eea8b082.png)

                       ----------------------------------------direction for use----------------------------------------
1. Click on the Button2 "Select a folder to be detected"
2. The picture format supports TIF, JPG, and PNG formats. Note that the folder path should not contain Chinese characters and no other types of files than pictures in the folder. When selecting a folder and click OK, click Botton1 Start Detection
3. When click on Botton1 "start detection" will take up a lot of GPU resources, try not to do other operations on the computer, prevent software crash detection data loss, etc., after detection, the detection results will be displayed in the text box, the output content including the image name, image path and pictures belong to the details of the "live" and "die" labels of pollen quantity.
4. Click on Botton3, "Exit the program", and the program closes.
                       
                       ----------------------------------------requirements----------------------------------------

Cython
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.2
Pillow
PyYAML>=5.3.1
scipy>=1.4.1
tensorboard>=2.2
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.41.0
                    
                    ----------------------------------------how to start----------------------------------------
python app_ui.py
