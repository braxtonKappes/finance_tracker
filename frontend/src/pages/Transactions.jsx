import { useEffect, useState } from "react";
import { fetchTransactions } from "../api/transactions";

function Transactions() {
  const [txs, setTxs] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("access_token"); // assuming token is stored here
    if (!token) return setError("No token found");

    fetchTransactions(token)
      .then(setTxs)
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <p>{error}</p>;

  return (
    <div>
      <h2>Transactions</h2>
      <ul>
        {txs.map((tx) => (
          <li key={tx.id}>{tx.title} - ${tx.amount}</li>
        ))}
      </ul>
    </div>
  );
}

export default Transactions;
