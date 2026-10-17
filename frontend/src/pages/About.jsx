import React from "react";

const About = () => {
  const technologies = [
    {
      name: "Machine Learning",
      description:
        "Classifies job postings using a trained Logistic Regression model.",
    },
    {
      name: "Natural Language Processing",
      description:
        "Processes job description text and converts it into numerical features using TF-IDF.",
    },
    {
      name: "FastAPI",
      description:
        "Connects the trained model to the frontend through a prediction API.",
    },
    {
      name: "React",
      description:
        "Provides an interactive interface for submitting job descriptions and viewing results.",
    },
  ];

  return (
    <div className="min-h-screen bg-[#F8FAFC]">
      <section className="mx-auto max-w-7xl px-6 py-16 sm:py-20">
        <div className="mx-auto max-w-3xl text-center">
          <span className="inline-flex rounded-full border border-indigo-100 bg-indigo-50 px-4 py-2 text-sm font-medium text-indigo-700">
            About the project
          </span>

          <h1 className="mt-6 text-4xl font-bold tracking-tight text-[#101828] sm:text-5xl">
            Meet JobShield
          </h1>

          <p className="mt-5 text-lg leading-8 text-slate-600">
            An intelligent system designed to identify potentially fraudulent
            job advertisements using Machine Learning and Natural Language
            Processing.
          </p>
        </div>

        <div className="mt-14 grid gap-8 md:grid-cols-2">
          <article className="rounded-2xl border border-slate-200 bg-white p-7 shadow-sm">
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-indigo-50 text-2xl">
              🎯
            </div>

            <h2 className="mt-5 text-xl font-bold text-[#101828]">
              Our Objective
            </h2>

            <p className="mt-3 leading-7 text-slate-600">
              JobShield aims to help job seekers screen job advertisements for
              possible warning signs before applying or sharing personal
              information. It provides an automated prediction based on the text
              submitted by the user.
            </p>
          </article>

          <article className="rounded-2xl border border-slate-200 bg-white p-7 shadow-sm">
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-teal-50 text-2xl">
              🛡️
            </div>

            <h2 className="mt-5 text-xl font-bold text-[#101828]">
              Why JobShield?
            </h2>

            <p className="mt-3 leading-7 text-slate-600">
              Fraudulent job advertisements can expose applicants to financial
              loss, misleading offers, and misuse of personal information.
              JobShield explores how text analysis can support safer and more
              informed job searching.
            </p>
          </article>
        </div>

        <div className="mt-14">
          <div className="text-center">
            <h2 className="text-3xl font-bold text-[#101828]">
              Technology Stack
            </h2>

            <p className="mt-3 text-slate-600">
              The technologies used to build the JobShield prototype.
            </p>
          </div>

          <div className="mt-8 grid gap-5 sm:grid-cols-2">
            {technologies.map((technology) => (
              <article
                key={technology.name}
                className="rounded-2xl border border-slate-200 bg-white p-6 transition hover:-translate-y-1 hover:shadow-md"
              >
                <h3 className="text-lg font-semibold text-indigo-700">
                  {technology.name}
                </h3>

                <p className="mt-2 leading-7 text-slate-600">
                  {technology.description}
                </p>
              </article>
            ))}
          </div>
        </div>

        <div className="mt-12 rounded-2xl border border-amber-200 bg-amber-50 p-6">
          <h2 className="text-lg font-bold text-amber-900">
            Important Disclaimer
          </h2>

          <p className="mt-2 text-sm leading-6 text-amber-900/80">
            JobShield is an academic project and its predictions are not
            definitive proof of fraud or legitimacy. Users should independently
            verify employers and job offers before taking action.
          </p>
        </div>
      </section>
    </div>
  );
};

export default About;
