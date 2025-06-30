import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

export default function Dashboard() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) navigate("/login");
  }, [navigate]);

  return (
    <div className="min-h-screen bg-gray-900 text-white px-4 py-6 sm:px-8">
      <div className="max-w-5xl mx-auto">
        {/* Header */}
        <header className="flex flex-col sm:flex-row justify-between items-center mb-10 gap-4">
          <h2 className="text-2xl sm:text-4xl font-bold">Finance Tracker Dashboard</h2>
          <button
            onClick={handleLogout}
            className="bg-red-600 hover:bg-red-700 px-4 py-2 rounded-md text-white font-semibold transition"
          >
            Log Out
          </button>
        </header>

        {/* Welcome Section */}
        <section className="bg-gray-800 p-6 rounded-lg shadow-md">
          <h3 className="text-xl sm:text-2xl font-semibold mb-4">Welcome back!</h3>
          <p className="text-gray-300 text-sm sm:text-base">
            Here is where your finance data will appear. You can build sections here
            for transactions, graphs, summaries, or budgeting tools.
          </p>
        </section>
      </div>
    </div>
  );
}
