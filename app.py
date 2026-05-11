import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Prathamesh Sontakke | Portfolio", page_icon="💼", layout="centered")

# --- HEADER SECTION (Using native Streamlit formatting for perfect Dark/Light mode scaling) ---
st.title("Prathamesh Sontakke")
st.subheader("Project & Client Delivery Professional | Implementation Specialist")

# Contact Information in 3 Columns with emojis
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("📞 **(+91) 8208484319**")
with col2:
    st.markdown("📧 **[SontakkePrathamesh10@gmail.com](mailto:SontakkePrathamesh10@gmail.com)**")
with col3:
    st.markdown("🔗 **[LinkedIn Profile](https://www.linkedin.com/in/prathamesh-sontakke/)**")

st.divider()

# --- IMPACT NUMBERS (METRICS BIAS) ---
st.header("Key Delivery Milestones")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
with m_col1:
    st.metric(label="Global Projects", value="20+")
with m_col2:
    st.metric(label="RFPs Supported", value="15+")
with m_col3:
    st.metric(label="Webinars Coordinated", value="5+")
with m_col4:
    st.metric(label="Tier-1 Accounts", value="1 (Cambridge)")

st.divider()

# --- INTERACTIVE ROLE FIT SWITCHER ---
st.header("Understand My Value")
role_interest = st.selectbox(
    "Select your team's focus to see how I fit your requirement:",
    ["Implementation & Client Delivery", "Project Coordinator / Scrum Master", "Product / Business Analyst"]
)

if role_interest == "Implementation & Client Delivery":
    st.info(
        "💡 **Why I fit:** I specialize in taking a client from 'contract signed' to 'fully onboarded'. "
        "With my experience managing LIMS implementations, configuring system fields via JSON to match real-world workflows, "
        "and running software training demos, I ensure high client retention and zero-friction rollouts."
    )
elif role_interest == "Project Coordinator / Scrum Master":
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

st.divider()

# --- WORK EXPERIENCE ---
st.header("Professional Journey")

# Company 1: Krishagni (Primary Focus)
st.subheader("Krishagni Solutions")
st.markdown("*Member of Domain Staff (Project & Delivery Operations) | April 2025 – Present*")

st.markdown("""
- **Implementation Lead — University of Cambridge Project:** Spearheaded end-to-end LIMS software implementation and biobanking workflow configurations; managed key stakeholder communications and performed functional JSON updates to customize system attributes.
- **SaaS Delivery:** Successfully gathered enterprise requirements and onboarded clients for **20+ global healthcare SaaS projects** across the US, Europe, and Australia.
- **Pre-Sales Enablement:** Contributed to **15+ RFP/RFQ responses** and ran **20+ customized product demos** to align technical capabilities with prospective client workflows.
- **Strategy & Growth Support:** Collaborated directly with the leadership team to construct case studies and launch **5+ public product webinars** to drive post-implementation adoption.
""")

# Company 2: Urban Company
st.subheader("Urban Company")
st.markdown("*Business Operations & Analyst Associate | Dec 2024 – April 2025 (3 Months)*")

st.markdown("""
- **Operational Efficiency:** Built interactive Power BI tracking dashboards to analyze partner onboarding trends and resolve workflow bottlenecks.
- **Capacity Planning:** Executed demand-supply forecasting models across multiple service subcategories to optimize partner availability.
""")

st.divider()

# --- INTERACTIVE SKILLS TABS ---
st.header("Core Competencies")

tab1, tab2, tab3 = st.tabs(["📊 Project & Delivery", "🔄 Agile & Execution", "💻 Tech & Data"])

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

st.divider()

# --- NEXTLEAP FELLOWSHIP & ACADEMICS ---
st.header("Education & Development")

col_edu1, col_edu2 = st.columns(2)
with col_edu1:
    st.subheader("Upskilling")
    st.markdown("**Product Management Fellowship**")
    st.caption("NextLeap | Expected July 2026")
    st.markdown("**McKinsey Forward Learning Program**")
    st.caption("Leadership & Structured Problem Solving | 2025")
with col_edu2:
    st.subheader("Academics")
    st.markdown("**M.Sc. in Biotechnology**")
    st.caption("Nagpur University (7.84 CGPA) | 2024")
    st.markdown("**B.Sc. in Biotechnology**")
    st.caption("Kamla Nehru Mahavidyalaya (72.22%) | 2022")

st.divider()
st.caption("💡 *This interactive resume was built using Python & Streamlit.*")
