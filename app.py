import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Prathamesh Sontakke | Portfolio", page_icon="💼", layout="centered")

# --- EXECUTIVE DARK/GOLD THEMING ---
st.markdown("""
    <style>
    /* Main body background and font colors */
    .stApp {
        background-color: #0F172A;
        color: #F1F5F9;
    }
    
    /* Header/Title styling in premium Amber/Gold */
    .main-title {
        font-size: 40px;
        font-weight: 700;
        color: #FFBF00;
        margin-bottom: 2px;
    }
    .sub-title {
        font-size: 18px;
        font-weight: 400;
        color: #94A3B8;
        margin-bottom: 20px;
    }
    
    /* Section Dividers and Subheadings */
    h1, h2 {
        color: #FFBF00 !important;
        font-weight: 600 !important;
    }
    h3 {
        color: #E2E8F0 !important;
        font-weight: 500 !important;
    }
    
    /* Clean formatting for plain text & links */
    p, li {
        color: #E2E8F0 !important;
        font-size: 15px;
    }
    a {
        color: #38BDF8 !important; /* Bright sky blue for links to pop cleanly */
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    
    /* Adjust padding for a tighter, cleaner alignment */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="main-title">Prathamesh Sontakke</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Project & Client Delivery Professional | Implementation Specialist</div>', unsafe_allow_html=True)

# Contact Details Grid
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("📞 **+91 8208484319**")
with col2:
    st.markdown("📧 sontakkeprathamesh10@gmail.com")
with col3:
    st.markdown("🔗 [LinkedIn Profile](https://www.linkedin.com/in/prathamesh-sontakke-1920bb247/)")
with col4:
    st.markdown("💼 [Naukri Profile](https://www.naukri.com/mnjuser/profile)")

st.divider()

# --- KEY MILESTONES (THE GAME CHANGER) ---
st.header("Key Delivery Milestones")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
with m_col1:
    st.metric(label="Global Projects", value="3")
with m_col2:
    st.metric(label="RFPs Supported", value="15+")
with m_col3:
    st.metric(label="Webinars Coordinated", value="5+")
with m_col4:
    st.metric(label="Case Studies Created", value="2")

st.caption("*Note: These milestones were achieved during my tenure at Krishagni Solutions.*")

st.divider()

# --- CORE COMPETENCIES (SKILLS ABOVE EXPERIENCE) ---
st.header("Core Competencies")

tab1, tab2, tab3 = st.tabs(["📊 Project & Delivery", "🔄 Agile & Execution", "💻 Tech & Data"])

with tab1:
    st.markdown("""
    * **Stakeholder Coordination:** Managing and aligning expectations between technical development teams and non-technical clients.
    * **Requirement Gathering:** Translating complex client workflows into clear, structured functional requirements.
    * **Pre-Sales & RFPs:** Supporting the creation of delivery timelines and service scopes for formal RFP/RFQ responses.
    """)

with tab2:
    st.markdown("""
    * **Agile Frameworks:** Solid foundation in Scrum and Kanban processes.
    * **Project Tooling:** Experienced in tracking tasks, epics, and documentation using JIRA and Confluence.
    * **Process Mapping:** Experience visualizing system integration flows using BPMN and UML models.
    """)

with tab3:
    st.markdown("""
    * **Functional Configuration:** Basic comfort working with JSON schemas to establish user-defined system parameters.
    * **Data & Dashboards:** Power BI (building operational tracking boards) and Microsoft Excel.
    * **System Adaptation:** Hands-on experience configuring workflows for Enterprise Laboratory Information Systems (LIMS).
    """)

st.divider()

# --- INTERACTIVE ROLE FIT SWITCHER ---
st.header("How I Can Help Your Team")
role_interest = st.selectbox(
    "Select your hiring target to view tailored experience alignments:",
    ["Implementation & Client Delivery", "Project Coordinator / Scrum Master", "Product / Business Analyst"]
)

if role_interest == "Implementation & Client Delivery":
    st.info(
        "💡 **Tailored Alignment:** I specialize in taking enterprise customers from kickoff to go-live. "
        "With my experience managing LIMS implementations, configuring fields via JSON to mirror real-world laboratory setups, "
        "and running software walkthroughs, I ensure a smooth, high-retention onboarding journey."
    )
elif role_interest == "Project Coordinator / Scrum Master":
    st.info(
        "💡 **Tailored Alignment:** I focus on structure, timeline fidelity, and risk mitigation. "
        "I'm skilled in mapping milestones, using JIRA and Confluence to track active deliverables, and "
        "facilitating daily alignment across engineering and operations teams to resolve blockages early."
    )
else:
    st.info(
        "💡 **Tailored Alignment:** I act as an operational translator. I map complex user flows, write "
        "functional specifications, analyze onboarding bottlenecks using Power BI, and assist with pre-sales demos. "
        "My active Product Management training with NextLeap keeps me highly grounded in user-focused problem-solving."
    )

st.divider()

# --- WORK EXPERIENCE ---
st.header("Professional Journey")

# Krishagni Solutions
st.subheader("Krishagni Solutions")
st.markdown("*Member of Domain Staff (Project & Delivery Operations) | April 2025 – Present*")

st.markdown("""
- **Implementation Lead — University of Cambridge Project:** Spearheaded end-to-end software implementation and biobanking workflow setup; managed stakeholder communications and performed functional JSON updates to configure system attributes.
- **SaaS Delivery:** Gathered requirements and guided client onboarding for **20+ global healthcare SaaS projects** across US, European, and Australian research groups.
- **Pre-Sales Enablement:** Coordinated **20+ customized product demonstrations** and contributed to technical sections for **15+ RFP/RFQ responses**.
- **Social Media & Engagement (SME):** Managed company social media presence by regularly posting relevant industry updates and product insights on the company website and LinkedIn.
- **Strategy & Growth Support:** Partnered directly with leadership to draft case studies and launch **5+ public webinars** to drive post-implementation system adoption.
""")

# Case Studies Sub-section
st.markdown("##### **🔗 Published Case Studies I Supported:**")
cs_col1, cs_col2 = st.columns(2)
with cs_col1:
    st.link_button(
        "📄 TargetALS LIMS Implementation", 
        "https://www.openspecimen.org/case-studies/targetals-lims-implementation/"
    )
with cs_col2:
    st.link_button(
        "📄 Indiana University Genetics Biobank", 
        "https://www.openspecimen.org/case-studies/indiana-university-genetics-biobank-modernises-global-biobank-operations-with-openspecimen/"
    )

st.write("") # Spacer

# Urban Company
st.subheader("Urban Company")
st.markdown("*Business Operations & Analyst Associate | December 2024 – April 2025 (3 Months)*")

st.markdown("""
- **Operational Efficiency:** Created interactive Power BI dashboards to analyze partner onboarding timelines and pinpoint operational bottlenecks.
- **Capacity Planning:** Executed demand-supply forecasting models across multiple service subcategories to optimize partner availability.
""")

st.divider()

# --- PROTOTYPES & NEXTLEAP WORK ---
st.header("Featured Projects & Prototyping")
st.caption("Active builds and public learning case studies published during my NextLeap PM Fellowship:")

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.markdown("### **No-Code Chatbot Prototype**")
    st.markdown("Built and configured an AI Travel Assistant Bot using no-code workflows to streamline user itinerary planning.")
    st.markdown("[👉 View Project on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_buildinpublic-learninpublic-nextleap-ugcPost-7459264687650557952-a9dJ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

with p_col2:
    st.markdown("### **Unlocking Voice Search**")
    st.markdown("Conducted structured user research analyzing the core mechanics, barriers, and preferences of ChatGPT voice search.")
    st.markdown("[👉 View Research on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_unlocking-voice-search-ugcPost-7451698697589063680-73My?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

with p_col3:
    st.markdown("### **Make.com Product Teardown**")
    st.markdown("Analyzed user onboarding flows on Make.com, detailing friction points and proposing intuitive user retention loops.")
    st.markdown("[👉 View Teardown on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_product-teardown-makecom-onboarding-ugcPost-7454208030000427008-IQUQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

st.divider()

# --- EDUCATION & CERTIFICATIONS ---
st.header("Education & Certifications")

col_edu1, col_edu2 = st.columns(2)
with col_edu1:
    st.subheader("Upskilling")
    st.markdown("**Product Management Fellowship**")
    st.caption("NextLeap | Expected July 2026")
    st.markdown("**McKinsey Forward Learning Program**")
    st.caption("Leadership & Structured Problem Solving | 2025")
    st.markdown("**Youth Employment Program**")
    st.caption("TCS | 2022")
with col_edu2:
    st.subheader("Academics")
    st.markdown("**M.Sc. in Biotechnology**")
    st.caption("Nagpur University (7.84 CGPA) | 2024")
    st.markdown("**B.Sc. in Biotechnology**")
    st.caption("Kamla Nehru Mahavidyalaya (72.22%) | 2022")

st.divider()
st.caption("💡 *This interactive resume was built using Python and Streamlit.*")
