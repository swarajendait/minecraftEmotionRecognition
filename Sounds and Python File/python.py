# import cv2
# from deepface import DeepFace
# import time
# from mcpi.minecraft import Minecraft
# from mcpi.entity import WOLF, SHEEP, ENDERMAN
# from playsound import playsound
# import mcpi_addons
#
# # Connect to the Minecraft world
# mc = Minecraft.create()
#
#
# # Initialize OpenCV video capture
# cap = cv2.VideoCapture(0)
#
# # Set a timer to check the emotion every 10 seconds
# emotion_check_interval = 25  # 10 seconds
# last_emotion_check_time = time.time()
#
# # Make Face Cascade
# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
# # Initialize dominant_emotion and last_spawn_time with appropriate values
# dominant_emotion = ""
# last_spawn_time = time.time()
#
#
# while True:
#     ret, frame = cap.read()
#
#     # Check if the frame is None (indicating an issue with the video source)
#     if frame is None:
#         break
#
#     current_time = time.time()
#
#     # Check if it's time to perform emotion analysis
#     if current_time - last_emotion_check_time >= emotion_check_interval:
#         result = DeepFace.analyze(frame, actions=('emotion'))
#
#         # Update dominant_emotion if a face is detected
#         if result and 'dominant_emotion' in result[0]:
#             dominant_emotion = result[0]['dominant_emotion']
#         else:
#             dominant_emotion = ""
#
#         last_emotion_check_time = current_time  # Update the last check time
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(gray, 1.1, 4)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     cv2.imshow('Original Video', frame)
#     # Check if dominant_emotion is "happy" and at least 10 seconds have passed since the last spawn
#     if dominant_emotion == "happy" and current_time - last_spawn_time >= emotion_check_interval:
#         x, y, z = mc.player.getTilePos()
#
#         # Use getHeight to find the Y-coordinate of the ground at the player's position
#         ground_height = mc.getHeight(x, z)
#         # Spawn the mob at player's X and Z coordinates with the ground_height
#         playsound("happy.mp3")
#         # Update the last_spawn_time to prevent spawning again for 10 seconds
#         last_spawn_time = current_time
#
#     if dominant_emotion == "fear" and current_time - last_spawn_time >= emotion_check_interval:
#         x, y, z = mc.player.getTilePos()
#
#         # Use getHeight to find the Y-coordinate of the ground at the player's position
#         ground_height = mc.getHeight(x, z)
#         # Spawn the mob at player's X and Z coordinates with the ground_height
#         entityVar = mc.spawnEntity(x, ground_height, z, ENDERMAN.id)
#         # Update the last_spawn_time to prevent spawning again for 10 seconds
#         last_spawn_time = current_time
#
#     if dominant_emotion == "surprised" and current_time - last_spawn_time >= emotion_check_interval:
#         x, y, z = mc.player.getTilePos()
#
#         # Use getHeight to find the Y-coordinate of the ground at the player's position
#         ground_height = mc.getHeight(x, z)
#         playsound("suspense.mp3")
#         # Spawn the mob at player's X and Z coordinates with the ground_height
#         entityVar = mc.spawnEntity(x, ground_height, z, ENDERMAN.id)
#         # Update the last_spawn_time to prevent spawning again for 10 seconds
#         last_spawn_time = current_time
#
#     if dominant_emotion == "sad" and current_time - last_spawn_time >= emotion_check_interval:
#         x, y, z = mc.player.getTilePos()
#
#         playsound("sad.mp3")
#
#         # Use getHeight to find the Y-coordinate of the ground at the player's position
#         ground_height = mc.getHeight(x, z)
#         # Spawn the mob at player's X and Z coordinates with the ground_height
#         # Update the last_spawn_time to prevent spawning again for 10 seconds
#         last_spawn_time = current_time
#
#     if dominant_emotion == "neutral" and current_time - last_spawn_time >= emotion_check_interval:
#         x, y, z = mc.player.getTilePos()
#
#         mc.postToChat("Come on man, Play the game and be more expressive physically dude!")
#
#         # Use getHeight to find the Y-coordinate of the ground at the player's position
#         ground_height = mc.getHeight(x, z)
#         # Spawn the mob at player's X and Z coordinates with the ground_height
#         # Update the last_spawn_time to prevent spawning again for 10 seconds
#         last_spawn_time = current_time
#
#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
import random

import cv2
from deepface import DeepFace
import time
from mcpi.minecraft import Minecraft
from mcpi.entity import WOLF, SHEEP, ENDERMAN, CHICKEN
import pygame

# Connect to the Minecraft world
mc = Minecraft.create()

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

# Set a timer for tracking "neutral" emotion
neutral_check_interval = 30  # 30 seconds
last_neutral_time = time.time()

# Initialize pygame mixer
pygame.mixer.init()

# Current Sound Variable
current_sound = None

# Set a timer to check the emotion every 10 seconds
emotion_check_interval = 10  # 10 seconds
last_emotion_check_time = time.time()

# Make Face Cascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize last_spawn_time with appropriate value
last_spawn_time = time.time()
dominant_emotion = ""

joke1 = "What happends to an illegally parked frog? .... It gets 'toad' away"
joke2 = "Why can't the Ender Dragon read a book? Because he always starts at the end!"
joke3 = "How does Steve keep fit? He runs around the block. "
joke4 = "What do you call a bear with no teeth? A gummy bear."
joke5 = "Knock Knock. Who's there? Tank. Tank who? Your Welcome"
joke6 = "Knowck Knowck. Whoes there? Nona. Nona Who? Nona your business, thats who.  *ooooo roasted*"


while True:
    ret, frame = cap.read()

    # Check if the frame is None (indicating an issue with the video source)
    if frame is None:
        break

    current_time = time.time()

    # Check if it's time to perform emotion analysis
    if current_time - last_emotion_check_time >= emotion_check_interval:
        result = DeepFace.analyze(frame, actions=('emotion'))

        # Update dominant_emotion if a face is detected
        if result and 'dominant_emotion' in result[0]:
            dominant_emotion = result[0]['dominant_emotion']
        else:
            dominant_emotion = ""

        last_emotion_check_time = current_time  # Update the last check time

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the detected emotion on the video frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Emotion: " + dominant_emotion, (50, 50), font, 1, (0, 255, 0), 2)

    cv2.imshow('Emotion Detection', frame)

    # Check and perform actions based on detected emotions
    if dominant_emotion == "happy" and current_time - last_spawn_time >= emotion_check_interval:
        x, y, z = mc.player.getTilePos()
        ground_height = mc.getHeight(x, z)
        mc.postToChat("You seem happy! Let's celebrate in Minecraft!")
        if current_sound != "happy.mp3":
            if current_sound is not None:
                pygame.mixer.music.stop()  # Stop the current sound
            pygame.mixer.music.load("happy.mp3")  # Load the new sound
            pygame.mixer.music.play()  # Play the new sound
            current_sound = "happy.mp3"
        mc.spawnEntity(x, ground_height, z, SHEEP.id)

        last_spawn_time = current_time

    if dominant_emotion == "fear" and current_time - last_spawn_time >= emotion_check_interval:
        x, y, z = mc.player.getTilePos()
        ground_height = mc.getHeight(x, z)
        if current_sound != "fear.mp3":
            if current_sound is not None:
                pygame.mixer.music.stop()  # Stop the current sound
            pygame.mixer.music.load("fear.mp3")  # Load the new sound
            pygame.mixer.music.play()  # Play the new sound
            current_sound = "fear.mp3"
        mc.postToChat("Fear detected! Beware of the Enderman!")
        mc.spawnEntity(x, y, z, ENDERMAN.id)
        mc.spawnEntity(x, y, z, ENDERMAN.id)
        last_spawn_time = current_time

    if dominant_emotion == "surprise" and current_time - last_spawn_time >= emotion_check_interval:
        x, y, z = mc.player.getTilePos()
        ground_height = mc.getHeight(x, z)
        if current_sound != "suspense.mp3":
            if current_sound is not None:
                pygame.mixer.music.stop()  # Stop the current sound
            pygame.mixer.music.load("suspense.mp3")  # Load the new sound
            pygame.mixer.music.play()  # Play the new sound
            current_sound = "suspense.mp3"
        mc.postToChat("Cock-a-doodle DOOOOOOOOOO!!!! Look around, you'll see a chicken! SURPRISE")
        mc.spawnEntity(x, y, z, CHICKEN.id)
        last_spawn_time = current_time

    if dominant_emotion == "sad" and current_time - last_spawn_time >= emotion_check_interval:
        x, y, z = mc.player.getTilePos()
        ground_height = mc.getHeight(x, z)
        if current_sound != "sad.mp3":
            if current_sound is not None:
                pygame.mixer.music.stop()  # Stop the current sound
            pygame.mixer.music.load("sad.mp3")  # Load the new sound
            pygame.mixer.music.play()  # Play the new sound
            current_sound = "sad.mp3"
        choice = [1, 2, 3, 4, 5, 6]
        selected_choice = random.choice(choice)
        if selected_choice == 1:
            mc.postToChat(joke1)
        if selected_choice == 2:
            mc.postToChat(joke2)
        if selected_choice == 3:
            mc.postToChat(joke3)
        if selected_choice == 4:
            mc.postToChat(joke4)
        if selected_choice == 5:
            mc.postToChat(joke5)
        if selected_choice == 6:
            mc.postToChat(joke6)

        mc.spawnEntity(x, ground_height, z, ENDERMAN.id)
        last_spawn_time = current_time



    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# import cv2
# from deepface import DeepFace
# import time
# from mcpi.minecraft import Minecraft
# from mcpi.entity import WOLF, SHEEP, ENDERMAN, CHICKEN
# import pygame
# import random
#
# # Connect to the Minecraft world
# mc = Minecraft.create()
#
# # Initialize OpenCV video capture
# cap = cv2.VideoCapture(0)
#
# # Initialize pygame mixer
# pygame.mixer.init()
#
# # Current Sound Variable
# current_sound = None
#
# # Set a timer to check the emotion every 10 seconds
# emotion_check_interval = 10  # 10 seconds
# last_emotion_check_time = time.time()
#
# # Set a timer for tracking "neutral" emotion
# neutral_check_interval = 30  # 30 seconds
# last_neutral_time = time.time()
#
# # Make Face Cascade
# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
# # Initialize last_spawn_time with appropriate value
# last_spawn_time = time.time()
# dominant_emotion = ""
#
# while True:
#     ret, frame = cap.read()
#
#     # Check if the frame is None (indicating an issue with the video source)
#     if frame is None:
#         break
#
#     current_time = time.time()
#
#     # Check if it's time to perform emotion analysis
#     if current_time - last_emotion_check_time >= emotion_check_interval:
#         result = DeepFace.analyze(frame, actions=('emotion'))
#
#         # Update dominant_emotion if a face is detected
#         if result and 'dominant_emotion' in result[0]:
#             dominant_emotion = result[0]['dominant_emotion']
#         else:
#             dominant_emotion = ""
#
#         last_emotion_check_time = current_time  # Update the last check time
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(gray, 1.1, 4)
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Display the detected emotion on the video frame
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(frame, "Emotion: " + dominant_emotion, (50, 50), font, 1, (0, 255, 0), 2)
#
#     cv2.imshow('Emotion Detection', frame)
#
#     # Check and perform actions based on detected emotions
#     if dominant_emotion == "happy" and current_time - last_spawn_time >= emotion_check_interval:
#         # ... (happy action)
#
#     if dominant_emotion == "fear" and current_time - last_spawn_time >= emotion_check_interval:
#         # ... (fear action)
#
#     if dominant_emotion == "surprise" and current_time - last_spawn_time >= emotion_check_interval:
#         # ... (surprise action)
#
#     if dominant_emotion == "sad" and current_time - last_spawn_time >= emotion_check_interval:
#         # ... (sad action)
#
#     # Check for "neutral" emotion and trigger a random emotion-based command if neutral for more than 30 seconds
#     if dominant_emotion == "neutral":
#         if current_time - last_neutral_time >= neutral_check_interval:
#             # Perform a random emotion-based command
#             random_emotion = random.choice(["happy", "fear", "surprise", "sad"])
#             if random_emotion == "happy":
#                 # ... (happy action)
#             elif random_emotion == "fear":
#                 # ... (fear action)
#             elif random_emotion == "surprise":
#                 # ... (surprise action)
#             elif random_emotion == "sad":
#                 # ... (sad action)
#
#             # Reset the last_neutral_time
#             last_neutral_time = current_time
#
#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


