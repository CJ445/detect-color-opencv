# detect-color-opencv

Virtual Env commands

- Creating
 ```
python -m venv venv
```
- Activating
 ```
venv\Scripts\activate.bat
```
- Listing
```
pip list
```
- Saving
```
pip freeze > requirements.txt
```
- Restoring
```
pip install -r requirements.txt
```
- Deactivating
```
deactivate
```

- In some cases,it is more convenient to shift from RGB to HSV colorspace depending on the usecase i.e. what we want to do with the images.
- Below is an image of how an HSV colorspace looks like.
-
![image](https://github.com/user-attachments/assets/398a2a5d-a1dc-40b6-af7d-7d3e7f039268)

- We'll be mostly be utilizing the Hue channel to differentiate between colors.
- Below is the top-view of the HSV colorspace cylinder
- 
![image](https://github.com/user-attachments/assets/4b74367e-d519-4c7f-9865-bffe2d4d27c3)

- To tell our program to detect all pixels from a given color, we have to give it the whole region as reference containing that color.
- For example, If we take the color yellow, below is the region that we have to specify to the program to recognize as yellow.
- 
![image](https://github.com/user-attachments/assets/55ef6d88-6c57-4eee-9cac-f3afe17a954e)
