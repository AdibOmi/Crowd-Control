import { useEffect, useState } from "react";
import axios from "axios";
import CrowdBox from "../components/CrowdBox";

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/occupancy")
      .then((res) => setData(res.data))
      .catch((err) => console.log(err));
  }, []);

  if (!data) return <h2>Loading...</h2>;

  return (
    <div className="dashboard">
      <h1>{data.venue_name}</h1>

      <div className="stats-card">
        <h2>{data.current_count} / {data.capacity}</h2>
        <p>People currently inside</p>
        <h3>Crowd Level: {data.crowd_level}</h3>
        <p>Capacity Used: {data.percentage}%</p>
      </div>

      <CrowdBox count={data.current_count} />
    </div>
  );
}

export default Dashboard;