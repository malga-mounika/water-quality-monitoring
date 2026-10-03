interface TurbidityCardProps {
  value: number;
}

function TurbidityCard({ value }: TurbidityCardProps) {
  return (
    <div className="metric-card">
      <div className="metric-card-header">
        <h2>Turbidity</h2>
      </div>

      <div className="metric-value">
        {value.toFixed(2)}
      </div>

      <div className="metric-unit">
        NTU
      </div>
    </div>
  );
}

export default TurbidityCard;