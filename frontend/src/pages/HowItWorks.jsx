
import React from "react";

const HowItWorks = () => {
  const steps = [
    {
      number: "01",
      title: "Enter Job Description",
      description:
        "The user pastes a job advertisement into the JobShield text area.",
      detail: "Input: Job posting text",
      color: "bg-indigo-50 text-indigo-700",
    },
    {
      number: "02",
      title: "Text Processing with NLP",
      description:
        "The submitted text is passed to the trained pipeline, where TF-IDF converts text into numerical features.",
      detail: "Technique: TF-IDF",
      color: "bg-violet-50 text-violet-700",
    },
    {
      number: "03",
      title: "Machine Learning Prediction",
      description:
        "The trained, class-balanced Logistic Regression model calculates a score for the fake-job class.",
      detail: "Model: Logistic Regression",
      color: "bg-teal-50 text-teal-700",
    },
    {
      number: "04",
      title: "Apply Classification Threshold",
      description:
        "The score is compared with the configured threshold of 0.70 to decide the predicted class.",
      detail: "Threshold: 0.70",
      color: "bg-amber-50 text-amber-700",
    },
    {
      number: "05",
      title: "Display the Result",
      description:
        "The API returns the prediction, model score, threshold, and numeric label for the frontend to display.",
      detail: "Output: Fake Job or Real Job",
      color: "bg-emerald-50 text-emerald-700",
    },
  ];

  return (
    <div className="min-h-screen bg-[#F8FAFC]">
      <section className="mx-auto max-w-7xl px-6 py-16 sm:py-20">
        <div className="mx-auto max-w-3xl text-center">
          <span className="inline-flex rounded-full border border-indigo-100 bg-indigo-50 px-4 py-2 text-sm font-medium text-indigo-700">
            Behind the prediction
          </span>

          <h1 className="mt-6 text-4xl font-bold tracking-tight text-[#101828] sm:text-5xl">
            How JobShield Works
          </h1>

          <p className="mt-5 text-lg leading-8 text-slate-600">
            From raw job description text to a machine learning
            prediction, JobShield follows these five steps.
          </p>
        </div>

        <div className="mx-auto mt-14 max-w-4xl">
          {steps.map((step, index) => (
            <div key={step.number} className="relative flex gap-5 sm:gap-7">
              {index !== steps.length - 1 && (
                <div className="absolute left-6 top-14 h-[calc(100%-2rem)] w-px bg-slate-200 sm:left-7" />
              )}

              <div
                className={`relative z-10 flex h-12 w-12 shrink-0 items-center justify-center rounded-xl font-bold sm:h-14 sm:w-14 ${step.color}`}
              >
                {step.number}
              </div>

              <article className="mb-8 flex-1 rounded-2xl border border-slate-200 bg-white p-5 shadow-sm sm:p-7">
                <h2 className="text-xl font-bold text-[#101828]">
                  {step.title}
                </h2>

                <p className="mt-3 leading-7 text-slate-600">
                  {step.description}
                </p>

                <span className="mt-4 inline-flex rounded-lg bg-slate-50 px-3 py-2 text-sm font-medium text-slate-700">
                  {step.detail}
                </span>
              </article>
            </div>
          ))}
        </div>

        <div className="mx-auto mt-4 max-w-4xl rounded-2xl border border-indigo-100 bg-indigo-50 p-6 sm:p-8">
          <h2 className="text-xl font-bold text-[#101828]">
            Understanding the Result
          </h2>

          <p className="mt-3 leading-7 text-slate-700">
            If the fake-job score is greater than or equal to
            0.70, the model predicts Fake Job. If the score is
            below 0.70, it predicts Real Job.
          </p>

          <p className="mt-3 text-sm leading-6 text-slate-600">
            The score is a model output, not a calibrated probability
            or a guarantee. Always verify job offers independently.
          </p>
        </div>
      </section>
    </div>
  );
};

export default HowItWorks;
