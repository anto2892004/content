from openai import OpenAI
import streamlit as st

# Initialize the OpenAI client
client = OpenAI(api_key="")  # Replace with your API key

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    }
    .stSidebar {
        background: linear-gradient(135deg, #ffffff, #f0f2f6);
        border-right: 1px solid #e0e0e0;
    }
    .stButton button {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #2575fc, #6a11cb);
        transform: scale(1.05);
    }
    .stHeader {
        color: #2c3e50;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .stSubheader {
        color: #34495e;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .stMarkdown {
        color: #7f8c8d;
        font-size: 16px;
    }
    .content-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .content-text {
        color: #2c3e50;
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app title and description
st.markdown('<p class="stHeader">Social Media Content Generator 🚀</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="stMarkdown">Generate engaging captions or content for your social media posts.</p>',
    unsafe_allow_html=True,
)

# Sidebar for customizations
with st.sidebar:
    st.markdown('<p class="stSubheader">Customizations</p>', unsafe_allow_html=True)
    
    # Input for URL or topic
    input_type = st.radio(
        "What would you like to provide?",
        ("URL", "Topic")
    )
    
    if input_type == "URL":
        url = st.text_input("Enter the URL:")
        topic = None
    else:
        topic = st.text_input("Enter the topic:")
        url = None
    
    # Select tone
    tone = st.selectbox(
        "Select the tone of the content:",
        ("Persuasive", "Humorous", "Professional", "Casual", "Inspirational")
    )
    
    # Select platform
    platform = st.selectbox(
        "Select the platform:",
        ("Instagram", "X (Twitter)", "Facebook", "LinkedIn", "TikTok")
    )
    
    # Checkbox for hashtags
    use_hashtags = st.checkbox("Include hashtags?")

# Main content generation
if st.button("Generate Content", key="generate_button"):
    if (url or topic) and tone and platform:
        try:
            # Construct the prompt
            prompt = f"Write a {tone.lower()} social media post for {platform} about "
            if url:
                prompt += f"the content at this URL: {url}."
            else:
                prompt += f"this topic: {topic}."
            
            if use_hashtags:
                prompt += " Include relevant hashtags."
            
            # Call the OpenAI API
            response = client.chat.completions.create(
                model="gpt-4-turbo",  # Use GPT-4 Turbo
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                max_tokens=300,  # Adjust as needed
            )
            
            # Display the generated content
            generated_content = response.choices[0].message.content
            st.markdown('<p class="stSubheader">Generated Content</p>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="content-card"><p class="content-text">{generated_content}</p></div>',
                unsafe_allow_html=True,
            )
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all the required fields.")