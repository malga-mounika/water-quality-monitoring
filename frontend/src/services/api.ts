import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: API_BASE_URL,
});

export interface WaterReading {
  id: number;
  device_id: string;
  ph: number | null;
  turbidity_ntu: number | null;
  latitude: number | null;
  longitude: number | null;
  wqi_score: number | null;
  quality_status: string | null;
  detected_contaminants: {
    diagnosis: string;
    likely_cause: string | null;
  }[] | null;
  ai_recommendation: string | null;
  timestamp: string;
}

export interface ReadingHistoryResponse {
  message: string;
  count: number;
  data: WaterReading[];
}

export const getReadingHistory = async (
  limit: number = 50
): Promise<WaterReading[]> => {
  const response = await api.get<ReadingHistoryResponse>(
    "/api/readings/history",
    {
      params: { limit },
    }
  );

  return response.data.data;
};

export default api;