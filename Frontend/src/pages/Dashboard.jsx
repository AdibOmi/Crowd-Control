import { useEffect, useState } from "react";
import axios from "axios";
import CrowdBox from "../components/CrowdBox";

function Dashboard() {
  const [venues, setVenues] = useState([]);
  const [selectedVenue, setSelectedVenue] = useState(1);
  const [data, setData] = useState(null);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/venues")
      .then((res) => setVenues(res.data))
      .catch(console.error);
  }, []);

  useEffect(() => {
    const fetchOccupancy = () => {
      axios
        .get(`http://127.0.0.1:8000/venues/${selectedVenue}/occupancy`)
        .then((res) => setData(res.data))
        .catch(console.error);
    };

    fetchOccupancy();

    const interval = setInterval(fetchOccupancy, 3000);

    return () => clearInterval(interval);
  }, [selectedVenue]);

  if (!data) return <h2>Loading...</h2>;

  const enterVenue = async () => {
  await axios.post(
    `http://127.0.0.1:8000/venues/${selectedVenue}/enter`
  );
};

const exitVenue = async () => {
  await axios.post(
    `http://127.0.0.1:8000/venues/${selectedVenue}/exit`
  );
};

  return (
    <div className="dashboard">
      <h1>{data.venue_name}</h1>

      <select
        value={selectedVenue}
        onChange={(e) => setSelectedVenue(e.target.value)}
      >
        {venues.map((venue) => (
          <option key={venue.id} value={venue.id}>
            {venue.venue_name}
          </option>
        ))}
      </select>

      <div className="stats-card">
        <h2>
          {data.current_count} / {data.capacity}
        </h2>

        <p>People currently inside</p>

        <h3 className={`level ${data.crowd_level.toLowerCase()}`}>
          Crowd Level: {data.crowd_level}
        </h3>

        <p>Capacity Used: {data.percentage}%</p>
      </div>
      
      <div className="button-group">
      <button onClick={enterVenue}>
        Person Entered
      </button>

      <button onClick={exitVenue}>
        Person Exited
      </button>
    </div>

      <CrowdBox count={data.current_count} level={data.crowd_level} />
    </div>
  );
}

export default Dashboard;