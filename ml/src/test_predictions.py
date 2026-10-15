from predictor import predict_job
# Five sample job descriptions
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

# Predict using the shared prediction function
for job in test_jobs:
    result = predict_job(job["text"])

    print("-" * 50)
    print(job["name"])
    print("Fake Score:", result["fake_score"])
    print("Threshold:", result["threshold"])
    print("Prediction:", result["prediction"])
    print("Label:", result["label"])

print("-" * 50)
print("All 5 job examples tested successfully.")
