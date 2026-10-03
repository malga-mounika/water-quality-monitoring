interface WQICardProps {
  score: number;
  status: string;
}

function WQICard({ score, status }: WQICardProps) {
  const getScoreColor = () => {
    if (score >= 80) return "#22c55e";
    if (score >= 50) return "#f59e0b";
    return "#ef4444";
  };

  const color = getScoreColor();

  return (
    <div className="wqi-card">
      <h2>Water Quality Index</h2>

      <div
        className="wqi-circle"
        style={{
          borderColor: color,
        }}
      >
        <span className="wqi-score">{score}</span>
        <span className="wqi-label">WQI</span>
      </div>

      <div
        className="wqi-status"
        style={{
          color: color,
        }}
      >
        {status}
      </div>
    </div>
  );
}

export default WQICard;