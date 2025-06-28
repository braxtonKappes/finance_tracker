const BASE_URL = import.meta.env.VITE_API_URL;

export async function fetchTransactions(token) {
  const res = await fetch(`${BASE_URL}/transactions/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    throw new Error("Failed to fetch transactions");
  }

  return res.json();
}
