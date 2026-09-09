import { Link } from "react-router-dom";

function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-container">

                <Link to="/" className="logo">
                    CodeSphere
                </Link>

                <div className="nav-links">
                    <Link to="/dashboard">Dashboard</Link>
                    <Link to="/learning">Learning</Link>
                    <Link to="/interview">Interview</Link>
                    <Link to="/resume">Resume</Link>
                    <Link to="/placements">Placements</Link>
                    <Link to="/login">Login</Link>
                    <Link to="/register">Register</Link>
                </div>

            </div>
        </nav>
    );
}

export default Navbar;