---

# YouTube Video Summarizer  

An AI-powered tool that extracts and summarizes the transcript of YouTube videos using Google's Gemini API. This Streamlit-based application provides concise and structured summaries of video content, helping users grasp essential details quickly.  

## Features  

- Extracts video transcripts automatically  
- Uses **Google Gemini API** to generate detailed summaries  
- Displays the video thumbnail for easy reference  
- User-friendly interface with **Streamlit**  

## Installation  

1. **Clone the repository**:  
   ```sh
   git clone https://github.com/allen-reji/youtube-video-summarizer.git  
   cd youtube-video-summarizer  
   ```  

2. **Create a virtual environment (optional but recommended)**:  
   ```sh
   python -m venv venv  
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`  
   ```  

3. **Install dependencies**:  
   ```sh
   pip install -r requirements.txt  
   ```  

4. **Set up API keys**:  
   - Create a `.env` file in the project root directory:  
     ```sh
     touch .env  
     ```  
   - Add your API key inside `.env`:  
     ```
     GOOGLE_APT_KEY=your_google_api_key  
     ```  

## Usage  

1. **Run the application**:  
   ```sh
   streamlit run app.py  
   ```  
2. **Enter the YouTube video link** in the input field.  
3. **Click "Get Detailed Notes"** to generate a summarized version of the video content.  

##  Requirements  

This project uses the following dependencies:  

- `streamlit` - For the web-based UI  
- `youtube-transcript-api` - To extract transcripts from YouTube videos  
- `google-generativeai` - To generate AI-powered summaries  
- `python-dotenv` - To manage API keys securely  

## License  

This project is licensed under the MIT License.  

---

## Contact

Allen Reji - [allenreji@gmail.com](allenreji@gmail.com)
