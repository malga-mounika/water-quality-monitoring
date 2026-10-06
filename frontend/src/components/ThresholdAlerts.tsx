interface ThresholdAlertsProps {
  ph: number | null;
  turbidity_ntu: number | null;
}

function ThresholdAlerts({ ph, turbidity_ntu }: ThresholdAlertsProps) {
  const alerts: string[] = [];

  if (ph !== null) {
    if (ph < 6.5) {
      alerts.push(`Acidic pH Level (${ph.toFixed(2)} - Below 6.50 limit)`);
    } else if (ph > 8.5) {
      alerts.push(`Alkaline pH Level (${ph.toFixed(2)} - Exceeds 8.50 limit)`);
    }
  }

  if (turbidity_ntu !== null && turbidity_ntu > 5.0) {
    alerts.push(`High Turbidity (${turbidity_ntu.toFixed(2)} NTU - Exceeds 5.00 NTU limit)`);
  }

  if (alerts.length === 0) {
    return (
      <div className="alert-banner alert-success">
        <span className="alert-icon">✅</span>
        <span className="alert-message">All parameters within optimal safety thresholds.</span>
      </div>
    );
  }

  return (
    <div className="alert-banner alert-warning">
      <span className="alert-icon">⚠️</span>
      <div className="alert-content">
        <strong>Active Parameter Alerts ({alerts.length}):</strong>
        <ul className="alert-list">
          {alerts.map((alert, idx) => (
            <li key={idx}>{alert}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default ThresholdAlerts;
