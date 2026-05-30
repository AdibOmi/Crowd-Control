function CrowdBox({ count, level }) {
  const people = Array.from({ length: count });

  return (
    <div className="crowd-box">
      {people.map((_, index) => (
        <div
          key={index}
          className={`person-dot ${level.toLowerCase()}`}
        ></div>
      ))}
    </div>
  );
}

export default CrowdBox;