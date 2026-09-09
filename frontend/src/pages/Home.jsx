import { Link } from "react-router-dom";

function Home() {
    return (
        <main className="home-page">

            {/* Hero Section */}
            <section className="hero-section">

                <div className="hero-content">

                    <h1>
                        Learn. Prepare. Get Placed.
                    </h1>

                    <p>
                        CodeSphere is a student platform designed to help you
                        learn technical skills, prepare for interviews, build
                        your resume, and discover placement opportunities.
                    </p>

                    <div className="hero-buttons">

                        <Link
                            to="/register"
                            className="primary-button"
                        >
                            Get Started
                        </Link>

                        <Link
                            to="/learning"
                            className="secondary-button"
                        >
                            Explore Learning
                        </Link>

                    </div>

                </div>

            </section>


            {/* Features Section */}
            <section className="features-section">

                <h2>
                    Everything You Need
                </h2>

                <div className="features-grid">

                    <div className="feature-card">
                        <h3>Learning</h3>
                        <p>
                            Learn through structured courses, lessons,
                            notes, important concepts, and useful videos.
                        </p>
                    </div>

                    <div className="feature-card">
                        <h3>Interview Preparation</h3>
                        <p>
                            Practice interview questions organized by
                            category and difficulty.
                        </p>
                    </div>

                    <div className="feature-card">
                        <h3>Resume Builder</h3>
                        <p>
                            Create and manage your professional resume
                            with your education, skills, projects, and experience.
                        </p>
                    </div>

                    <div className="feature-card">
                        <h3>Placements</h3>
                        <p>
                            Discover available job and placement opportunities
                            and access their application information.
                        </p>
                    </div>

                </div>

            </section>


            {/* CTA Section */}
            <section className="cta-section">

                <h2>
                    Start Your Career Journey
                </h2>

                <p>
                    Create your CodeSphere account and start preparing
                    for your future.
                </p>

                <Link
                    to="/register"
                    className="primary-button"
                >
                    Create Account
                </Link>

            </section>

        </main>
    );
}

export default Home;