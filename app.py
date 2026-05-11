import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Prathamesh Sontakke | Portfolio", page_icon="💼", layout="centered")

# --- CUSTOM CSS FOR PREMIUM RESUME THEME (TIMES NEW ROMAN / LIGHT SLATE / NAVY & GOLD) ---
st.markdown("""
    <style>
    /* Professional light slate resume background */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Times New Roman', Times, serif !important;
    }
    
    /* Document-style container constraints */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 800px !important;
    }
    
    /* Typography adjustments to Times New Roman */
    h1, h2, h3, h4, h5, p, li, span, label, div {
        font-family: 'Times New Roman', Times, serif !important;
    }
    
    /* Title: Bold Deep Navy */
    .main-title {
        font-size: 38px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 2px;
        text-align: center;
    }
    
    /* Subtitle: Slate Gray */
    .sub-title {
        font-size: 18px;
        font-style: italic;
        color: #475569;
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* Section Headers: Navy with Gold/Bronze underline */
    .section-header {
        font-size: 22px;
        font-weight: bold;
        color: #1E3A8A;
        border-bottom: 2px solid #D97706;
        padding-bottom: 4px;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    
    /* Custom CSS for Power BI-style KPI Number Plates */
    .kpi-container {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 10px;
    }
    .kpi-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        padding: 15px;
        text-align: center;
        flex: 1;
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
    
    /* Standard Text & Bullets: Dark Charcoal for crisp reading */
    p, li {
        color: #1E293B !important;
        font-size: 15.5px !important;
        line-height: 1.6 !important;
    }
    
    /* Custom links */
    a {
        color: #2563EB !important;
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

# Contact Details: Organized into 2 Clean Rows
row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.markdown("<p style='text-align: center; margin:0;'>📞 <b>+91 8208484319</b></p>", unsafe_allow_html=True)
with row1_col2:
    st.markdown("<p style='text-align: center; margin:0;'>📧 <b>sontakkeprathamesh10@gmail.com</b></p>", unsafe_allow_html=True)

st.write("") # Micro spacer

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    st.markdown("<p style='text-align: center; margin:0;'>🔗 <b><a href='https://www.linkedin.com/in/prathamesh-sontakke-1920bb247/' target='_blank'>LinkedIn Profile</a></b></p>", unsafe_allow_html=True)
with row2_col2:
    st.markdown("<p style='text-align: center; margin:0;'>💼 <b><a href='https://www.naukri.com/mnjuser/profile' target='_blank'>Naukri Profile</a></b></p>", unsafe_allow_html=True)

st.write("")

# --- KEY MILESTONES (POWER BI DASHBOARD CARDS) ---
st.markdown('<div class="section-header">Key Delivery Milestones</div>', unsafe_allow_html=True)

# Render HTML KPI Cards
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

# --- CORE COMPETENCIES (SKILLS HIGHER UP) ---
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

# --- INTERACTIVE ROLE FIT SWITCHER ---
st.markdown('<div class="section-header">How I Can Help Your Team</div>', unsafe_allow_html=True)
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

# --- WORK EXPERIENCE ---
st.markdown('<div class="section-header">Professional Journey</div>', unsafe_allow_html=True)

# Krishagni Solutions
st.subheader("Krishagni Solutions")
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

st.write("") # Spacer

# Urban Company
st.subheader("Urban Company")
st.markdown("*Business Operations & Analyst Associate | December 2024 – April 2025 (3 Months)*")

st.markdown("""
- **Operational Efficiency:** Created interactive Power BI dashboards to analyze partner onboarding timelines and pinpoint operational bottlenecks.
- **Capacity Planning:** Executed demand-supply forecasting models across multiple service subcategories to optimize partner availability.
""")

# --- PROTOTYPES & NEXTLEAP WORK ---
st.markdown('<div class="section-header">Featured Projects & Prototyping</div>', unsafe_allow_html=True)
st.caption("Active builds and public learning case studies published during my NextLeap PM Fellowship:")

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.markdown("### **Groww Pro Terminal**")
    st.markdown("Built an interactive portal to solve mutual fund research and IPO tracking complexities for everyday investors.")
    st.markdown("[👉 View Project on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_buildinpublic-learninpublic-nextleap-ugcPost-7459264687650557952-a9dJ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

with p_col2:
    st.markdown("### **Unlocking Voice Search**")
    st.markdown("Conducted structured user research analyzing the core mechanics, barriers, and preferences of ChatGPT voice search.")
    st.markdown("[👉 View Research on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_unlocking-voice-search-ugcPost-7451698697589063680-73My?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

with p_col3:
    st.markdown("### **Make.com Teardown**")
    st.markdown("Analyzed onboarding flows on Make.com, detailing friction points and proposing intuitive user retention loops.")
    st.markdown("[👉 View Teardown on LinkedIn](https://www.linkedin.com/posts/prathamesh-sontakke-1920bb247_product-teardown-makecom-onboarding-ugcPost-7454208030000427008-IQUQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD0Ptj4BmfSH22CaGLF6AtYLQsHYiMek9Gk)")

# --- EDUCATION & CERTIFICATIONS ---
st.markdown('<div class="section-header">Education & Certifications</div>', unsafe_allow_html=True)

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
