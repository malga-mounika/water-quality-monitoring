interface TurbidityCardProps {
  value: number | null;
}

function TurbidityCard({ value }: TurbidityCardProps) {
  const getStatusInfo = () => {
    if (value === null) return { text: "No Data", badgeClass: "badge-gray" };
    if (value <= 5.0) return { text: "Optimal", badgeClass: "badge-green" };
    if (value <= 10.0) return { text: "Moderate", badgeClass: "badge-amber" };
    return { text: "High Turbidity", badgeClass: "badge-red" };
  };

  const status = getStatusInfo();

  return (
    <div className="metric-card">
      <div className="card-header-flex">
        <h2>Turbidity</h2>
        <span className={`status-badge ${status.badgeClass}`}>{status.text}</span>
      </div>

      <div className="metric-value">
        {value?.toFixed(2) ?? "--"}
      </div>

      <p className="metric-unit">NTU</p>

      <p className="metric-unit">(Ideal: 0 – 5 NTU)</p>
    </div>
  );
}

export default TurbidityCard;