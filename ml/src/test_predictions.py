
import joblib

model = joblib.load(
    "ml/models/logistic_regression_balanced_pipeline.joblib"
)

test_jobs = [
    {
        "name": "Example 1 - Suspicious Data Entry",
        "text": """
        Work from home data entry job.
        Earn $5000 every week with no experience.
        Pay a registration fee before joining.
        Contact us only through WhatsApp.
        """
    },
    {
        "name": "Example 2 - Software Developer",
        "text": """
        We are hiring a Junior Python Developer.
        Candidates should know Python, SQL, Git,
        and basic REST APIs. Applicants will complete
        a technical interview. Salary depends on experience.
        Apply through our official company careers page.
        """
    },
    {
        "name": "Example 3 - Suspicious Immediate Hiring",
        "text": """
        Guaranteed job for everyone. No interview,
        no skills required. Earn huge money daily.
        Send your identity documents and pay a processing
        fee today to secure your position.
        """
    },
    {
        "name": "Example 4 - Customer Support",
        "text": """
        Customer Support Executive required for a
        full-time office role. Good communication skills
        and basic computer knowledge are required.
        The recruitment process includes an interview.
        Apply through the company's careers portal.
        """
    },
    {
        "name": "Example 5 - Unclear Remote Job",
        "text": """
        Remote marketing assistant needed.
        Flexible working hours and performance-based pay.
        Applicants should have basic writing skills and
        social media knowledge. Send your resume by email
        for further details about the role.
        """
    }
]

for job in test_jobs:
    prediction = model.predict([job["text"]])[0]
    result = "Fake Job" if prediction == 1 else "Real Job"

    print("-" * 45)
    print(job["name"])
    print("Prediction:", result)
