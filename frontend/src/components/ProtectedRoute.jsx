import { Navigate, useLocation } from "react-router-dom";
import { getAuthToken } from "../services/learningApi";

function ProtectedRoute({ children }) {
    const location = useLocation();
    const token = getAuthToken();

    if (!token) {
        return <Navigate to="/login" replace state={{ from: location.pathname }} />;
    }

    if (
        location.pathname === "/dashboard" &&
        localStorage.getItem("is_admin") === "true"
    ) {
        return <Navigate to="/admin" replace />;
    }

    return children;
}

export default ProtectedRoute;