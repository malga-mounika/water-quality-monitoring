interface PHCardProps {
  value: number | null;
}

function PHCard({ value }: PHCardProps) {
  const getStatusInfo = () => {
    if (value === null) return { text: "No Data", badgeClass: "badge-gray" };
    if (value >= 6.5 && value <= 8.5) return { text: "Normal", badgeClass: "badge-green" };
    if (value < 6.5) return { text: "Acidic Alert", badgeClass: "badge-red" };
    return { text: "Alkaline Alert", badgeClass: "badge-purple" };
  };

  const status = getStatusInfo();

  return (
    <div className="metric-card">
      <div className="card-header-flex">
        <h2>pH</h2>
        <span className={`status-badge ${status.badgeClass}`}>{status.text}</span>
      </div>

      <div className="metric-value">
        {value?.toFixed(2) ?? "--"}
      </div>

      <p className="metric-unit">(Ideal: 6.5 – 8.5)</p>
    </div>
  );
}

export default PHCard;