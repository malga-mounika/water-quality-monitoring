import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

interface TurbidityChartProps {
  data: {
    timestamp: string;
    turbidity_ntu: number | null;
  }[];
}

function TurbidityChart({ data }: TurbidityChartProps) {
  const chartData = [...data]
    .filter((reading) => reading.turbidity_ntu !== null)
    .reverse()
    .map((reading) => ({
      time: new Date(reading.timestamp).toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
      turbidity: reading.turbidity_ntu,
    }));

  return (
    <div className="chart-card">
      <h2>Turbidity Trend</h2>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="time" />

          <YAxis
            label={{
              value: "NTU",
              angle: -90,
              position: "insideLeft",
            }}
          />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="turbidity"
            stroke="#16a34a"
            strokeWidth={3}
            dot={{ r: 4 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default TurbidityChart;