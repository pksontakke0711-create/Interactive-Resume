import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Prathamesh Sontakke | Portfolio", page_icon="💼", layout="centered")

# --- CUSTOM CSS FOR CLEAN LOOK ---
st.markdown("""
    <style>
    .main-title {
        font-size: 38px;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 20px;
        font-weight: 500;
        color: #4B5563;
        margin-bottom: 25px;
    }
    .section-header {
        font-size: 24px;
        font-weight: 600;
        color: #1E3A8A;
        border-bottom: 2px solid #E5E7EB;
        padding-bottom: 5px;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .highlight {
        font-weight: 600;
        color: #2563EB;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="main-title">Prathamesh Sontakke</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Project & Client Delivery Professional | Implementation Specialist</div>', unsafe_allow_html=True)

# Contact Information in 3 Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write("📱 (+91) 8208484319")
with col2:
    st.write("📧 [SontakkePrathamesh10@gmail.com](mailto:SontakkePrathamesh10@gmail.com)")
with col3:
    st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/prathamesh-sontakke/)") # Replace with your actual LinkedIn link path if needed

st.markdown("---")

# --- IMPACT NUMBERS (METRICS BIAS) ---
st.markdown('<div class="section-header">Key Delivery Milestones</div>', unsafe_allow_header=True)
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
with m_col1:
    st.metric(label="Global Projects", value="20+")
with m_col2:
    st.metric(label="RFPs Supported", value="15+")
with m_col3:
    st.metric(label="Webinars Led", value="5+")
with m_col4:
    st.metric(label="Tier-1 Accounts", value="1 (Cambridge)")

# --- INTERACTIVE ROLE FIT SWITCHER ---
st.markdown('<div class="section-header">Understand My Value (Select Your Team)</div>', unsafe_allow_html=True)
role_interest = st.selectbox(
    "Are you hiring for a...",
    ["Implementation & Client Delivery Role", "Project Coordinator / Scrum Master Role", "Product / Business Analyst Role"]
)

if role_interest == "Implementation & Client Delivery Role":
    st.info(
        "💡 **Why I fit:** I specialize in taking a client from 'contract signed' to 'fully onboarded'. "
        "With my experience managing LIMS implementations, configuring system fields via JSON to match real-world workflows, "
        "and running software training demos, I ensure high client retention and zero-friction rollouts."
    )
elif role_interest == "Project Coordinator / Scrum Master Role":
    st.info(
        "💡 **Why I fit:** I focus on structure and timeline execution. I'm skilled in Agile methodologies (Scrum/Kanban), "
        "tracking deliverables using JIRA/Confluence, and facilitating cross-functional alignment between engineering "
        "teams and business stakeholders to eliminate project bottlenecks."
    )
else:
    st.info(
        "💡 **Why I fit:** I act as a translator. I map complex user journeys, write functional requirements, "
        "analyze onboarding data (Power BI), and support strategic pre-sales efforts. My current Product Management "
        "Fellowship at NextLeap keeps me highly grounded in user-centric problem solving."
    )

# --- WORK EXPERIENCE ---
st.markdown('<div class="section-header">Professional Journey</div>', unsafe_allow_html=True)

# Company 1: Krishagni (Primary Focus)
st.markdown("### **Krishagni Solutions**")
st.caption("Member of Domain Staff (Project & Delivery Operations) | April 2025 – Present")

st.markdown("""
- **Implementation Lead — University of Cambridge Project:** Spearheaded end-to-end LIMS software implementation and biobanking workflow configurations; managed key stakeholder communications and performed functional JSON updates to customize system attributes.
- **SaaS Delivery:** Successfully gathered enterprise requirements and onboarded clients for **20+ global healthcare SaaS projects** across the US, Europe, and Australia.
- **Pre-Sales Enablement:** Contributed to **15+ RFP/RFQ responses** and ran **20+ customized product demos** to align technical capabilities with prospective client workflows.
- **Strategy & Growth Support:** Collaborated directly with the leadership team to construct case studies and launch **5+ public product webinars** to drive post-implementation adoption.
""")

# Company 2: Urban Company
st.markdown("### **Urban Company**")
st.caption("Business Operations & Analyst Associate | Dec 2024 – April 2025 (3 Months)")

st.markdown("""
- **Operational Efficiency:** Built interactive Power BI tracking dashboards to analyze partner onboarding trends and resolve workflow bottlenecks.
- **Capacity Planning:** Executed demand-supply forecasting models across multiple service subcategories to optimize partner availability.
""")

# --- INTERACTIVE SKILLS TABS ---
st.markdown('<div class="section-header">Core Competencies</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Project & Delivery", "Agile & Execution", "Tech & Data"])

with tab1:
    st.write("✔️ **Stakeholder Coordination:** Managing expectation alignment between technical developers and non-technical clients.")
    st.write("✔️ **Requirement Gathering:** Translating complex client processes into clear, structured functional requirements.")
    st.write("✔️ **Pre-Sales & RFPs:** Authoring delivery timelines and service scopes for formal RFP/RFQ responses.")

with tab2:
    st.write("✔️ **Agile Methodologies:** Certified-level understanding of Scrum and Kanban frameworks.")
    st.write("✔️ **Workspace Tools:** Managing tasks, epics, and documentation using JIRA and Confluence.")
    st.write("✔️ **Process Mapping:** Visualizing system integration flows using BPMN and UML.")

with tab3:
    st.write("✔️ **Functional Configurations:** Basic comfort working with **JSON** structure for workflow setup.")
    st.write("✔️ **Data Visualization:** Power BI (creating clean operation dashboards) and MS Excel.")
    st.write("✔️ **Active Upskilling:** Applying product-thinking frameworks through the **NextLeap PM Fellowship**.")

# --- NEXTLEAP FELLOWSHIP & ACADEMICS ---
st.markdown('<div class="section-header">Education & Professional Development</div>', unsafe_allow_html=True)

col_edu1, col_edu2 = st.columns(2)
with col_edu1:
    st.markdown("##### **Upskilling Initiatives**")
    st.write("🎓 **Product Management Fellowship**")
    st.caption("NextLeap | Expected July 2026")
    st.write("💼 **McKinsey Forward Learning Program**")
    st.caption("Leadership & Structured Problem Solving | 2025")
with col_edu2:
    st.markdown("##### **Academics**")
    st.write("🔬 **M.Sc. in Biotechnology**")
    st.caption("Nagpur University (7.84 CGPA) | 2024")
    st.write("🧬 **B.Sc. in Biotechnology**")
    st.caption("Kamla Nehru Mahavidyalaya (72.22%) | 2022")

st.markdown("---")
st.write("💡 *This interactive resume was custom-built by Prathamesh using Python and Streamlit.*")
