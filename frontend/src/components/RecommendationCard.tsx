interface RecommendationCardProps {
  contaminants: {
    diagnosis: string;
    likely_cause: string | null;
  }[] | null;
  recommendation: string | null;
}

function RecommendationCard({
  contaminants,
  recommendation,
}: RecommendationCardProps) {
  const contamination = contaminants?.[0];

  return (
    <div className="recommendation-card">
      <h2>Contamination & Recommendation</h2>

      <div className="recommendation-grid">

        {/* Left side */}
        <div className="recommendation-section">
          <h3>Detected Contamination</h3>

          <p>
            {contamination?.diagnosis ??
              "No contamination detected"}
          </p>

          {contamination?.likely_cause && (
            <>
              <h3 className="sub-heading">Possible Cause</h3>
              <p>{contamination.likely_cause}</p>
            </>
          )}
        </div>

        {/* Right side */}
        <div className="recommendation-section">
          <h3>Recommended Treatment</h3>

          <p>
            {recommendation ??
              "No treatment recommendation is currently available."}
          </p>
        </div>

      </div>
    </div>
  );
}

export default RecommendationCard;