import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

interface PHChartProps {
  data: {
    timestamp: string;
    ph: number | null;
  }[];
}

function PHChart({ data }: PHChartProps) {
  const chartData = [...data]
    .filter((reading) => reading.ph !== null)
    .reverse()
    .map((reading) => ({
      time: new Date(reading.timestamp).toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
      ph: reading.ph,
    }));

  return (
    <div className="chart-card">
      <h2>pH Trend</h2>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="time" />

          <YAxis
            domain={[0, 14]}
            label={{
              value: "pH",
              angle: -90,
              position: "insideLeft",
            }}
          />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="ph"
            stroke="#2563eb"
            strokeWidth={3}
            dot={{ r: 4 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default PHChart;