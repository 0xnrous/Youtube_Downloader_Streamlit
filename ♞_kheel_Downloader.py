import base64
from pytube import YouTube
import streamlit as st
import time 
import os
import glob

st.set_page_config(
    page_title= 'Kheel ♘ ♞ Video Downloader',
    page_icon= '♘♞',
    layout="wide")

st.title(" Kheel ♘ ♞ YouTube Video Downloader")
st.sidebar.success("Made with ❤️ / \n Created by 0XNROUS")

def main():
    path = st.text_input('Enter URL of youtube video')
    option = st.selectbox(
        'Select type of download',
        ('highest_resolution [1080 - 720]', 'audio', 'lowest_resolution [360 - 240]')
    )     
    
    # read subfolders in a give directory based on the actual directory level
    foldernames_list = [os.path.basename(x) for x in glob.glob(f'{"/Volumes/0xnrous"}')]
    basepath = "/Volumes/0xnrous"
    basepath = "/Users/0xnrous/Developer/Streamlit_30Days/youtube_downloader"
    basepath = "/Users/0xnrous/Developer/Streamlit_30Days"
    # create selectbox with the foldernames
    chosen_folder = st.selectbox(label="Choose a folder", options=foldernames_list)

    # set the full path to be able to refer to it
    SAVE_PATH =  basepath + "/videos_Kheel/" + chosen_folder
      
    #SAVE_PATH = st.text_input("Save path", value ='/Users/0xnrous/Developer/Streamlit_30Days/youtube_downloader' , key="save_path")
    
    col1 , col2 = st.columns(2 , gap="large")
    with col1:
        #if st.button("DOWNLOAD"):
        if st.button("DOWNLOAD"):
            video_object =  YouTube(path) 
            st.snow()
            st.write("Title of Video : " + str(video_object.title))
            st.write("Length of Video : " + str(video_object.length))
            st.write("Number of Views on YOUTUBE : " + str(video_object.views))
            bar = st.progress(20)
            time.sleep(2)
            bar.progress(30 )
            time.sleep(3)
            bar.progress(50)
            time.sleep(3)
            bar.progress(60)
            time.sleep(3)
            bar.progress(70)
            time.sleep(3)
            bar.progress(80)
            time.sleep(3)
            time.sleep(5)    
            st.balloons()
            bar.progress(100)
            st.success("Video Downloaded")
                
            if option == 'audio':
                video_object.streams.get_audio_only().download(output_path=SAVE_PATH)
            elif option == 'highest_resolution [1080 - 720]':
                video_object.streams.get_highest_resolution().download(output_path=SAVE_PATH)
            elif option == 'lowest_resolution [360 - 240]':
                video_object.streams.get_lowest_resolution().download(output_path=SAVE_PATH)
    
    with col2:
        if st.button("VIEW PREVIEW"):
            st.header("Video Preview")
            st.video(path)
            

        
if __name__ == '__main__':
    main()
    