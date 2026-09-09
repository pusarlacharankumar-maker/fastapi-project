import { Link } from "react-router-dom";

function Dashboard() {
    return (
        <main className="dashboard-page">

            <div className="dashboard-container">

                {/* Header */}
                <div className="dashboard-header">
                    <div>
                        <h1>Dashboard</h1>
                        <p>Welcome back to CodeSphere.</p>
                    </div>

                    <Link
                        to="/learning"
                        className="primary-button"
                    >
                        Continue Learning
                    </Link>
                </div>


                {/* Statistics */}
                <section className="stats-grid">

                    <div className="stat-card">
                        <span>Courses</span>
                        <strong>0</strong>
                        <p>Total courses</p>
                    </div>

                    <div className="stat-card">
                        <span>Lessons</span>
                        <strong>0</strong>
                        <p>Total lessons</p>
                    </div>

                    <div className="stat-card">
                        <span>Completed</span>
                        <strong>0</strong>
                        <p>Lessons completed</p>
                    </div>

                    <div className="stat-card">
                        <span>Progress</span>
                        <strong>0%</strong>
                        <p>Average progress</p>
                    </div>

                </section>


                {/* Main Dashboard */}
                <section className="dashboard-grid">

                    {/* Learning Progress */}
                    <div className="dashboard-card">

                        <div className="card-header">
                            <h2>Learning Progress</h2>

                            <Link to="/learning">
                                View Courses
                            </Link>
                        </div>

                        <div className="progress-area">

                            <div className="progress-circle">
                                0%
                            </div>

                            <div>
                                <h3>Keep Learning</h3>

                                <p>
                                    Start a course and track your learning
                                    progress here.
                                </p>
                            </div>

                        </div>

                    </div>


                    {/* Resume */}
                    <div className="dashboard-card">

                        <div className="card-header">
                            <h2>Resume</h2>

                            <Link to="/resume">
                                Manage
                            </Link>
                        </div>

                        <p className="empty-message">
                            You haven't created your resume yet.
                        </p>

                        <Link
                            to="/resume"
                            className="primary-button"
                        >
                            Create Resume
                        </Link>

                    </div>


                    {/* Interview */}
                    <div className="dashboard-card">

                        <div className="card-header">
                            <h2>Interview Preparation</h2>

                            <Link to="/interview">
                                Practice
                            </Link>
                        </div>

                        <p className="empty-message">
                            Practice interview questions and improve
                            your preparation.
                        </p>

                        <Link
                            to="/interview"
                            className="secondary-button"
                        >
                            Start Practice
                        </Link>

                    </div>


                    {/* Placements */}
                    <div className="dashboard-card">

                        <div className="card-header">
                            <h2>Placements</h2>

                            <Link to="/placements">
                                View Jobs
                            </Link>
                        </div>

                        <p className="empty-message">
                            Explore available placement and job
                            opportunities.
                        </p>

                        <Link
                            to="/placements"
                            className="secondary-button"
                        >
                            Explore Placements
                        </Link>

                    </div>

                </section>

            </div>

        </main>
    );
}

export default Dashboard;