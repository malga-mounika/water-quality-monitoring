interface PHCardProps {
  value: number;
}

function PHCard({ value }: PHCardProps) {
  return (
    <div className="metric-card">
      <div className="metric-card-header">
        <h2>pH Level</h2>
      </div>

      <div className="metric-value">
        {value.toFixed(2)}
      </div>

      <div className="metric-unit">
        pH
      </div>
    </div>
  );
}

export default PHCard;