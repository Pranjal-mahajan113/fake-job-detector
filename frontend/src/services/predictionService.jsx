import React from "react";

const predictionService = () => {
  const API_URL = "http://127.0.0.1:8000/api/predict";

  const predictJob = async (jobText) => {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        job_text: jobText,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(
        typeof data.detail === "string"
          ? data.detail
          : "Unable to analyze the job.",
      );
    }

    return data;
  };

  return { predictJob };
};

export default predictionService;
