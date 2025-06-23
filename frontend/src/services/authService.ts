// frontend/src/services/authService.ts

const API_BASE = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

export async function login(email: string, password: string) {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: email, password }),
  });

  if (!res.ok) {
    const error = await res.json();
    throw new Error(error.detail || "Login failed");
  }

  const data = await res.json();
  localStorage.setItem("token", data.access_token);
  return data;
}

export async function signup(username: string, password: string, role: string) {
  const res = await fetch(`${API_BASE}/auth/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password, role }),
  });

  if (!res.ok) {
    const error = await res.json();
    throw new Error(error.detail || "Signup failed");
  }

  const data = await res.json();
  localStorage.setItem("token", data.access_token);
  return data;
}

export function logout() {
  localStorage.removeItem("token");
}

export function getToken() {
  return localStorage.getItem("token");
}
