import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
} from "react-leaflet";

import "leaflet/dist/leaflet.css";

interface LocationCardProps {
  latitude: number | null;
  longitude: number | null;
}

function LocationCard({
  latitude,
  longitude,
}: LocationCardProps) {
  if (latitude === null || longitude === null) {
    return (
      <div className="location-card">
        <h2>GPS Location</h2>
        <p>Location data not available</p>
      </div>
    );
  }

  return (
    <div className="location-card">
      <h2>GPS Location</h2>

      <div className="coordinates">
        <p>
          <strong>Latitude:</strong> {latitude.toFixed(6)}
        </p>

        <p>
          <strong>Longitude:</strong> {longitude.toFixed(6)}
        </p>
      </div>

      <MapContainer
        center={[latitude, longitude]}
        zoom={15}
        scrollWheelZoom={true}
        style={{
          height: "350px",
          width: "100%",
          borderRadius: "12px",
        }}
      >
        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Marker position={[latitude, longitude]}>
          <Popup>
            Water sample location
            <br />
            Latitude: {latitude.toFixed(6)}
            <br />
            Longitude: {longitude.toFixed(6)}
          </Popup>
        </Marker>
      </MapContainer>
    </div>
  );
}

export default LocationCard;