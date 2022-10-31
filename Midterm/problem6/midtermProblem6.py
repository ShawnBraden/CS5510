from fer import Video
from fer import FER
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import imageio

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def partA():
  # Put in the location of the video file that has to be processed
  location_videofile = "./Midterm/problem6/Video_One.mp4"

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

  emotions_values = [angry, disgust, fear, happy, sad, surprise, neutral]

  score_comparisons = pd.DataFrame(emotions, columns = ['Human Emotions'])
  score_comparisons['Emotion Value from the Video'] = emotions_values
  score_comparisons


def partB():
  # define a video capture object
  cap = cv2.VideoCapture(0)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter('./Midterm/problem6/screen_recording.avi', fourcc, 20.0, (640, 480))
  
  # The dataframe that will hold the emotions score for each frame of the live video feed
  score_comparisons = pd.DataFrame(columns = emotions)

  print("Original Dataframe", score_comparisons)

  emo_detector = FER(mtcnn=True)
  i = 0
  while(i < 10):
      ret, frame = cap.read()

      # Capture all the emotions on the image
      captured_emotions = emo_detector.detect_emotions(frame)

      if (not captured_emotions):
        continue

      dictionary = captured_emotions[0]["emotions"]
      individualImageEmotions = []

      for emotion in dictionary:
        individualImageEmotions.append(dictionary[emotion])

      score_comparisons.loc[len(score_comparisons.index)] = individualImageEmotions

      # Display the resulting frame
      cv2.imshow('frame', frame)
        
      # the 'q' button is set as the quitting button you may use any desired button of your choice
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

      i += 1

  # Create the csv file that will hold the emotions score
  score_comparisons.to_csv("./Midterm/problem6/emotionScore.csv", index=False)

  df = pd.read_csv("./Midterm/problem6/emotionScore.csv")
  df.plot(title="Emotions over time")

  cap.release()
  out.release() 
  cv2.destroyAllWindows()

def partD():

  # Read the image
  img = imageio.imread("./Midterm/problem6/Two_Face.jpeg")
  height,width,junk = img.shape

  # Cut the image in half
  width_cutoff = width // 2
  s1 = img[:, :width_cutoff]
  s2 = img[:, width_cutoff:]

  # Save each half
  imageio.imsave("./Midterm/problem6/face1.jpeg", s1)
  imageio.imsave("./Midterm/problem6/face2.jpeg", s2)

  image = plt.imread("./Midterm/problem6/face1.jpeg")
  image1 = plt.imread("./Midterm/problem6/face2.jpeg")

  # image = plt.imread("./Midterm/problem6/Two_Face.jpeg")


  emo_detector = FER(mtcnn=True)
  captured_emotions = emo_detector.detect_emotions(image)
  print("Captured Emotions: ", captured_emotions)

  captured_emotions = emo_detector.detect_emotions(image1)
  print("Captured Emotions: ", captured_emotions)

  # print(captured_emotions)
  plt.imshow(image)

  plt.imshow(image1)

  # Use the top Emotion() function to call for the dominant emotion in the image
  dominant_emotion, emotion_score = emo_detector.top_emotion(image)
  print(dominant_emotion, emotion_score)

  dominant_emotion, emotion_score = emo_detector.top_emotion(image1)
  print(dominant_emotion, emotion_score)


def main():
  partA()
  # partB()
  # partD()

  plt.show()
  
main()