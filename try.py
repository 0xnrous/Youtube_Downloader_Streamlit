
'''
st.write("Title of Video : " + str(video_object.title))
        st.write("Number of Views on YOUTUBE : " + str(video_object.views))
        st.write("Length of Video : " + str(video_object.length))
        st.write("Duration of Video : " + str(video_object.duration))
        st.write("Resolution of Video : " + str(video_object.resolution))
        st.write("Bitrate of Video : " + str(video_object.bitrate))
        st.write("File size of Video : " + str(video_object.filesize))
        st.write("File type of Video : " + str(video_object.mime_type))
        
        
        
        
        spinner during a process
>>> with st.spinner(text='In progress'):
>>>   time.sleep(3)
>>>   st.success('Done')




>>> bar = st.progress(50)
>>> time.sleep(3)
>>> bar.progress(100)

    st.write("Operating System Supported by Video Downloader")
    st.image('/Users/0xnrous/Developer/Streamlit_30Days/youtube_downloader/images/windows.svg')   
    st.image('/Users/0xnrous/Developer/Streamlit_30Days/youtube_downloader/images/apple.svg')
    st.image('/Users/0xnrous/Developer/Streamlit_30Days/youtube_downloader/images/linux.svg')

'''