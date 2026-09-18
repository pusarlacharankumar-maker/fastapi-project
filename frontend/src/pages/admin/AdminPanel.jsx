import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function AdminPanel() {
    const navigate = useNavigate();
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    const loadUsers = async () => {
        try {
            setLoading(true);
            setError("");

            const token = localStorage.getItem("access_token");
            const isAdmin = localStorage.getItem("is_admin") === "true";

            if (!token || !isAdmin) {
                navigate("/dashboard");
                return;
            }

            const response = await fetch("http://127.0.0.1:8000/admin/users", {
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
            });

            if (!response.ok) {
                throw new Error("Access denied or request failed");
            }

            const data = await response.json();
            setUsers(Array.isArray(data) ? data : []);
        } catch (err) {
            setError(err.message || "Unable to load admin data.");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadUsers();
    }, [navigate]);

    const handleDeleteUser = async (userId) => {
        const confirmed = window.confirm("Are you sure you want to delete this user?");

        if (!confirmed) return;

        try {
            const token = localStorage.getItem("access_token");

            const response = await fetch(`http://127.0.0.1:8000/admin/users/${userId}`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
            });

            if (!response.ok) {
                throw new Error("Failed to delete user");
            }

            await loadUsers();
        } catch (err) {
            setError(err.message || "Unable to delete user.");
        }
    };

    const totalUsers = users.length;
    const adminUsers = users.filter((user) => user.is_admin).length;
    const normalUsers = totalUsers - adminUsers;

    return (
        <main className="admin-page">
            <div className="admin-container">
                <header className="admin-header">
                    <div>
                        <p className="eyebrow">Admin panel</p>
                        <h1>System Overview</h1>
                    </div>
                    <button type="button" onClick={() => navigate("/admin/learning")}>Manage Learning</button>
                </header>

                {error && <div className="admin-error">{error}</div>}

                <section className="admin-stats">
                    <div className="admin-stat-card">
                        <span>Total Users</span>
                        <strong>{totalUsers}</strong>
                    </div>

                    <div className="admin-stat-card">
                        <span>Admins</span>
                        <strong>{adminUsers}</strong>
                    </div>

                    <div className="admin-stat-card">
                        <span>Students</span>
                        <strong>{normalUsers}</strong>
                    </div>
                </section>

                <section className="admin-panel-card">
                    <div className="admin-panel-header">
                        <h2>User Management</h2>
                    </div>

                    {loading ? (
                        <p className="admin-empty">Loading users...</p>
                    ) : users.length === 0 ? (
                        <p className="admin-empty">No users found.</p>
                    ) : (
                        <div className="user-table-wrap">
                            <table className="user-table">
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>Username</th>
                                        <th>Email</th>
                                        <th>Role</th>
                                        <th>Action</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {users.map((user) => (
                                        <tr key={user.id}>
                                            <td>{user.id}</td>
                                            <td>{user.username}</td>
                                            <td>{user.email}</td>
                                            <td>
                                                <span
                                                    className={
                                                        user.is_admin ? "role-badge admin" : "role-badge user"
                                                    }
                                                >
                                                    {user.is_admin ? "Admin" : "User"}
                                                </span>
                                            </td>
                                            <td>
                                                <button
                                                    type="button"
                                                    className="delete-btn"
                                                    onClick={() => handleDeleteUser(user.id)}
                                                >
                                                    Delete
                                                </button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    )}
                </section>
            </div>
        </main>
    );
}

export default AdminPanel;
