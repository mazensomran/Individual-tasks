import os
import requests
import yadisk
import cv2
import math

TOKEN = "y0_AgAAAAB0ev3aAAteQwAAAAD8jhCdAACO2KRnnoRNp7ixUIlt8t6afxVoTA"
URL = "/Downloads/TestInterviewVideo/"

def make_screenshots(video_path, output_dir, count):
    cap = cv2.VideoCapture(video_path)
    duration = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    interval = duration / count
    for i in range(count):
        cap.set(cv2.CAP_PROP_POS_MSEC, interval * (i + 1))
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(output_dir+'//snapshot_0000'+str(i+1)+'.jpg', frame)
    cap.release()

def main():
    disk = yadisk.Client(token=TOKEN)
    for folder in disk.listdir(URL):
        if folder.type == 'dir':
            for file in disk.listdir(folder.path):
                if file.type == 'file' and file.name.endswith('.mp4'):
                    disk.download(file.path,'C://Users//MSI//Desktop//mission1//'+str(file.name))
                    video_path = 'C://Users//MSI//Desktop//mission1//'+str(file.name)
                    video_name = file.name
                    output_dir ='C://Users//MSI//Desktop//mission1//' + str(file.name.split('.')[0])
                    os.mkdir(output_dir)

                    make_screenshots(video_path, output_dir, 5)
                    for snap in os.listdir(output_dir):
                        if snap.endswith('.jpg'):
                            disk.upload(output_dir+'//'+snap, URL+str(folder.name.split('.')[0])+'/'+snap)

                    print(f"Скриншоты видео {video_name} загружено эффективно.")
if __name__ == "__main__":
    main()
