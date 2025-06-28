import { useState } from "react";
import Login from "./components/Login";
import Signup from "./components/Signup";

function App() {
  const [showLogin, setShowLogin] = useState(true);

  return (
    <div>
      <h1>Finance Tracker</h1>
      <button onClick={() => setShowLogin(!showLogin)}>
        {showLogin ? "Go to Sign Up" : "Go to Login"}
      </button>
      {showLogin ? <Login /> : <Signup />}
    </div>
  );
}

export default App;
