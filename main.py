import cv2 as cv
import pandas as pd

subtitles=pd.read_csv("C:\\Users\\harsh\\OneDrive\\Desktop\\SR\\t2.3\\subtitles.csv")

winname="Video with Subtitles"
vid_path="C:\\Users\\harsh\\Downloads\\123.mp4"

vid=cv.VideoCapture(vid_path)

subtitle_index=0
subtitle_start=subtitles['start_time'].iloc[subtitle_index]
subtitle_end=subtitles['end_time'].iloc[subtitle_index]

length=len(subtitles['subtitle_text'].iloc[subtitle_index])

size=int(input("Enter the size of the subtitle text: \n"))
thickness=int(input("Enter the thickness of the subtitle text: \n"))

org=int(input("Organisation of the subtitles:\n1.Top\n2.Bottom"))

if org==1:
    kern=(840-size*length,160)
else:
    kern=(840-size*length,1960)


while True:
    ret, frame=vid.read()


    if not ret:
        break

    timer=vid.get(0)/1000.0
    

    if timer>=subtitle_start and timer<=subtitle_end :
        text=subtitles['subtitle_text'].iloc[subtitle_index]

        cv.putText(frame,text, (840-3*length,1960), cv.FONT_HERSHEY_COMPLEX, size, (255,255,255), thickness)

#160  1960
    if timer>=subtitle_end:
        subtitle_index+=1
        if subtitle_index < len(subtitles):
            subtitle_start = subtitles['start_time'].iloc[subtitle_index]
            subtitle_end = subtitles['end_time'].iloc[subtitle_index]
            length=len(subtitles['subtitle_text'].iloc[subtitle_index])
        else:
            subtitle_start = float('inf')

    cv.namedWindow(winname)
    cv.imshow(winname,cv.resize(frame,(1280,720)))

    if cv.waitKey(1)==ord('q'):
        break




vid.release()
cv.destroyAllWindows()

