
import React from "react";

const ResultCard = ({ result }) => {
  if (!result) return null;

  const isFake = result.label === 1;
  const score = Math.min(
    100,
    Math.max(0, result.fake_score * 100)
  );

  return (
    <section
      aria-live="polite"
      className={`mt-6 rounded-2xl border p-6 shadow-sm ${
        isFake
          ? "border-red-200 bg-red-50"
          : "border-emerald-200 bg-emerald-50"
      }`}
    >
      <div className="flex items-start gap-4">
        <div
          className={`flex h-12 w-12 shrink-0 items-center justify-center rounded-xl text-2xl ${
            isFake
              ? "bg-red-100 text-red-700"
              : "bg-emerald-100 text-emerald-700"
          }`}
          aria-hidden="true"
        >
          {isFake ? "!" : "✓"}
        </div>

        <div>
          <p
            className={`text-sm font-semibold ${
              isFake ? "text-red-700" : "text-emerald-700"
            }`}
          >
            Analysis result
          </p>

          <h2
            className={`mt-1 text-2xl font-bold ${
              isFake ? "text-red-800" : "text-emerald-800"
            }`}
          >
            {result.prediction}
          </h2>

          <p className="mt-1 text-sm text-slate-600">
            {isFake
              ? "Potential warning signs detected."
              : "The model did not flag this posting as fake."}
          </p>
        </div>
      </div>

      <div className="mt-6 rounded-xl border border-white/80 bg-white/80 p-4">
        <div className="flex items-center justify-between gap-3">
          <span className="text-sm font-medium text-slate-600">
            Fake-job model score
          </span>

          <span className="text-lg font-bold text-[#101828]">
            {score.toFixed(2)}%
          </span>
        </div>

        <div
          className="mt-3 h-2.5 overflow-hidden rounded-full bg-slate-200"
          role="progressbar"
          aria-label="Fake-job model score"
          aria-valuemin={0}
          aria-valuemax={100}
          aria-valuenow={Number(score.toFixed(2))}
        >
          <div
            className={`h-full rounded-full transition-all duration-500 ${
              isFake ? "bg-red-500" : "bg-emerald-500"
            }`}
            style={{ width: `${score}%` }}
          />
        </div>

        <p className="mt-3 text-xs text-slate-500">
          Classification threshold:{" "}
          {(result.threshold * 100).toFixed(0)}%
        </p>
      </div>

      <p className="mt-4 text-sm leading-6 text-slate-600">
        This is an automated prediction, not definitive proof
        that a job posting is fraudulent or legitimate. Verify
        the employer independently before sharing personal information.
      </p>
    </section>
  );
};

export default ResultCard;
