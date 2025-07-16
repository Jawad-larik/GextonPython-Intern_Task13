import streamlit as st
from PIL import Image
from datetime import datetime
import pandas as pd
import base64
import os

# Page configuration
st.set_page_config(page_title="Jawad's Portfolio", layout="wide", page_icon="💼")

# ---------- Sidebar (Profile Section) ----------
with st.sidebar:
    # Profile Image
    img_path = "profile.jpg"
    if os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, width=140)
    else:
        st.warning("⚠️ Profile picture not found.")
    st.markdown("## **Muhammad Jawad Larik**")
    # Quick Bio
    st.markdown("""
    🎓 *IT Student - University of Sindh, Jamshoro*  
    💻 *Python Developer Intern*  
    📍 *Hyderabad, Pakistan* """)
    
    # Social Media
    st.markdown("### 🔗 Social Media Links:")
    st.markdown("""
    - [LinkedIn](https://www.linkedin.com/in/jawad-larik01)
    - [GitHub](https://github.com/jawad-larik01) """)

    # Theme Toggle
    st.markdown("---")
    st.markdown("### 🌗 Theme Mode")
    theme = st.radio("Choose Theme", ["Light", "Dark"], index=0)
    if theme == "Dark":
        st.markdown("""
            <style>
            body { background-color: #0e1117; color: white; }
            .stApp { background-color: #0e1117; }
            </style>
            """,
            unsafe_allow_html=True
        )
    # ---------- Languages ----------
    st.markdown("---")
    st.subheader("🌐 Languages")
    st.write("- English – Fluent\n- Urdu – Native\n- Sindhi – Native")

# ---------- Main Page ----------
st.header("👋 Welcome to my Digital Portfolio!")
st.subheader("Explore my journey, projects, and get in touch.")
st.markdown("---")

st.title("👨‍💻 Jawad Larik")
st.markdown("### Aspiring IT Professional | Python Developer & Tech Enthusiast")

# ---------- About Me ----------
st.markdown("---")
st.subheader("🎯 About Me")
st.write("""
I’m a passionate Information Technology student at the University of Sindh, Jamshoro, with hands-on experience in Python development, Web technologies, and IT automation.  
Currently interning at Gexton Education Institute, I'm actively engaged in real-world projects that boost my problem-solving and backend development skills.  
Driven by a hunger to learn and create, I continuously explore areas like AI, data science, and modern frameworks.  
I believe in growing by doing and aim to contribute purposefully to impactful tech innovations.
""")

# ---------- Education ----------
st.markdown("---")
st.subheader("🎓 Education")
st.write("""
- **BS Information Technology** – University of Sindh | *2024 - Ongoing*  
- **HSC/Intermediate (Pre-Engineering)** – Govt Boys Degree College Qasimabad | *2021 - 2023*  
- **Matriculation (Science)** – Agha Taj Muhammad High School | *2019 - 2021*
""")

# ---------- Experience ----------
st.markdown("---")
st.subheader("💼 Experience")
st.write("""
- **Python Developer Intern** – Gexton Education Institute *(Onsite, June 2025 - Present)*  
- **Python Developer Intern** – Code Alpha *(Remote, Jun 2023 - Aug 2023)*
""")

# ---------- Skills ----------
st.markdown("---")
st.subheader("🛠️ Skills")
st.markdown("""
- **Programming Languages**: Python, C++, Java, PHP, MySQL
- **Tools & Frameworks**: Streamlit, Git, MySQL, PostgreSQL
- **Designing Tools**: Adobe Photoshop, Adobe Illustrator
- **Other Skills**: Microsoft Office Suite, Maya 3D Modeling
""")

# ---------- Certifications ----------
st.markdown("---")
st.subheader("📑 Certifications")

certificates = [
    { "title": "Gaming & Animation Certification",
      "desc": "Acquired skills in game design and animation through a structured program.",
      "img": "certificate1.jpg",
      "link": "",
      "Completion date": "October 2024",
    },
    { "title": "Certified Fitness Trainer",
      "desc": "Earned from Fitness Academy (PVT) Ltd (IFCA FITNESS affiliated). Gained strong foundation in fitness, health, and wellness for personal growth and lifestyle improvement.",
      "img": "certificate2.jpg",
      "link": "",
      "Completion date": "January 2025",
    },
    { "title": "Certificate of Soft Skills",
      "desc": "Completed an online course by Google through Pakistan Freelancers Association, gaining key skills in communication, teamwork, and problem-solving for personal and professional growth.",
      "img": "certificate3.jpg",
      "link": "",
      "Completion date": "August 2024",
    },
    {"title": "Introduction to Artificial Intelligence",
      "desc": "Gained foundational knowledge in AI concepts and applications. Provided by SKillup-Simplilearn.",
      "img": "certificate4.jpg",
      "link": "",
      "Completion date": "November 2024",
    }
]
certs = st.columns(2)
for idx, cert in enumerate(certificates):
    with certs[idx % 2]:
        st.markdown(f"### {cert['title']}")
        st.write(cert["desc"])
        st.write(f"**Date:** {cert.get('Completion date', 'N/A')}")
        if cert.get("link"):
            st.markdown(f"[🔗 View Certificate]({cert['link']})")
        if cert.get("img") and os.path.exists(cert["img"]):
            st.image(cert["img"], width=250)
        else:
            st.info("🖼️ Image not found.")

# ---------- Projects ----------
st.markdown("---")
st.subheader("📁 My Projects")

projects = [
    {
        "title": "Real Estate Flyer Design",
        "desc": "Created as a final project for my Graphic Design course, with a focus on clean, modern aesthetics for a luxury real estate poster.",
        "tools": "Adobe Illustrator | Photoshop", 
        "link": "https://github.com/Jawad-larik/GraphicDesign-Project_Real-Estate-Flyer",
        "img": "project1.png", 
    },
    {
        "title": "AI-Based Resume Screening System",
        "desc": "Built an intelligent NLP-based app that automates resume screening with real-time results using Streamlit.",
        "tools": "Python | Streamlit | NLP",
        "link": "https://github.com/Jawad-larik/GextonPython-Intern_Task12",
        "img": "project2.png",
    },
]
proj_cols = st.columns(2)
for index, p in enumerate(projects):
    with proj_cols[index % 2]:
        st.markdown(f"### {p['title']}")
        st.write(p['desc'])
        st.write(f"**Tools Used:** {p['tools']}")
        st.markdown(f"[🔗 GitHub Link]({p['link']})")
        if os.path.exists(p['img']):
            st.image(p['img'], width=250)
        else:
            st.warning("⚠️ Image not found")
        
# ---------- Resume Download ----------        
def show_pdf(file_path):
    """Embed a PDF file in the app via base64 + iframe."""
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="350" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

st.markdown("---")
st.subheader("📄 Resume")
resume_path = "resume.pdf"
if os.path.exists(resume_path):
    with open(resume_path, "rb") as pdf:
        st.download_button("📥 Click here to download my latest resume (PDF)", data=pdf, file_name="Jawad_Resume.pdf")
    st.markdown("### Preview:")
    # st.pdf(resume_path)
    show_pdf(resume_path)
else:
    st.warning("⚠️ Resume file not found")

# ---------- Contact Form ----------
st.markdown("---")
st.subheader("📬 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send Message")
    
if submitted:
    import pandas as pd
    from datetime import datetime
    df = pd.DataFrame([[datetime.now(), name, email, message]],
                      columns=["Timestamp", "Name", "Email", "Message"])
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/contact_messages.csv", mode="a", header=not os.path.exists("data/contact_messages.csv"), index=False)
    st.toast("✅ Message sent!")
    st.balloons()  # Adds a fun balloon animation

# ---------- Footer ----------
st.markdown("---")
st.markdown("© 2025 Jawad Larik | Powered by Streamlit")
