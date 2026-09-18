import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import { loginUser } from "../../services/authApi";

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [selectedRole, setSelectedRole] = useState("user");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError("");
        setLoading(true);

        try {
            const tokens = await loginUser({
                email,
                password,
                role: selectedRole,
            });
            const finalRole =
                tokens.role ||
                (tokens.is_admin ? "admin" : selectedRole || "user");

            localStorage.setItem("access_token", tokens.access_token);
            localStorage.setItem("refresh_token", tokens.refresh_token);
            localStorage.setItem("role", finalRole);
            localStorage.setItem("selected_role", selectedRole);
            localStorage.setItem(
                "is_admin",
                String(Boolean(tokens.is_admin || finalRole === "admin"))
            );
            window.dispatchEvent(new Event("auth-change"));

            if (finalRole === "admin" || tokens.is_admin) {
                navigate("/admin");
                return;
            }

            navigate("/dashboard");
        } catch (requestError) {
            setError(requestError.message || "Unable to login.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="auth-page">
            <div className="auth-card">

                <h1>Welcome Back</h1>
                <p>Login to your CodeSphere account</p>

                {error && <p className="auth-error">{error}</p>}

                <form onSubmit={handleSubmit}>

                    <div className="form-group">
                        <label>Email</label>

                        <input
                            type="email"
                            value={email}
                            onChange={(event) => setEmail(event.target.value)}
                            placeholder="Enter your email"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Password</label>

                        <input
                            type="password"
                            value={password}
                            onChange={(event) => setPassword(event.target.value)}
                            placeholder="Enter your password"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Select Role</label>
                        <select
                            value={selectedRole}
                            onChange={(event) => setSelectedRole(event.target.value)}
                            className="role-select"
                        >
                            <option value="user">User</option>
                            <option value="admin">Admin</option>
                        </select>
                    </div>

                    <button type="submit" disabled={loading}>
                        {loading ? "Logging in..." : "Login"}
                    </button>

                </form>
                <p className="auth-link">
                    Don't have an account?{" "}
                    <Link to="/register">Create an account</Link>
                </p>

            </div>
        </div>
    );
}

export default Login;