import streamlit as st
from dotenv import load_dotenv 
load_dotenv()               #to load all environment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi  #gets the idea from the video and retrieves the transcript (videos must be public)

genai.configure(api_key=os.getenv("GOOGLE_APT_KEY"))

prompt='''You are an advanced AI assistant specializing in video content analysis.
Given the full transcript of a YouTube video, your job is to deeply analyze and 
summarize the video in a way that conveys every important detail, theme, 
and nuance while ensuring the summary remains structured and easy to understand.'''

#getting the transcript data from youtube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]                                      #extracting the video id from the url
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)                 #to get the transcript from the video_id we got in the form of a list  
        
        transcript=""               
        for i in transcript_text:
            transcript+= " "+i["text"]              #appending one by one to form a paragraph

        return transcript
    
    except Exception as e:
        raise e

#getting the summary based on the prompt from google gemini
def generate_gemini_content(transcript_text,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("Youtube Video Summarizer")
youtube_link=st.text_input("Enter the Youtube Video Link: ")   #text input box to get the input link
if youtube_link:
    video_id=youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_container_width=True)   #this url is the default url where youtube thumbnails are stored when 
                                                                                     #you upload a video, and the reference is wrt the youtube video id

if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)
    if(transcript_text):
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes: ")
        st.write(summary)