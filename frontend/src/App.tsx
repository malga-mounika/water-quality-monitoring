import { useEffect, useState } from "react";

import PHCard from "./components/PHCard";
import TurbidityCard from "./components/TurbidityCard";
import WQICard from "./components/WQICard";
import PHChart from "./components/PHChart";
import TurbidityChart from "./components/TurbidityChart";
import LocationCard from "./components/LocationCard";
import RecommendationCard from "./components/RecommendationCard";
import ThresholdAlerts from "./components/ThresholdAlerts";

import {
  getReadingHistory,
  type WaterReading,
} from "./services/api";

import "./App.css";

function App() {
  const [readings, setReadings] = useState<WaterReading[]>([]);
  const [loading, setLoading] = useState(true);
  const [darkMode, setDarkMode] = useState<boolean>(() => {
    return localStorage.getItem("theme") === "dark";
  });

  const toggleDarkMode = () => {
    setDarkMode((prev) => {
      const next = !prev;
      localStorage.setItem("theme", next ? "dark" : "light");
      return next;
    });
  };

  useEffect(() => {
    let isMounted = true;

    const loadReadings = async () => {
      try {
        const data = await getReadingHistory(50);

        if (isMounted) {
          setReadings(data);
        }
      } catch (error) {
        console.error("Failed to load readings:", error);
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    // Load immediately
    loadReadings();

    // Refresh every 3 seconds
    const intervalId = window.setInterval(() => {
      loadReadings();
    }, 3000);

    // Stop polling when the page/component is closed
    return () => {
      isMounted = false;
      window.clearInterval(intervalId);
    };
  }, []);

  const latest = readings.length > 0 ? readings[0] : null;

  if (loading) {
    return <div className={`loading ${darkMode ? "dark-theme" : ""}`}>Loading water quality data...</div>;
  }

  return (
    <div className={`dashboard ${darkMode ? "dark-theme" : ""}`}>
      <header className="dashboard-header">
        <div>
          <h1>Water Quality Monitoring</h1>
          <p>Real-Time Water Quality Dashboard</p>
        </div>

        <div className="header-actions">
          <button
            className="theme-toggle-btn"
            onClick={toggleDarkMode}
            title="Toggle Light/Dark Theme"
          >
            {darkMode ? "☀️ Light Mode" : "🌙 Dark Mode"}
          </button>

          <div className="device-status">
            <span className="status-dot"></span>
            Device Online
          </div>
        </div>
      </header>

      <main>
        <ThresholdAlerts
          ph={latest?.ph ?? null}
          turbidity_ntu={latest?.turbidity_ntu ?? null}
        />

        <section className="metrics-grid">
          <PHCard value={latest?.ph ?? 0} />

          <TurbidityCard
            value={latest?.turbidity_ntu ?? 0}
          />

          <WQICard
            score={latest?.wqi_score ?? 0}
            status={latest?.quality_status ?? "Unknown"}
          />
        </section>

        <section className="charts-grid">
          <PHChart data={readings} />

          <TurbidityChart data={readings} />
        </section>

        <LocationCard
          latitude={latest?.latitude ?? null}
          longitude={latest?.longitude ?? null}
        />

        <RecommendationCard
          contaminants={latest?.detected_contaminants ?? null}
          recommendation={latest?.ai_recommendation ?? null}
        />
      </main>
    </div>
  );
}

export default App;