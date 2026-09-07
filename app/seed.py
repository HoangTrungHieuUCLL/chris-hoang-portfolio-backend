"""Idempotent seed script: `python -m app.seed`. Upserts projects by slug so it's
safe to re-run whenever a new project needs adding — edit PROJECTS below and re-run."""

from app.database import Base, SessionLocal, engine
from app.models import Project

PROJECTS = [
    dict(
        slug="automated-sales-forecast-pipeline",
        name="Automated Sales Forecast Pipeline",
        description=(
            "End-to-end ETL/ELT pipeline for time-series sales data across eight IKEA "
            "Belgium stores, unifying inconsistent systems into one source of truth. "
            "Built ingestion, validation, and transformation stages that catch bad data "
            "before it reaches anyone downstream, plus the dashboard tooling on top."
        ),
        tech_stack=["Python", "SQL", "PostgreSQL", "Apache Airflow", "Google Cloud Platform", "Power BI"],
        category="Data & ML",
        organization="IKEA Belgium",
        year="2026",
        link_url=None,
        featured=True,
        sort_order=1,
    ),
    dict(
        slug="ai-talent-matching-system",
        name="AI-Powered Talent Matching System",
        description=(
            "Trained a customised BERT model with LayoutLM and DBSCAN clustering to "
            "automatically match candidates to roles from unstructured resume data."
        ),
        tech_stack=["Python", "BERT", "LayoutLM", "DBSCAN", "Machine Learning"],
        category="Data & ML",
        organization="IKEA Belgium",
        year="2026",
        link_url=None,
        featured=False,
        sort_order=2,
    ),
    dict(
        slug="sales-prediction-app",
        name="Sales Prediction App",
        description=(
            "Self-serve web app that lets store managers upload their own variables "
            "and get back predicted sales, turning a one-off ML analysis into a "
            "reusable internal tool."
        ),
        tech_stack=["Python", "Machine Learning", "Web App"],
        category="Data & ML",
        organization="IKEA Belgium",
        year="2026",
        link_url=None,
        featured=False,
        sort_order=3,
    ),
    dict(
        slug="faulty-gas-bottle-detection",
        name="Faulty Gas Bottle Detection",
        description=(
            "Went from raw, unlabeled physical inspection photos to a working YOLO "
            "object-detection model that flags faulty gas bottles on the line."
        ),
        tech_stack=["Python", "YOLO", "Computer Vision"],
        category="Data & ML",
        organization="PrimaGaz",
        year="2025",
        link_url=None,
        featured=True,
        sort_order=4,
    ),
    dict(
        slug="ai-food-recognition",
        name="AI Food Recognition for Calorie Tracking",
        description=(
            "Built and deployed a Shiny app powered by AI to automatically recognise "
            "similar food products for a calorie-tracker app's data team."
        ),
        tech_stack=["ShinyPython", "Machine Learning"],
        category="Data & ML",
        organization=None,
        year="2025",
        link_url=None,
        featured=False,
        sort_order=5,
    ),
    dict(
        slug="football-tactic-prediction",
        name="Football Tactic Prediction Model",
        description=(
            "Predictive model for OH Leuven that predicts when the opposing team "
            "switches from a defensive to an attacking shape, with 88% accuracy."
        ),
        tech_stack=["Python", "Machine Learning", "Random Forest"],
        category="Data & ML",
        organization="OH Leuven",
        year="2025",
        link_url=None,
        featured=False,
        sort_order=6,
    ),
    dict(
        slug="stroke-occurrence-prediction",
        name="Stroke Occurrence Prediction Model",
        description=(
            "Analysed clinical data and trained a Random Forest model to predict "
            "stroke occurrence, reaching 80% accuracy."
        ),
        tech_stack=["Python", "scikit-learn", "Random Forest"],
        category="Data & ML",
        organization=None,
        year="2025",
        link_url=None,
        featured=True,
        sort_order=7,
    ),
    dict(
        slug="belfius-event-management",
        name="Belfius Event Management Web App",
        description=(
            "Shipped a web app with a 10-member SCRUM team over five two-week "
            "sprints, replacing Google Forms for internal event management at a "
            "major Belgian bank and insurer."
        ),
        tech_stack=["TypeScript", "CSS", "Java", "Agile/SCRUM"],
        category="Web Development",
        organization="Belfius",
        year="2024",
        link_url=None,
        featured=False,
        sort_order=8,
    ),
    dict(
        slug="ai-accessibility-aid",
        name="AI Accessibility Aid for the Visually Impaired",
        description=(
            "Built a web app, browser extension, and Python tools that combine a "
            "large language model with OpenCV to help visually impaired users "
            "understand their surroundings."
        ),
        tech_stack=["React", "Python", "OpenCV", "LLM"],
        category="Web Development",
        organization=None,
        year="2024",
        link_url=None,
        featured=True,
        sort_order=9,
    ),
    dict(
        slug="automated-server-monitoring",
        name="Automated Server Monitoring",
        description=(
            "Built a VBA-powered spreadsheet that automatically tracks server "
            "alerts, cutting monitoring time from five hours to one."
        ),
        tech_stack=["Excel VBA"],
        category="Automation",
        organization=None,
        year="2023",
        link_url=None,
        featured=False,
        sort_order=10,
    ),
    dict(
        slug="mario-inspired-game",
        name="Mario-Inspired Game",
        description=(
            "A Mario-inspired platformer built with Python and PyGame for UCLL IT "
            "Talents Days."
        ),
        tech_stack=["Python", "PyGame"],
        category="Automation",
        organization="UCLL IT Talents Days",
        year="2023",
        link_url=None,
        featured=False,
        sort_order=11,
    ),
]


def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        for data in PROJECTS:
            existing = db.query(Project).filter(Project.slug == data["slug"]).first()
            if existing:
                for key, value in data.items():
                    setattr(existing, key, value)
            else:
                db.add(Project(**data))
        db.commit()
        print(f"Seeded {len(PROJECTS)} projects.")
    finally:
        db.close()


if __name__ == "__main__":
    run()
