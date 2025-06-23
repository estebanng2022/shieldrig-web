import React from "react";

const MainLayout = ({ children }: { children: React.ReactNode }) => (
  <div className="flex min-h-screen bg-gray-100">
    <aside className="w-64 bg-white shadow-md">Sidebar</aside>
    <main className="flex-1 p-6">{children}</main>
  </div>
);

export default MainLayout;