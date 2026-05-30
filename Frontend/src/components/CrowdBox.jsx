function CrowdBox({ count }) {
  const people = Array.from({ length: count });

  return (
    <div className="crowd-box">
      {people.map((_, index) => (
        <div key={index} className="person-dot"></div>
      ))}
    </div>
  );
}

export default CrowdBox;