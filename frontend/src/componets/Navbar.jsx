import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <header className="sticky top-0 z-50 border-b border-slate-200 bg-white/95 backdrop-blur">
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        {/* Logo */}
        <Link to="/" className="flex items-center gap-2">
          <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-[#101828] text-white">
            <span className="text-lg font-bold">J</span>
          </span>
          <span className="text-xl font-bold tracking-tight text-[#101828]">
            JobShield
          </span>
        </Link>

        {/* Navigation links */}
        <div className="hidden items-center gap-8 md:flex">
          <Link
            to="/"
            className="text-sm font-medium text-slate-700 transition hover:text-indigo-600"
          >
            Home
          </Link>
          <Link
            to="/how-it-works"
            className="text-sm font-medium text-slate-700 transition hover:text-indigo-600"
          >
            How It Works
          </Link>
          <Link
            to="/about"
            className="text-sm font-medium text-slate-700 transition hover:text-indigo-600"
          >
            About
          </Link>
        </div>

        {/* Primary action */}
        <Link
          to="/"
          className="rounded-xl bg-indigo-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition hover:bg-indigo-700"
        >
          Check a Job
        </Link>
      </nav>
    </header>
  );
};

export default Navbar;
