from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = "https://github.com/rayanramoul/rayanramoul/blob/master/Resume.pdf"
profile_pic = "https://avatars.githubusercontent.com/u/26028963?v=4"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Rayan Samy RAMOUL | Resume"
PAGE_ICON = ":wave:"
NAME = "Rayan Samy RAMOUL"
DESCRIPTION = """
I am Rayan Samy RAMOUL, a Research Engineer at InstaDeep specializing in LLMs and Computer Vision.
"""
EMAIL = "raysamram@gmail.com"
PHONE = "(+33) 0636052920"
LOCATION = "Paris, France"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rayan-samy-ramoul/",
    "GitHub": "https://github.com/rayanramoul",
    "Twitter": "https://twitter.com/raysamram",
}
PROJECTS = {
    "🏆 Active Object Localization with Deep Reinforcement Learning": "https://github.com/rayanramoul/Active-Object-Localization-Deep-Reinforcement-Learning",
    "🏆 ViT Pytorch Implementation": "https://github.com/rayanramoul/Visual-Transformer-PyTorch",
    "🏆 Multi-Agent RL for Hunt Environment": "https://github.com/rayanramoul/Multi-Agent-Reinforcement-Learning",
    "🏆 Deep Reinforcement Learning for Chess": "https://github.com/rayanramoul/Arcane-Chess",
    "🏆 Find: File explorer app based on NLP": "https://github.com/rayanramoul/Findr",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
hide_menu_style = """<style>
@import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;500;600;700&display=swap');


* {font-family: 'Readex Pro';}


.main {
    background-color: #ffeedc;
}
a {
    text-decoration: none;
    font-weight: 500;
}

a:hover {
    color: #d33682 !important;
    text-decoration: none;
}

ul {list-style-type: none;}

hr {
    margin-top: 0px;
    margin-bottom: 5%;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

img {
    border-radius: 50%;
}



</style>"""

st.markdown(hide_menu_style, unsafe_allow_html=True)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)
    st.write("📞", PHONE)
    st.write("📍", LOCATION)


# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Extensive experience in LLM Engineering, Software Engineering, and deploying models.
- ✔️ Proficient in training deep learning models, setting up and managing pipelines, and deploying models in production environments.
- ✔️ Skilled in implementing and maintaining CI/CD pipelines to streamline development and deployment processes.
- ✔️ Strong hands-on experience and knowledge in Python, PyTorch, and related technologies.
- ✔️ Proven ability to lead technical teams, manage codebases, review code, and ensure adherence to good software engineering practices.
- ✔️ Excellent communicator with a strong ability to interact with clients, understand their needs, and deliver AI solutions.
"""
)


# --- SKILLS ---
st.write("\n")
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Tools and Languages: Python, PyTorch, Git, OpenCV, Pandas, Scikit Learn, LATEX, Linux and Bash, NoSQL, SQL, FastAPI, C++, JavaScript and React, Streamlit.
- 📊 Quantitative Research: Deep Learning, Machine Learning, Computer Vision, Deep Reinforcement Learning (DQN), Mathematical Optimization, Mathematical Modeling, Advanced Algorithmic.
- 📚 Communication: French (Native), English (fluent), and Arabic (basic).
"""
)


# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Research Engineer - LLM | InstaDeep**")
st.write("Feb 2023 - Present | Paris, France")
st.write(
    """
- ► LLM Engineering
- ► Software Engineering
- ► Models training, pipelines, deployment
"""
)

# --- JOB 2
st.write("\n")
st.write("🚧", "**Confirmed AI Engineer | Quant AI Lab**")
st.write("Sep 2021 - Feb 2023 | Paris, France")
st.write(
    """
- ► Leading the deep learning and computer vision offer of the France team at Quant AI Lab.
- ► Trained and deployed multiple deep learning models on AWS. Created, maintained, and improved the computer vision product.
- ► Developed multiple deep learning models to answer client needs and wrapped them in APIs with React or Streamlit UIs.
- ► Created applications and demos to answer client needs, such as generative AI, unsupervised embedding of images, object tracking, and anomaly detection.
- ► Managed a technical team to achieve company goals. Managed code, reviewed code, and implemented good software engineering practices for deployment and CI/CD.
- ► Interacted with clients to help sell the AI offer and understand the field’s challenges. Helped clients integrate AI solutions.
"""
)

# --- JOB 3
st.write("\n")
st.write(
    "🚧",
    "**Research Intern in Deep Learning | Dynamic Meteorology Laboratory / Paris, Sorbonne University**",
)
st.write("Mar 2021 - Sep 2021 | Paris, France")
st.write(
    """
- ► Evaluated the contribution of different artificial intelligence techniques for classifying spatial organizations of low clouds observed by satellites.
- ► Handled Xarray dataset of geo satellite collection, applying the Image-Embedding technique using a combination of pre-trained models and fully-connected MLP.
- ► Utilized PCA for dimensionality reduction and computed clustering labels, with subsequent visualization of feature maps, GradCAM, and implementation of Deep Convolutional AutoEncoders and Deep Clustering.
- ► Presented results in a seminar, with results to be presented at an international conference in July 2022, and a paper for a peer-reviewed journal in preparation.
"""
)


# --- EDUCATION ---
st.write("\n")
st.subheader("Education")
st.write("---")
st.write(
    "🎓",
    "**Master 2 in Computer Vision (IMA) | Sorbonne University (ex: University of Pierre and Marie Curie U.P.M.C)**",
)
st.write("Sep 2021 | Paris, France")
st.write(
    """
- Grade: 15/20, High Honors. Ranked at the top of the internship grades with 18/20 and jury’s congratulations.
- Relevant Coursework: Deep Learning and Images Interpretation, Advanced Image Processing, Computer Vision, Medical Imaging.
"""
)

st.write("\n")
st.write("🎓", "**Entrepreneur Student | CELSA Higher-School Paris-Sorbonne**")
st.write("Jun 2022 | Paris, France")
st.write(
    """
- Relevant Coursework: Strategy, marketing and market research, building a business model, accounting and management, financing methods, intellectual property, corporate law, communication.
"""
)

st.write("\n")
st.write(
    "🎓",
    "**Bachelor in Mathematics and Computer Science | University of Science and Technology Houari Boumediene**",
)
st.write("Sep 2020 | Algiers, Algeria")


# --- CERTIFICATIONS ---
st.write("\n")
st.subheader("Certifications")
st.write("---")
st.write("📜", "**Amazon Web Services (AWS) Cloud Practitioner**")
st.write("Sep 2021 | Paris, France")

st.write("\n")
st.write("📜", "**Financial Markets from Yale University**")
st.write("Jun 2022 | Paris, France")


# --- PROJECTS & ACCOMPLISHMENTS ---
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
