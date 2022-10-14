# We install the FER() library to perform facial recognition
# This installation will also take care of any of the above dependencies if they are missing
# pip install FER

from fer import Video
from fer import FER
import pandas as pd
import cv2
import matplotlib.pyplot as plt 


def partA():
  # Put in the location of the video file that has to be processed
  location_videofile = "./content/Video_One.mp4"

  # Build the Face detection detector
  face_detector = FER(mtcnn=True)
  # Input the video for processing
  input_video = Video(location_videofile)

  # The Analyze() function will run analysis on every frame of the input video. 
  # It will create a rectangular box around every image and show the emotion values next to that.
  # Finally, the method will publish a new video that will have a box around the face of the human with live emotion values.
  processing_data = input_video.analyze(face_detector, display=False)

  # We will now convert the analysed information into a dataframe.
  # This will help us import the data as a .CSV file to perform analysis over it later
  vid_df = input_video.to_pandas(processing_data)
  vid_df = input_video.get_first_face(vid_df)
  vid_df = input_video.get_emotions(vid_df)

  # Plotting the emotions against time in the video
  pltfig = vid_df.plot(figsize=(20, 8), fontsize=16).get_figure()

  # We will now work on the dataframe to extract which emotion was prominent in the video
  angry = sum(vid_df.angry)
  disgust = sum(vid_df.disgust)
  fear = sum(vid_df.fear)
  happy = sum(vid_df.happy)
  sad = sum(vid_df.sad)
  surprise = sum(vid_df.surprise)
  neutral = sum(vid_df.neutral)

  emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
  emotions_values = [angry, disgust, fear, happy, sad, surprise, neutral]

  score_comparisons = pd.DataFrame(emotions, columns = ['Human Emotions'])
  score_comparisons['Emotion Value from the Video'] = emotions_values
  score_comparisons


# Part B
def partB():
  # define a video capture object
  vid = cv2.VideoCapture(0)
    
  while(True):
        
      # Capture the video frame by frame
      ret, frame = vid.read()
    
      # Display the resulting frame
      cv2.imshow('frame', frame)
        
      # the 'q' button is set as the quitting button you may use any desired button of your choice
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

  # After the loop release the cap object
  vid.release()
  # Destroy all the windows
  cv2.destroyAllWindows()

def main():
  # partA()
  partB()

main()