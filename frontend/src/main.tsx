import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { AuthProvider } from "./hooks/AuthContext";

const rootElement = document.getElementById("root");

if (!rootElement) {
  throw new Error("❌ No se encontró el elemento con id 'root'.");
}

ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    <AuthProvider>
      <App />
    </AuthProvider>
  </React.StrictMode>
);