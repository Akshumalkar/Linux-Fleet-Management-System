import { useEffect, useState } from "react";

function App() {
  const [nodes, setNodes] = useState([]);
  const [error, setError] = useState(null);

  const fetchNodes = async () => {
    try {
      const res = await fetch("http://localhost:8000/nodes");

      if (!res.ok) {
        throw new Error("Backend error: " + res.status);
      }

      const data = await res.json();

      if (!Array.isArray(data)) {
        throw new Error("API did not return array");
      }

      setNodes(data);
      setError(null);
    } catch (err) {
      console.error(err);
      setError(err.message);
      setNodes([]);
    }
  };

  useEffect(() => {
    fetchNodes();

    const interval = setInterval(fetchNodes, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: 20, background: "#111", color: "white" }}>
      <h1>Fleet Dashboard</h1>

      {error && (
        <p style={{ color: "red" }}>Error: {error}</p>
      )}

      {nodes.length === 0 && !error ? (
        <p>No nodes found</p>
      ) : (
        nodes.map((node) => (
          <div key={node.id}>
            <h3>{node.hostname}</h3>
            <p>{node.ip_address}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default App;