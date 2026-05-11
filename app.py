import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Prathamesh Sontakke | Portfolio", page_icon="💼", layout="centered")

# --- RECRUITER-PREMIUM LIGHT-SLATE THEME (Times New Roman / Navy / Deep Gray) ---
st.markdown("""
    <style>
    /* Premium, soft light-slate background (highly readable, professional) */
    .stApp {
        background-color: #F1F5F9;
        color: #1E293B;
    }
    
    /* Strict layout constraints to reduce scrolling and tighten gaps */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 800px !important;
    }
    
    /* Enforce professional serif font across all elements */
    h1, h2, h3, h4, h5, p, li, span, label, div {
        font-family: 'Times New Roman', Times, serif !important;
    }
    
    /* Main Name Header - Bold Elegant Navy */
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 2px;
        text-align: center;
    }
    
    /* Subtitle - Professional Slate */
    .sub-title {
        font-size: 17px;
        font-style: italic;
        color: #475569;
        margin-bottom: 15px;
        text-align: center;
    }
    
    /* Standardized Section Headers with Clean Underline */
    .section-header {
        font-size: 20px;
        font-weight: bold;
        color: #1E3A8A;
        border-bottom: 2px solid #B45309; /* Warm bronze accent line */
        padding-bottom: 3px;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    
    /* Clean text styling to prevent "invisible text" on light backgrounds */
    p, li, span {
        color: #1E293B !important;
        font-size: 15px !important;
        line-height: 1.5 !important;
    }
    
    /* Dark Navy for subheadings so they never blend into the background */
    h3, .company-name {
        color: #0F172A !important;
        font-weight: bold !important;
        font-size: 18px !important;
        margin-top: 10px !important;
        margin-bottom: 2px !important;
    }
    
    /* Dynamic KPI scorecard block containers */
    .kpi-container {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .kpi-card {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 6px;
        padding: 10px;
        text-align: center;
        flex: 1;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .kpi-number {
        font-size: 24px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 1px;
    }
    .kpi-label {
        font-size: 12px;
        color: #475569;
        font-weight: bold;
    }
    
    /* Tighten gap spacing around Streamlit widgets */
    .stSelectbox {
        margin-bottom: 5px !important;
    }
    
    /* Hyperlink formatting */
    a {
        color: #1D4ED8 !important;
        text-decoration: none;
        font-weight: bold;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="main-title">Prathamesh Sontakke</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Project & Client Delivery Professional | Implementation Specialist</div>', unsafe_allow_html=True)

# Tight Contact Layout: Row 1 (Core Info), Row 2 (Profiles)
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

st.write("") # Micro divider spacing

# --- 1. HOW I CAN HELP YOUR TEAM (NOW AT THE TOP) ---
st.markdown('<div class="section-header">How I Can Help Your Team</div>', unsafe_allow_html=True)
role_interest = st.selectbox(
    "Select your team's objective to see my tailored alignment:",
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

# --- 2. KEY MILESTONES (BELOW PITCH) ---
st.markdown('<div class="section-header">Key Delivery Milestones</div>', unsafe_allow_html=True)

# Render Power BI style KPI scorecards
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

# --- 3. CORE COMPETENCIES ---
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

# --- 4. WORK EXPERIENCE (BOLDED COMPANY NAMES & CORRECTED INVISIBLE TEXT) ---
st.markdown('<div class="section-header">Professional Journey</div>', unsafe_allow_html=True)

# Krishagni Solutions
st.markdown("<div class='company-name'>Krishagni Solutions</div>", unsafe_allow_html=True)
st.markdown("*Member of Domain Staff (Project & Delivery Operations) | April 2025 – Present*")

st.markdown("""
- **Implementation Lead — University of Cambridge Project:** Spearheaded end-to-end software implementation and biobanking workflow setup; managed stakeholder communications and performed functional JSON updates to configure system attributes.
- **SaaS Delivery:** Gathered requirements and guided client onboarding for **20+ global healthcare SaaS projects** across US, European, and Australian research groups.
- **Pre-Sales Enablement:** Coordinated **20+ customized product demonstrations** and contributed to technical sections for **15+ RFP/RFQ responses**.
- **Social Media & Engagement (SME):** Managed company social media presence by regularly posting relevant industry updates and product insights on the company website and LinkedIn.
- **Strategy & Growth Support:** Partnered directly with leadership to draft case studies and launch **5+ webinars** to drive post-implementation system adoption.
""")

# Case Studies Sub-section with styled link buttons
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
st.markdown("<div class='company-name'>Urban Company</div>", unsafe_allow_html=True)
st.markdown("*Business Operations & Analyst Associate | December 2024 – April 2025 (3 Months)*")

st.markdown("""
- **Operational Efficiency:** Created interactive Power BI dashboards to analyze partner onboarding timelines and pinpoint operational bottlenecks.
- **Capacity Planning:** Executed demand-supply forecasting models across multiple service subcategories to optimize partner availability.
""")

# --- 5. PROTOTYPES & NEXTLEAP WORK (REDUCED GAP & CORRECTED HEADER COLOR) ---
st.markdown('<div class="section-header">Featured Projects & Prototyping</div>', unsafe_allow_html=True)
st.caption("Active builds and public learning case studies published during my NextLeap PM Fellowship:")

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.markdown("<h4 style='color:#0F172A !important; margin:0;'>Groww Pro Terminal</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px !important; margin-top:5px;'>Built an interactive portal to solve mutual fund research and IPO tracking complexities for everyday investors.</p>", unsafe_allow_html=True)
    st.markdown("[👉 View on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_buildinpublic-learninpublic-nextleap-ugcPost-7459264687650557952-a9dJ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

with p_col2:
    st.markdown("<h4 style='color:#0F172A !important; margin:0;'>Unlocking Voice</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px !important; margin-top:5px;'>Conducted structured user research analyzing the core mechanics, barriers, and preferences of ChatGPT voice search.</p>", unsafe_allow_html=True)
    st.markdown("[👉 View on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_unlocking-voice-search-ugcPost-7451698697589063680-73My?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

with p_col3:
    st.markdown("<h4 style='color:#0F172A !important; margin:0;'>Make.com Teardown</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px !important; margin-top:5px;'>Analyzed onboarding flows on Make.com, detailing friction points and proposing intuitive user retention loops.</p>", unsafe_allow_html=True)
    st.markdown("[👉 View on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_product-teardown-makecom-onboarding-ugcPost-7454208030000427008-IQUQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

# --- 6. EDUCATION & CERTIFICATIONS ---
st.markdown('<div class="section-header">Education & Certifications</div>', unsafe_allow_html=True)

col_edu1, col_edu2 = st.columns(2)
with col_edu1:
    st.markdown("<div class='company-name'>Upskilling</div>", unsafe_allow_html=True)
    st.markdown("**Product Management Fellowship**")
    st.caption("NextLeap | Expected July 2026")
    st.markdown("**McKinsey Forward Program**")
    st.caption("Leadership & Structured Problem Solving | 2025")
    st.markdown("**Youth Employment Program**")
    st.caption("TCS | 2022")
with col_edu2:
    st.markdown("<div class='company-name'>Academics</div>", unsafe_allow_html=True)
    st.markdown("**M.Sc. in Biotechnology**")
    st.caption("Nagpur University (7.84 CGPA) | 2024")
    st.markdown("**B.Sc. in Biotechnology**")
    st.caption("Kamla Nehru Mahavidyalaya (72.22%) | 2022")

st.divider()
st.caption("💡 *This interactive resume was built using Python and Streamlit.*")
