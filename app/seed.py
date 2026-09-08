"""Idempotent seed script: `python -m app.seed`. Upserts projects by slug so it's
safe to re-run whenever a new project needs adding: edit PROJECTS below and re-run."""

from app.database import Base, SessionLocal, engine
from app.migrate import ensure_schema
from app.models import Project

PROJECTS = [
    dict(
        slug="automated-sales-forecast-pipeline",
        name="Automated Sales Forecast Pipeline",
        description=(
            "End-to-end ETL/ELT pipeline for time-series sales data across eight IKEA "
            "Belgium stores, unifying inconsistent systems into one source of truth. "
            "Built ingestion, validation, and transformation stages that catch bad data "
            "before it reaches anyone downstream, powering automated weekly sales forecasts."
        ),
        tech_stack=["Python", "SQL", "PostgreSQL", "Apache Airflow", "Google Cloud Platform"],
        category="Data & ML",
        organization="IKEA Belgium",
        year="2026",
        link_url=None,
        image_url="https://images.unsplash.com/photo-1726866672851-5b99c837603c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Bernd Dittrich",
        image_credit_url="https://unsplash.com/@hdbernd",
        featured=True,
        sort_order=1,
    ),
    dict(
        slug="store-kpi-dashboard",
        name="Cross-Store KPI Dashboard",
        description=(
            "Tracked down and reconciled inconsistent data from data owners across "
            "eight IKEA Belgium stores, then built a dashboard giving store managers "
            "direct access to KPIs and country-average benchmarks."
        ),
        tech_stack=["Power BI", "SQL", "Google Cloud Platform"],
        category="Data & ML",
        organization="IKEA Belgium",
        year="2026",
        link_url=None,
        image_url="https://images.unsplash.com/photo-1621264448270-9ef00e88a935?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Behnam Norouzi",
        image_credit_url="https://unsplash.com/@behy_studio",
        featured=False,
        sort_order=2,
    ),
    dict(
        slug="sales-impact-pricing-analysis",
        name="Sales Impact Analysis for Service Pricing",
        description=(
            "Used machine learning techniques to quantify the impact contribution of "
            "a proposed new service, providing the analysis that directly informed "
            "IKEA Belgium's pricing decision."
        ),
        tech_stack=["Python", "Machine Learning", "SQL"],
        category="Data & ML",
        organization="IKEA Belgium",
        year="2026",
        link_url=None,
        image_url="https://images.unsplash.com/photo-1745270917331-787c80129680?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Arturo Añez",
        image_credit_url="https://unsplash.com/@americanaez225",
        featured=False,
        sort_order=3,
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
        link_url="https://frontend2-production-34d6.up.railway.app",
        link_label="Try the Application",
        image_url="https://images.unsplash.com/photo-1664854953181-b12e6dda8b7c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Resource Database",
        image_credit_url="https://unsplash.com/@resourcedatabase",
        featured=False,
        sort_order=4,
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
        image_url="https://images.unsplash.com/photo-1765046255462-198d49d07dd1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Olli Kilpi",
        image_credit_url="https://unsplash.com/@space_parts",
        featured=False,
        sort_order=5,
    ),
    dict(
        slug="faulty-gas-bottle-detection",
        name="Faulty Gas Bottle Detection",
        description=(
            "Real-time computer-vision pipeline that inspects gas bottles moving on a "
            "conveyor belt, built from raw unlabeled inspection footage: extracted and "
            "labelled the frames, then trained the models. A fine-tuned YOLO11 detector "
            "locates each bottle, ByteTrack assigns it a stable ID across frames, and a "
            "ConvNeXtV2 classifier judges its condition (OK / NOT OK). A second YOLO model "
            "pinpoints the stamped tarra weight and recertification year, which EasyOCR "
            "reads after CLAHE contrast enhancement. Multi-frame majority voting and regex "
            "validation stabilise those readings, and any bottle past its recertification "
            "year is flagged automatically. Ships an annotated output video, a per-bottle "
            "CSV log, and a Tkinter demo GUI, evaluated against ground truth with a "
            "confusion matrix and an F3 score that deliberately weights recall over "
            "precision, since missing a faulty bottle costs far more than a false alarm."
        ),
        tech_stack=[
            "Python",
            "YOLO11",
            "Ultralytics",
            "PyTorch",
            "ConvNeXtV2",
            "ByteTrack",
            "EasyOCR",
            "OpenCV",
            "Computer Vision",
        ],
        category="Data & ML",
        organization="PrimaGaz",
        year="2025",
        link_url="https://github.com/FurquanMobeen/gass_GASSY",
        link_label="View the Code on GitHub",
        image_url="https://images.unsplash.com/photo-1730392165436-c00ec1fcb550?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Marco J Haenssgen",
        image_credit_url="https://unsplash.com/@marcohaenssgen",
        featured=True,
        sort_order=6,
    ),
    dict(
        slug="ai-food-recognition",
        name="AI Food Recognition for Calorie Tracking",
        description=(
            "Admin dashboard for a calorie-tracker app's data team, whose database fills "
            "up with user-scanned food products that arrive unverified or half-empty. "
            "Product text is cleaned and merged into one feature (lowercasing, Dutch "
            "stopword removal, word deduplication, NLTK Porter stemming), vectorised with "
            "TF-IDF and clustered with cosine-metric DBSCAN, so near-duplicate entries "
            "surface as ‘alike products’ that the team can merge into a single "
            "verified record. Built as a Shiny for Python dashboard on top of a Flask REST "
            "API and a PostgreSQL database: work queues are ordered by scan count so the "
            "most-scanned products get fixed first, and a comparison view puts two "
            "products’ text fields and nutrition values side by side with Plotly bar "
            "and radar charts. Also handled the messy start: repairing multi-layer "
            "encoding errors in the source CSV and modelling it into the Postgres schema "
            "the app runs on."
        ),
        tech_stack=[
            "Python",
            "Shiny for Python",
            "Flask",
            "PostgreSQL",
            "scikit-learn",
            "DBSCAN",
            "TF-IDF",
            "NLTK",
            "Plotly",
            "pandas",
        ],
        category="Data & ML",
        organization=None,
        year="2025",
        link_url="https://dashboard-production-7e41.up.railway.app",
        link_label="Try the Application",
        repo_url="https://github.com/HoangTrungHieuUCLL/DataVisualisation_2025-2026_FOOD_teamF3",
        image_url="https://images.unsplash.com/photo-1542459550-fb2d04bef698?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="NordWood Themes",
        image_credit_url="https://unsplash.com/@nordwood",
        featured=False,
        sort_order=7,
    ),
    dict(
        slug="football-tactic-prediction",
        name="Defense-to-Offense Transition Analysis",
        description=(
            "Built with a six-person team at OH Leuven's International Week, on one "
            "question: how does a side turn winning the ball back into an attack? "
            "Working from Belgian league event and tracking data, we defined the "
            "transition window as the 10 seconds before to 5 seconds after a recovery "
            "or interception, and picked Genk as the case study because they lead the "
            "league in both shots and ball recoveries. SQL queries against the match "
            "database feed pitch heatmaps (mplsoccer) showing where Genk win the ball, "
            "how compact their shape stays at the moment of recovery, and which first "
            "pass launches the attack. The predictive half is a two-layer PyTorch LSTM "
            "that reads four frames of tracking data (22 players plus the ball, 46 "
            "coordinates per frame) and predicts where everyone moves next, so an "
            "attack can be anticipated while it is still forming; it is a proof of "
            "concept, trained end to end on a worked transition rather than a "
            "match-validated model. A Streamlit dashboard puts any two teams' action "
            "heatmaps side by side."
        ),
        tech_stack=[
            "Python",
            "PyTorch",
            "LSTM",
            "PostgreSQL",
            "pandas",
            "mplsoccer",
            "Streamlit",
            "Tracking Data",
        ],
        category="Data & ML",
        organization="OH Leuven",
        year="2025",
        link_url=None,
        image_url="https://images.unsplash.com/photo-1517747614396-d21a78b850e8?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Izuddin Helmi Adnan",
        image_credit_url="https://unsplash.com/@izuddinhelmi",
        featured=False,
        sort_order=8,
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
        image_url="https://images.unsplash.com/photo-1776883700432-1df0abe9fc18?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Szabolcs Antal",
        image_credit_url="https://unsplash.com/@szabolcsantal",
        featured=True,
        sort_order=9,
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
        image_url="https://images.unsplash.com/photo-1681949103006-70066fb25dfe?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Sable Flow",
        image_credit_url="https://unsplash.com/@sableflow",
        featured=False,
        sort_order=10,
    ),
    dict(
        slug="ai-accessibility-aid",
        name="AI Accessibility Aid for the Visually Impaired",
        description=(
            "Vision is three tools sharing one goal: telling a visually impaired "
            "person what is in front of them. The web app takes a photo from the "
            "camera, runs an OpenCV pass that measures unique colours and total "
            "contour length, and uses that complexity score to pick the model: "
            "Gemini Flash for busy scenes, the cheaper Flash-Lite for simple "
            "ones. The prompt is written for a screen reader rather than a chat "
            "window: name the place first, describe people by what they are doing "
            "before what they look like, order objects nearest to furthest and left "
            "to right, and stay under twenty seconds read aloud. The description is "
            "spoken through the Web Speech API, and follow-up questions can be asked "
            "out loud (where something is, whether it is safe), with the model told "
            "to treat the photo as the situation in front of the user, estimate "
            "distances in metres, and call out hazards. A voice command overlays a "
            "MiDaS depth map to show what is closest. The Chrome extension carries "
            "the same idea onto the open web: Ctrl-click any image and hear a real "
            "description, since screen readers otherwise read only whatever alt text "
            "a developer bothered to write."
        ),
        tech_stack=[
            "TypeScript",
            "Next.js",
            "React",
            "Express",
            "Python",
            "OpenCV",
            "PyTorch",
            "MiDaS",
            "Google Gemini",
            "Web Speech API",
        ],
        category="Web Development",
        organization=None,
        year="2024",
        link_url="https://frontend-production-e783.up.railway.app",
        link_label="Try the Application",
        image_url="https://images.unsplash.com/photo-1581090122319-8fab9528eaaa?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="ThisisEngineering",
        image_credit_url="https://unsplash.com/@thisisengineering",
        featured=True,
        sort_order=11,
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
        image_url="https://images.unsplash.com/photo-1784652852605-6945598f2af3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Tony Marinescu",
        image_credit_url="https://unsplash.com/@tonymarinescu",
        featured=False,
        sort_order=12,
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
        image_url="https://images.unsplash.com/photo-1786989906323-2d5016760f21?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        image_credit_name="Kade Tyack",
        image_credit_url="https://unsplash.com/@kade_tyack",
        featured=False,
        sort_order=13,
    ),
]


def run():
    Base.metadata.create_all(bind=engine)
    ensure_schema()
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
