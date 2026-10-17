import { Outlet } from "react-router-dom";
import Navbar from "../componets/Navbar";
const MainLayout = () => {
  return (
    <div className="flex min-h-screen flex-col bg-[#F8FAFC] text-[#101828]">
      <Navbar />

      <main className="flex-1">
        <Outlet />
      </main>

      <footer className="border-t border-slate-200 bg-white">
        <div className="mx-auto max-w-7xl px-6 py-6 text-center text-sm text-slate-500">
          © {new Date().getFullYear()} JobShield. AI-assisted job screening.
        </div>
      </footer>
    </div>
  );
};

export default MainLayout;
