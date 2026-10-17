import React from "react";
import { useState } from "react";
import ResultCard from "../componets/ResultCard";
import predictionService from "../services/predictionService";

const Home = () => {
  const { predictJob } = predictionService();
  const [jobText, setJobText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  async function handleSubmit(event) {
    event.preventDefault();

    if (!jobText.trim()) {
      setError("Please enter a job description.");
      setResult(null);
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const prediction = await predictJob(jobText.trim());
      setResult(prediction);
    } catch (err) {
      setError(err.message || "Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  }
  return (
    <div className="min-h-screen">
      <section className="mx-auto max-w-7xl px-6 py-16 sm:py-24">
        <div className="mx-auto max-w-3xl text-center">
          <span className="inline-flex items-center rounded-full border border-indigo-100 bg-indigo-50 px-4 py-2 text-sm font-medium text-indigo-700">
            AI-powered job screening
          </span>

          <h1 className="mt-6 text-4xl font-bold tracking-tight text-[#101828] sm:text-5xl lg:text-6xl">
            Find the red flags.
            <span className="mt-2 block text-indigo-600">
              Protect your career.
            </span>
          </h1>

          <p className="mx-auto mt-6 max-w-2xl text-lg leading-8 text-slate-600">
            Screen job postings with Machine Learning and Natural Language
            Processing before sharing your personal information or applying.
          </p>
        </div>

        <div className="mx-auto mt-12 max-w-3xl rounded-2xl border border-slate-200 bg-white p-6 shadow-sm sm:p-8">
          <form onSubmit={handleSubmit}>
            <label
              htmlFor="job-description"
              className="block text-base font-semibold text-[#101828]"
            >
              Paste the job description
            </label>

            <p className="mt-2 text-sm text-slate-500">
              Include as much of the job posting as you have.
            </p>

            <textarea
              id="job-description"
              value={jobText}
              onChange={(event) => setJobText(event.target.value)}
              placeholder="Paste the job title, responsibilities, requirements, salary details..."
              rows={8}
              required
              className="mt-5 w-full resize-y rounded-xl border border-slate-300 bg-white px-4 py-3 text-sm leading-6 text-slate-800 outline-none transition placeholder:text-slate-400 focus:border-indigo-500 focus:ring-4 focus:ring-indigo-100"
            />

            <div className="mt-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <p className="text-xs text-slate-500">
                Please avoid sharing personal information.
              </p>

              <button
                type="submit"
                disabled={loading || !jobText.trim()}
                className="inline-flex items-center justify-center gap-2 rounded-xl bg-indigo-600 px-6 py-3 font-semibold text-white transition hover:bg-indigo-700 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {loading ? (
                  <>
                    <span className="h-4 w-4 animate-spin rounded-full border-2 border-white/30 border-t-white" />
                    Analyzing...
                  </>
                ) : (
                  <>
                    Analyze Job
                    <span aria-hidden="true">→</span>
                  </>
                )}
              </button>
            </div>
          </form>
          {error && (
            <p
              role="alert"
              className="mt-5 rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-700"
            >
              {error}
            </p>
          )}

          <ResultCard result={result} />
        </div>

        <p className="mx-auto mt-6 max-w-2xl text-center text-sm leading-6 text-slate-500">
          JobShield provides an automated prediction, not a definitive
          determination of fraud. Always verify an employer independently.
        </p>
      </section>
    </div>
  );
};

export default Home;
