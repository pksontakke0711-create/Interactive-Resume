import streamlit as st

# --- PAGE CONFIG (SWITCHED TO WIDE LAYOUT) ---
st.set_page_config(page_title="Prathamesh Sontakke | Portfolio", page_icon="💼", layout="wide")

# --- RECRUITER-PREMIUM FULL-WIDTH LIGHT THEME ---
st.markdown("""
    <style>
    /* Soft light slate-gray background */
    .stApp {
        background-color: #F8FAFC;
        color: #1E293B;
    }
    
    /* Expanded container for wide-screen readability layout */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1350px !important;
        margin: 0 auto !important;
    }
    
    /* Global Serif Font Rule for clean document styling */
    h1, h2, h3, h4, h5, p, li, span, label, div {
        font-family: 'Times New Roman', Times, serif !important;
    }
    
    /* Main Title with crisp deep blue text */
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 2px;
        text-align: center;
    }
    
    /* Elegant italicized subtitle */
    .sub-title {
        font-size: 20px;
        font-style: italic;
        color: #334155;
        margin-bottom: 12px;
        text-align: center;
        font-weight: bold;
    }
    
    /* Single Line Contact Row with tight margins */
    .contact-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .contact-row-single {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 30px;
        font-size: 16px !important;
        font-weight: bold;
        color: #0F172A !important;
    }
    
    /* Standardized Section Headers with Gold/Bronze Accent Line */
    .section-header {
        font-size: 24px;
        font-weight: bold;
        color: #1E3A8A;
        border-bottom: 2px solid #D97706; 
        padding-bottom: 4px;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    
    /* High-contrast text styling */
    p, li {
        color: #1E293B !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
    }
    
    /* Highlighted bold headers inside bullets */
    .bullet-bold {
        font-weight: bold;
        color: #0F172A;
    }
    
    /* Subheading styling for roles and companies */
    .company-title {
        font-size: 21px;
        font-weight: bold;
        color: #0F172A !important;
        margin-top: 10px !important;
        margin-bottom: 2px !important;
    }
    
    /* Date and location headers */
    .date-location {
        font-size: 15px !important;
        font-style: italic;
        color: #475569 !important;
        font-weight: bold;
        margin-bottom: 8px;
    }
    
    /* Recruiter Soft-Blue Grid Panels with Strict Uniform Heights */
    .blue-panel-flat {
        background-color: #EFF6FF !important;
        border: 1px solid #DBEAFE !important;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        min-height: 205px; /* Visual grid bounds across columns */
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    
    /* Clean Border-Only Cards strictly for Education to match height without blue bg */
    .border-only-card {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        min-height: 175px;
    }
    
    /* Fixed KPI Card styling layout */
    .kpi-container-fixed {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        margin-top: 5px;
        margin-bottom: 10px;
    }
    .kpi-card-fixed {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        flex: 1;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }
    .kpi-number-fixed {
        font-size: 30px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 1px;
    }
    .kpi-label-fixed {
        font-size: 13px;
        color: #0F172A;
        font-weight: bold;
    }
    
    /* Custom High-Contrast HTML Case Study Buttons */
    .btn-case-study {
        display: inline-block;
        background-color: #1E3A8A !important;
        color: #FFFFFF !important;
        font-weight: bold;
        font-size: 14px;
        text-align: center;
        text-decoration: none;
        padding: 8px 18px;
        border-radius: 6px;
        border: none;
        margin-right: 12px;
        margin-top: 8px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .btn-case-study:hover {
        background-color: #1D4ED8 !important;
        color: #FFFFFF !important;
        text-decoration: none;
    }
    
    /* High-contrast clean link styling */
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

# Contact Details Row Consolidated into a Single Clean Line
st.markdown("""
<div class="contact-container">
    <div class="contact-row-single">
        <span>📞 +91 8208484319</span>
        <span>📧 SontakkePrathamesh10@gmail.com</span>
        <span>🔗 <a href="https://www.linkedin.com/in/prathamesh-sontakke-1920bb247/" target="_blank">LinkedIn Profile</a></span>
        <span>💼 <a href="https://www.naukri.com/mnjuser/profile" target="_blank">Naukri Profile</a></span>
    </div>
</div>
""", unsafe_allow_html=True)


# --- 1. HOW I CAN HELP YOUR TEAM (FLAT HORIZONTAL GRID) ---
st.markdown('<div class="section-header">How I Can Help Your Team</div>', unsafe_allow_html=True)

help_col1, help_col2, help_col3 = st.columns(3)

with help_col1:
    st.markdown("""
    <div class="blue-panel-flat" style="min-height: 195px;">
        <h4 style="color:#1E3A8A !important; margin-top:0; font-size:18px; font-weight:bold;">🔄 Implementation & Client Delivery</h4>
        <p style="font-size:14.5px !important; margin-top:6px; margin-bottom:0;">
            <strong>Implementation & Onboarding Lead:</strong> I specialize in bringing enterprise customers from kickoff to go-live. 
            With my experience managing complex LIMS setups, executing custom JSON configurations, and guiding 20+ healthcare SaaS onboarding journeys, I ensure structured, low-friction integration.
        </p>
    </div>
    """, unsafe_allow_html=True)

with help_col2:
    st.markdown("""
    <div class="blue-panel-flat" style="min-height: 195px;">
        <h4 style="color:#1E3A8A !important; margin-top:0; font-size:18px; font-weight:bold;">📅 Project Coordinator / Scrum Master</h4>
        <p style="font-size:14.5px !important; margin-top:6px; margin-bottom:0;">
            <strong>Structure & Sprint Delivery:</strong> I focus on timeline execution and risk mitigation. I bring solid hands-on experience 
            mapping milestones, leveraging JIRA and Confluence to track epics and deliverables, and facilitating clear cross-functional communication to bypass operational bottlenecks.
        </p>
    </div>
    """, unsafe_allow_html=True)

with help_col3:
    st.markdown("""
    <div class="blue-panel-flat" style="min-height: 195px;">
        <h4 style="color:#1E3A8A !important; margin-top:0; font-size:18px; font-weight:bold;">📊 Product / Business Analyst</h4>
        <p style="font-size:14.5px !important; margin-top:6px; margin-bottom:0;">
            <strong>Operational Translator:</strong> I map complex user flows, draft functional specifications, coordinate client requirement gathering, 
            and translate technical requirements cleanly. My analytical background with Power BI enables me to build data-backed project health dashboards.
        </p>
    </div>
    """, unsafe_allow_html=True)


# --- 2. KEY DELIVERY MILESTONES ---
st.markdown('<div class="section-header">Key Delivery Milestones</div>', unsafe_allow_html=True)

st.markdown("""
<div class="kpi-container-fixed">
    <div class="kpi-card-fixed">
        <div class="kpi-number-fixed">3</div>
        <div class="kpi-label-fixed">🌐 Global Projects</div>
    </div>
    <div class="kpi-card-fixed">
        <div class="kpi-number-fixed">15+</div>
        <div class="kpi-label-fixed">📄 RFPs Supported</div>
    </div>
    <div class="kpi-card-fixed">
        <div class="kpi-number-fixed">5+</div>
        <div class="kpi-label-fixed">🎤 Webinars Coordinated</div>
    </div>
    <div class="kpi-card-fixed">
        <div class="kpi-number-fixed">2</div>
        <div class="kpi-label-fixed">📊 Case Studies Created</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='font-size:13.5px !important; font-style:italic; font-weight:bold; color:#475569; margin-top:4px;'>*Note: These milestones were achieved during my tenure at Krishagni Solutions.*</p>", unsafe_allow_html=True)


# --- 3. CORE COMPETENCIES (EQUALIZED HEIGHT PANEL GRID) ---
st.markdown('<div class="section-header">Core Competencies</div>', unsafe_allow_html=True)

comp_col1, comp_col2, comp_col3 = st.columns(3)

with comp_col1:
    st.markdown("""
    <div class="blue-panel-flat">
        <h4 style="color:#1E3A8A !important; margin-top:0; font-size:18px; font-weight:bold;">📋 Project & Delivery</h4>
        <ul style="margin-top:6px; padding-left:18px; font-size:14.5px !important; margin-bottom:0;">
            <li><strong>Stakeholder Coordination:</strong> Aligning expectations between technical developers and global client teams.</li>
            <li><strong>Requirement Gathering:</strong> Translating intricate customer biobanking setups into clear system parameters.</li>
            <li><strong>Pre-Sales Timelines:</strong> Supporting leadership with service scopes, timelines, and technical responses for RFPs.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with comp_col2:
    st.markdown("""
    <div class="blue-panel-flat">
        <h4 style="color:#1E3A8A !important; margin-top:0; font-size:18px; font-weight:bold;">🔄 Agile & Execution</h4>
        <ul style="margin-top:6px; padding-left:18px; font-size:14.5px !important; margin-bottom:0;">
            <li><strong>Agile Execution:</strong> Practical workflow tracking using Scrum and Kanban structures.</li>
            <li><strong>Project Tools:</strong> Solid daily usage of JIRA and Confluence for progress logs and specifications.</li>
            <li><strong>Process Mapping:</strong> Designing functional process flows using BPMN standards and UML frameworks.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with comp_col3:
    st.markdown("""
    <div class="blue-panel-flat">
        <h4 style="color:#1E3A8A !important; margin-top:0; font-size:18px; font-weight:bold;">💻 Tech & Data</h4>
        <ul style="margin-top:6px; padding-left:18px; font-size:14.5px !important; margin-bottom:0;">
            <li><strong>JSON Configurations:</strong> Performing functional JSON schema updates to adapt software properties.</li>
            <li><strong>Data & Analytics:</strong> Visualizing metrics using Power BI dashboards and Excel.</li>
            <li><strong>System Adaptation:</strong> Customizing laboratory information workflows for enterprise clients.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# --- 4. WORK EXPERIENCE ---
st.markdown('<div class="section-header">Professional Journey</div>', unsafe_allow_html=True)

# Krishagni Solutions
st.markdown("<div class='company-title'>Krishagni Solutions</div>", unsafe_allow_html=True)
st.markdown("<div class='date-location'>Member of Domain Staff (Project & Delivery Operations) | April 2025 – Present</div>", unsafe_allow_html=True)

st.markdown("""
- <span class="bullet-bold">Implementation Lead — University of Cambridge Project:</span> Managed end-to-end software deployment, managed stakeholder communication, and updated configuration schemas using JSON to mirror exact user workflows.
- <span class="bullet-bold">SaaS Delivery:</span> Led requirements gathering and client onboarding for <span class="bullet-bold">20+ global healthcare SaaS projects</span> across US, UK, and Australian research cohorts.
- <span class="bullet-bold">Pre-Sales Enablement:</span> Facilitated <span class="bullet-bold">20+ customized product demonstrations</span> and drafted technical content for <span class="bullet-bold">15+ RFPs and RFQs</span>.
- <span class="bullet-bold">Social Media & Engagement (SME):</span> Managed the company's social media presence by consistently publishing relevant biobanking industry insights on the official website and LinkedIn channels.
- <span class="bullet-bold">Strategy & Growth Support:</span> Partnered with leadership to draft and coordinate customer adoption case studies and launched <span class="bullet-bold">5+ public webinars</span>.
""", unsafe_allow_html=True)

st.markdown("<h5 style='font-size:16px; font-weight:bold; margin-top:10px; margin-bottom:2px;'>🔗 Published Case Studies I Authored & Supported:</h5>", unsafe_allow_html=True)
st.markdown("""
<div style="margin-bottom: 20px;">
    <a class="btn-case-study" href="https://www.openspecimen.org/case-studies/targetals-lims-implementation/" target="_blank">📄 TargetALS Case Study</a>
    <a class="btn-case-study" href="https://www.openspecimen.org/case-studies/indiana-university-genetics-biobank-modernises-global-biobank-operations-with-openspecimen/" target="_blank">📄 Indiana University Case Study</a>
</div>
""", unsafe_allow_html=True)

# Urban Company
st.markdown("<div class='company-title'>Urban Company</div>", unsafe_allow_html=True)
st.markdown("<div class='date-location'>Business Operations & Analyst Associate | December 2024 – April 2025</div>", unsafe_allow_html=True)

st.markdown("""
- <span class="bullet-bold">Operational Efficiency:</span> Built customized Power BI dashboards to track onboarding trends across 3+ service subcategories, boosting visibility for category leadership.
- <span class="bullet-bold">Capacity Planning:</span> Ran data-driven supply-demand forecasting models to optimize partner availability and pipeline metrics.
- <span class="bullet-bold">Process Streamlining:</span> Pinpointed process drop-offs and bottleneck workflows through structured analysis and systematic partner follow-ups.
""", unsafe_allow_html=True)


# --- 5. PROTOTYPES & NEXTLEAP WORK ---
st.markdown('<div class="section-header">Featured Projects & Prototyping</div>', unsafe
