import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Prathamesh Sontakke | Portfolio", page_icon="💼", layout="centered")

# --- EXECUTIVE DARK THEME & STABLE ALIGNMENT CSS ---
st.markdown("""
    <style>
    /* Premium dark dashboard background */
    .stApp {
        background-color: #0F172A;
        color: #F1F5F9;
    }
    
    /* Strict content width and alignment for uniform layout */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 850px !important;
        margin: 0 auto !important;
    }
    
    /* Clean typography with stable leading */
    h1, h2, h3, h4, h5, p, li, span, label, div {
        font-family: 'Times New Roman', Times, serif !important;
        line-height: 1.5 !important;
    }
    
    /* Title: Bold Deep Navy (adjust font sizes for hierarchy) */
    .main-title {
        font-size: 38px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 2px;
        text-align: center;
    }
    
    /* Subtitle: Clean gold accent */
    .sub-title {
        font-size: 18px;
        font-weight: 400;
        color: #D97706;
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* Section Headers: Navy with matching gold underline */
    .section-header {
        font-size: 22px;
        font-weight: bold;
        color: #1E3A8A;
        border-bottom: 2px solid #D97706;
        padding-bottom: 4px;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    
    /* CSS Grid for perfectly aligned KPI metrics scorecards */
    .kpi-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-bottom: 10px;
    }
    .kpi-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }
    .kpi-number {
        font-size: 28px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 2px;
    }
    .kpi-label {
        font-size: 13px;
        color: #475569;
        font-weight: bold;
    }
    
    /* High-contrast text & perfectly centered card alignment */
    p, li, div {
        color: #F1F5F9 !important;
    }
    
    /* Stable, centered card layout with even top/bottom padding */
    .stAlert {
        display: flex;
        justify-content: center !important;
        align-items: center !important;
        background-color: #EFF6FF !important;
        border: 1px solid #DBEAFE !important;
        color: #0F172A !important;
        padding: 20px !important;
        border-radius: 8px !important;
        margin-top: 10px !important;
    }
    
    /* Stable text center alignment inside the pitch card */
    .stAlert p, .stAlert li {
        color: #0F172A !important;
        text-align: center !important;
    }
    
    /* Clean dark gray text for subheadings (e.g., degree locations) */
    .text-stable {
        color: #94A3B8 !important;
    }
    
    /* Stable hyperlinking pop */
    a {
        color: #38BDF8 !important;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="main-title">Prathamesh Sontakke</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Project & Client Delivery Professional | Implementation Specialist</div>', unsafe_allow_html=True)

# Perfectly Aligned Contact Row
col_c1, col_c2 = st.columns(2)
with col_c1:
    st.markdown("<p style='text-align: center; margin:0;'>📞 <b>+91 8208484319</b></p>", unsafe_allow_html=True)
with col_c2:
    st.markdown("<p style='text-align: center; margin:0;'>📧 <b>sontakkeprathamesh10@gmail.com</b></p>", unsafe_allow_html=True)

col_p1, col_p2 = st.columns(2)
with col_p1:
    st.markdown("<p style='text-align: center; margin:0; margin-top: 4px;'>🔗 <b><a href='https://www.linkedin.com/in/prathamesh-sontakke-1920bb247/' target='_blank'>LinkedIn Profile</a></b></p>", unsafe_allow_html=True)
with col_p2:
    st.markdown("<p style='text-align: center; margin:0; margin-top: 4px;'>💼 <b><a href='https://www.naukri.com/mnjuser/profile' target='_blank'>Naukri Profile</a></b></p>", unsafe_allow_html=True)

st.write("") # Symmetrical spacing

# --- INTERACTIVE ROLE FIT SWITCHER (PERFECTLY ALIGNED CARD) ---
st.markdown('<div class="section-header">How I Can Help Your Team</div>', unsafe_allow_html=True)
role_interest = st.selectbox(
    "Select your hiring target to view my tailored alignment:",
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

# --- KEY MILESTONES (STABLE KPI SCORECARDS) ---
st.markdown('<div class="section-header">Key Delivery Milestones</div>', unsafe_allow_html=True)

# Symmetrical 4-column metrics layout using pure CSS grid
st.markdown("""
<div class="kpi-container">
    <div class="kpi-card">
        <div class="kpi-number">3</div>
        <div class="kpi-label">🌐 Global Projects</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-number">15+</div>
        <div class="kpi-label">📄 RFPs Supported</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-number">5+</div>
        <div class="kpi-label">🎤 Webinars Coordinated</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-number">2</div>
        <div class="kpi-label">📊 Case Studies Created</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.caption("*Note: These milestones were achieved during my tenure at Krishagni Solutions.*")


# --- CORE COMPETENCIES (STABLE HEIGHT PANELS) ---
st.markdown('<div class="section-header">Core Competencies</div>', unsafe_allow_html=True)

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
    * **Data & Dashboards:** Power BI (building operational tracking dashboards) and Microsoft Excel.
    * **System Adaptation:** Hands-on experience configuring workflows for Enterprise Laboratory Information Systems (LIMS).
    """)


# --- WORK EXPERIENCE (STABLE HEIGHT PANELS) ---
st.markdown('<div class="section-header">Professional Journey</div>', unsafe_allow_html=True)

# Krishagni Solutions
st.subheader("Krishagni Solutions")
st.markdown("*Member of Domain Staff (Project & Delivery Operations) | April 2025 – Present*")

st.markdown("""
- <span class="bullet-gold"><b>Implementation Lead — University of Cambridge Project:</b></span> Spearheaded end-to-end software implementation and biobanking workflow setup; managed stakeholder communications and performed functional JSON updates to configure system attributes.
- <span class="bullet-gold"><b>SaaS Delivery:</b></span> Gathered requirements and guided client onboarding for **20+ global healthcare SaaS projects** across US, European, and Australian research groups.
- <span class="bullet-gold"><b>Pre-Sales Enablement:</b></span> Coordinated **20+ customized product demonstrations** and contributed to technical sections for **15+ RFP/RFQ responses**.
- <span class="bullet-gold"><b>Social Media & Engagement (SME):</b></span> Managed company social media presence by regularly posting relevant industry updates and product insights on the company website and LinkedIn.
- <span class="bullet-gold"><b>Strategy & Growth Support:</b></span> Partnered directly with leadership to draft case studies and launch **5+ public webinars** to drive post-implementation system adoption.
""", unsafe_allow_html=True)

# perfectly aligned case study links
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

st.write("") # Tiny spacer

# Urban Company
st.subheader("Urban Company")
st.markdown("*Business Operations & Analyst Associate | December 2024 – April 2025 (3 Months)*")

st.markdown("""
- <span class="bullet-gold"><b>Operational Efficiency:</b></span> Created interactive Power BI dashboards to analyze partner onboarding timelines and pinpoint operational bottlenecks.
- <span class="bullet-gold"><b>Capacity Planning:</b></span> Executed demand-supply forecasting models across multiple service subcategories to optimize partner availability.
""")

# --- PROTOTYPES & NEXTLEAP WORK (STABLE HEIGHT PANELS) ---
st.markdown('<div class="section-header">Featured Projects & Prototyping</div>', unsafe_allow_html=True)
st.caption("Active builds and public learning case studies published during my NextLeap PM Fellowship:")

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.markdown("<h4 style='color:#FFFFFF !important; margin:0;'>Groww Pro Terminal</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px !important; margin-top:5px;'>Built an interactive portal to solve mutual fund research and IPO tracking complexities for everyday investors.</p>", unsafe_allow_html=True)
    st.markdown("[👉 View Project on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_buildinpublic-learninpublic-nextleap-ugcPost-7459264687650557952-a9dJ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

with p_col2:
    st.markdown("<h4 style='color:#FFFFFF !important; margin:0;'>Unlocking Voice</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px !important; margin-top:5px;'>Conducted structured user research analyzing the core mechanics, barriers, and preferences of ChatGPT voice search.</p>", unsafe_allow_html=True)
    st.markdown("[👉 View Research on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_unlocking-voice-search-ugcPost-7451698697589063680-73My?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

with p_col3:
    st.markdown("<h4 style='color:#FFFFFF !important; margin:0;'>Make.com Teardown</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px !important; margin-top:5px;'>Analyzed onboarding flows on Make.com, detailing friction points and proposing intuitive user retention loops.</p>", unsafe_allow_html=True)
    st.markdown("[👉 View Teardown on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_product-teardown-makecom-onboarding-ugcPost-7454208030000427008-IQUQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

# --- EDUCATION & CERTIFICATIONS (STABLE HEIGHT PANELS) ---
st.markdown('<div class="section-header">Education & Certifications</div>', unsafe_allow_html=True)

col_edu1, col_edu2 = st.columns(2)
with col_edu1:
    st.subheader("Upskilling")
    st.markdown("**Product Management Fellowship**")
    st.markdown("<span class='text-stable'>NextLeap | Expected July 2026</span>", unsafe_allow_html=True)
    st.markdown("**McKinsey Forward Learning Program**")
    st.markdown("<span class='text-stable'>Leadership & Structured Problem Solving | 2025</span>", unsafe_allow_html=True)
    st.markdown("**Youth Employment Program**")
    st.markdown("<span class='text-stable'>TCS Graduate Academy | 2022</span>", unsafe_allow_html=True)
with col_edu2:
    st.subheader("Academics")
    st.markdown("**M.Sc. in Biotechnology**")
    st.markdown("<span class='text-stable'>Nagpur University (7.84 CGPA) | 2022 - 2024</span>", unsafe_allow_html=True)
    st.markdown("**B.Sc. in Biotechnology**")
    st.markdown("<span class='text-stable'>Kamla Nehru Mahavidyalaya (72.22%) | 2019 - 2022</span>", unsafe_allow_html=True)

st.divider()
st.caption("💡 *This interactive resume was built using Python and Streamlit.*")
