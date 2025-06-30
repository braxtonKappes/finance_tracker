# Finance Tracker

Finance Tracker is a full-stack web application that allows users to register, log in, and access a personalized dashboard. Built with React, Tailwind CSS, and FastAPI, it’s designed to be scalable, modern, and responsive across all devices.

---

## Use Case

This application simulates a personal finance platform. Users can:

- Sign up and securely log in
- Access a dashboard interface
- Extend functionality with transaction records, charts, and budgeting tools (planned features)

---

## Tech Stack

### Frontend
- React – JavaScript UI library for component-based design
- Vite – Fast frontend build tool
- Tailwind CSS – Utility-first CSS framework
- React Router DOM – Client-side routing

### Backend
- FastAPI – High-performance Python web framework
- JWT – Token-based authentication
- CORS – Cross-origin request handling for API access

---

## Features

- Secure authentication with JWT
- Login and signup flows connected to backend
- Responsive dashboard layout
- Protected routes using React Router
- Clean and maintainable structure

---

## Getting Started

### Prerequisites

- Node.js (v16+ recommended)
- Python 3.10+
- A local FastAPI backend server (see below)

---

### Frontend Setup

1. Clone the repository

git clone https://github.com/yourusername/finance-tracker.git
cd finance-tracker/frontend

2. Install Frontend Dependencies

npm install

3. Initialize Tailwind (if not already initialized)

npx tailwindcss init -p

Update tailwind.config.js:
    content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"]

Ensure index.css includes:
    @tailwind base;
    @tailwind components;
    @tailwind utilities;

4. Start the Frontend
npm run dev

5. Run the Backend (FastAPI)
In a separate terminal:
    uvicorn main:app --reload --port 8000

## File Structure Overview
finance-tracker/
├── frontend/
│   ├── components/
│   │   ├── Login.jsx
│   │   ├── Signup.jsx
│   │   └── Dashboard.jsx
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
└── backend/
    └── main.py

## About the Developer
Boyd “Braxton” Kappes
Software Engineer with a focus on full-stack web development, blending React + Tailwind on the frontend and Python/FastAPI on the backend.

Location: Wind Lake, WI

Email: braxtonkappes@gmail.com

LinkedIn: [\[My LinkedIn\]](https://www.linkedin.com/in/boydbraxtonkappes/)