import streamlit as st
from PIL import Image
from pathlib import Path
# Go up from /pages/ to /resume/
current_dir = Path(__file__).parent.parent

# Correct paths from the project root
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "arun_circle.png"
image_pic = current_dir / "image" / "creative-thinking.png"
st.markdown(
    """
    <style>
        div[data-testid="collapsedControl"] {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)
# Example Project Entries
project_list = [
    # Automation & Cloud Projects
    {
        "title": "Workflow Approval & Tracking System",
        "description": "Designed a leave and purchase approval system using Power Apps and Power Automate with real-time Power BI tracking, reducing turnaround time by 60%.",
        "tech_stack": "Power Apps, Power Automate, Power BI, SharePoint"
    },
    {
        "title": "Supply Chain Entry Automation",
        "description": "Developed a system for supply chain data entry and logging with automated validation and alerts, cutting manual entry errors by 80%.",
        "tech_stack": "Power Apps, SharePoint, Power Automate"
    },
    {
        "title": "Real-Time Event Pipeline",
        "description": "Built a Kafka-based pipeline to process order events in real time with Azure Functions triggering downstream services.",
        "tech_stack": "Apache Kafka, Azure Event Hub, Azure Functions, Python"
    },
    {
        "title": "Kubernetes-Based Web Deployment",
        "description": "Deployed React and Flask apps into Kubernetes (EKS) clusters using Docker and Helm with CI/CD for automated updates.",
        "tech_stack": "Kubernetes, Docker, AWS EKS, Helm, GitHub Actions"
    },
    {
        "title": "Scalable API Hosting on AWS",
        "description": "Hosted Node.js and Python APIs using EC2 and Elastic Beanstalk with autoscaling and load balancing for production readiness.",
        "tech_stack": "AWS EC2, Elastic Beanstalk, NGINX, Node.js, Python"
    },
    {
        "title": "AI-Driven Workflow Automation",
        "description": "Automated tasks like email parsing, form routing, and CRM updates using N8N and OpenAI, streamlining daily ops.",
        "tech_stack": "N8N, OpenAI, Python, Zapier"
    },

    # Power BI Dashboards
    {
        "title": "Sales Performance Dashboard",
        "description": "Visualized regional and product-wise sales KPIs, enabling real-time monitoring and strategic insights for sales leads.",
        "tech_stack": "Power BI, DAX, SQL"
    },
    {
        "title": "Finance Budget vs Actual Dashboard",
        "description": "Built dynamic visuals to compare actual vs forecasted spend across departments, improving budget visibility.",
        "tech_stack": "Power BI, Excel, SQL"
    },
    {
        "title": "HR Leave & Attrition Tracker",
        "description": "Created an interactive dashboard to track employee leaves, attrition trends, and department-level insights.",
        "tech_stack": "Power BI, SharePoint"
    },
    {
        "title": "Project Delivery & Timeline Tracker",
        "description": "Developed timeline-based dashboard to track milestones, delays, and task ownership across 10+ projects.",
        "tech_stack": "Power BI, MS Project"
    },
    {
        "title": "Customer Support Ticket Dashboard",
        "description": "Built support ticket resolution dashboard highlighting SLA compliance, response rates, and escalation trends.",
        "tech_stack": "Power BI, Power Automate"
    },
    {
        "title": "Procurement & Inventory Dashboard",
        "description": "Integrated procurement data to track vendor performance, stock levels, and reorder triggers.",
        "tech_stack": "Power BI, Excel, SQL"
    },
    {
        "title": "Website Analytics Dashboard",
        "description": "Visualized user behavior and funnel conversion using web analytics data, improving UX decisions.",
        "tech_stack": "Power BI, Google Analytics"
    },
    {
        "title": "Revenue Forecasting Dashboard",
        "description": "Created predictive visuals for quarterly revenue trends using historical sales and market data.",
        "tech_stack": "Power BI, Python"
    },
    {
        "title": "Supply Chain Fulfillment Dashboard",
        "description": "Monitored shipment status, delays, and fulfillment SLAs across vendors and regions.",
        "tech_stack": "Power BI, SQL"
    },
    {
        "title": "IT Infrastructure Monitoring Dashboard",
        "description": "Displayed server uptime, downtime incidents, and alert logs for proactive infrastructure management.",
        "tech_stack": "Power BI, Azure Monitor"
    }
]
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
def showproject():

    for project in project_list:
        st.markdown(f"""
        ### {project['title']}
        🛠️ {project['tech_stack']}  
        {project['description']}
        """)
        st.write('\n')  # space between projects

