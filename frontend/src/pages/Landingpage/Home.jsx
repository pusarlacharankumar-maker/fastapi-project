import { Link } from "react-router-dom";
import "./Home.css";

function Home() {
    const modules = [
        {
            number: "01",
            title: "Learning",
            text: "Master the skills that matter through structured courses, projects and practical learning.",
            link: "/learning",
        },
        {
            number: "02",
            title: "Interview",
            text: "Practice technical and communication skills before facing the real interview.",
            link: "/interview",
        },
        {
            number: "03",
            title: "Resume",
            text: "Turn your skills, projects and achievements into a professional profile.",
            link: "/resume",
        },
        {
            number: "04",
            title: "Placement",
            text: "Discover opportunities and understand the skills companies are looking for.",
            link: "/placements",
        },
    ];

    return (
        <main className="home-page">

            {/* ================= HERO ================= */}

            <section className="hero">

                <div className="hero-orb hero-orb-one"></div>
                <div className="hero-orb hero-orb-two"></div>

                <div className="hero-content">

                    <div className="hero-eyebrow">
                        <span></span>
                        AI POWERED CAREER PLATFORM
                    </div>

                    <h1>
                        Learn skills.
                        <br />
                        <span>Build your future.</span>
                    </h1>

                    <p className="hero-description">
                        CodeSphere AI helps students transform what they learn
                        into real skills, confidence and career opportunities.
                    </p>

                    <div className="hero-actions">

                        {/* REGISTER BUTTON */}

                        <Link
                            to="/register"
                            className="register-button"
                        >
                            Register Now
                            <span>↗</span>
                        </Link>

                        <Link
                            to="/learning"
                            className="outline-button"
                        >
                            Explore Platform
                        </Link>

                    </div>

                    <div className="hero-statement">
                        <span>✦</span>
                        Learn something today that your future self will thank you for.
                    </div>

                </div>


                {/* ================= HERO VISUAL ================= */}

                <div className="hero-visual">

                    <div className="visual-glow"></div>

                    <div className="floating-word word-one">
                        LEARN
                    </div>

                    <div className="floating-word word-two">
                        CREATE
                    </div>

                    <div className="floating-word word-three">
                        GROW
                    </div>

                    <div className="student-circle">

                        <div className="circle-inner">

                            <div className="circle-small-label">
                                YOUR JOURNEY
                            </div>

                            <div className="circle-number">
                                72<span>%</span>
                            </div>

                            <div className="circle-text">
                                Career readiness
                            </div>

                            <div className="circle-line">
                                <div></div>
                            </div>

                        </div>

                    </div>

                    <div className="ai-chip">
                        <span>✦</span>
                        AI INSIGHT
                    </div>

                </div>

            </section>


            {/* ================= MARQUEE ================= */}

            <section className="marquee-section">

                <div className="marquee">

                    <span>LEARN</span>
                    <i>✦</i>

                    <span>PRACTICE</span>
                    <i>✦</i>

                    <span>IMPROVE</span>
                    <i>✦</i>

                    <span>BUILD</span>
                    <i>✦</i>

                    <span>GET PLACED</span>
                    <i>✦</i>

                </div>

            </section>


            {/* ================= INTRO ================= */}

            <section className="intro-section">

                <div className="section-tag">
                    WHY CODESPHERE AI
                </div>

                <div className="intro-content">

                    <h2>
                        Your education is more
                        <br />
                        than just <em>marks.</em>
                    </h2>

                    <div className="intro-right">

                        <p>
                            You learn programming. You build projects.
                            You attend classes. But what comes next?
                        </p>

                        <p>
                            CodeSphere AI connects your learning journey
                            with the skills, practice and career preparation
                            you need to move forward.
                        </p>

                        <Link
                            to="/learning"
                            className="simple-link"
                        >
                            Discover how it works
                            <span>→</span>
                        </Link>

                    </div>

                </div>

            </section>


            {/* ================= PLATFORM ================= */}

            <section className="platform-section">

                <div className="platform-heading">

                    <div>

                        <div className="section-tag">
                            THE PLATFORM
                        </div>

                        <h2>
                            Everything starts
                            <br />
                            with <em>one step.</em>
                        </h2>

                    </div>

                    <p>
                        One connected ecosystem for students who want to
                        learn, improve and become career ready.
                    </p>

                </div>


                <div className="module-list">

                    {modules.map((module) => (

                        <Link
                            to={module.link}
                            className="module-row"
                            key={module.number}
                        >

                            <span className="module-number">
                                {module.number}
                            </span>

                            <h3>
                                {module.title}
                            </h3>

                            <p>
                                {module.text}
                            </p>

                            <span className="module-arrow">
                                ↗
                            </span>

                        </Link>

                    ))}

                </div>

            </section>


            {/* ================= AI SECTION ================= */}

            <section className="ai-section">

                <div className="ai-background-circle"></div>

                <div className="ai-content">

                    <div className="section-tag light-tag">
                        INTELLIGENT LEARNING
                    </div>

                    <h2>
                        Don't just learn.
                        <br />
                        <em>Know how you're learning.</em>
                    </h2>

                    <p>
                        CodeSphere AI analyzes your progress, performance,
                        strengths and weaknesses to help you understand
                        what you should focus on next.
                    </p>

                    <Link
                        to="/learning/analytics"
                        className="light-button"
                    >
                        Explore AI Analytics
                        <span>↗</span>
                    </Link>

                </div>


                <div className="ai-visual">

                    <div className="ai-ring ring-one"></div>
                    <div className="ai-ring ring-two"></div>
                    <div className="ai-ring ring-three"></div>

                    <div className="ai-center">
                        <span>AI</span>
                        <small>UNDERSTANDS</small>
                    </div>

                    <div className="ai-floating ai-float-one">
                        Programming
                        <strong>82%</strong>
                    </div>

                    <div className="ai-floating ai-float-two">
                        Problem Solving
                        <strong>68%</strong>
                    </div>

                    <div className="ai-floating ai-float-three">
                        Web Development
                        <strong>74%</strong>
                    </div>

                </div>

            </section>


            {/* ================= JOURNEY ================= */}

            <section className="journey-section">

                <div className="section-tag">
                    YOUR JOURNEY
                </div>

                <h2>
                    Small steps.
                    <br />
                    <em>Big transformation.</em>
                </h2>


                <div className="journey">

                    <div className="journey-item">

                        <span>01</span>

                        <div>
                            <h3>Learn</h3>

                            <p>
                                Build strong technical foundations and
                                understand the concepts that matter.
                            </p>
                        </div>

                    </div>


                    <div className="journey-item">

                        <span>02</span>

                        <div>
                            <h3>Practice</h3>

                            <p>
                                Test yourself through quizzes, projects
                                and interview preparation.
                            </p>
                        </div>

                    </div>


                    <div className="journey-item">

                        <span>03</span>

                        <div>
                            <h3>Improve</h3>

                            <p>
                                Understand your strengths and identify
                                where you need to grow.
                            </p>
                        </div>

                    </div>


                    <div className="journey-item">

                        <span>04</span>

                        <div>
                            <h3>Get Placed</h3>

                            <p>
                                Build your profile and step confidently
                                toward career opportunities.
                            </p>
                        </div>

                    </div>

                </div>

            </section>


            {/* ================= MOTIVATION ================= */}

            <section className="motivation-section">

                <div className="motivation-shape"></div>

                <div className="motivation-content">

                    <div className="motivation-mark">
                        ✦
                    </div>

                    <h2>
                        You don't have to
                        <br />
                        know everything
                        <br />
                        <em>to get started.</em>
                    </h2>

                    <p>
                        Every expert was once a beginner.
                        Every career started with one decision.
                    </p>

                </div>

            </section>


            {/* ================= ABOUT ================= */}

            <section className="about-section">

                <div className="section-tag">
                    ABOUT CODESPHERE AI
                </div>

                <div className="about-grid">

                    <h2>
                        Built for the
                        <br />
                        <em>next generation.</em>
                    </h2>

                    <div className="about-text">

                        <p>
                            <strong>CodeSphere AI</strong> is an AI-powered
                            education and career development platform created
                            to help students turn knowledge into opportunity.
                        </p>

                        <p>
                            Instead of keeping learning, performance,
                            interview preparation, resumes and placements
                            disconnected, CodeSphere AI brings them together
                            into one continuous journey.
                        </p>

                        <p>
                            Our goal is simple:
                            <strong>
                                {" "}help students discover their potential,
                                build real skills and become ready for the
                                world beyond the classroom.
                            </strong>
                        </p>

                    </div>

                </div>

            </section>


            {/* ================= FINAL CTA ================= */}

            <section className="final-section">

                <div className="final-glow"></div>

                <div className="final-content">

                    <div className="section-tag light-tag">
                        YOUR NEXT CHAPTER
                    </div>

                    <h2>
                        Start where
                        <br />
                        you are.
                        <br />
                        <em>Build where you want to be.</em>
                    </h2>

                    <p>
                        Your future career doesn't happen in one day.
                        Start building it one skill at a time.
                    </p>

                    <Link
                        to="/register"
                        className="final-button"
                    >
                        Register Now
                        <span>↗</span>
                    </Link>

                </div>

            </section>


            {/* ================= FOOTER ================= */}

            <footer className="home-footer">

                <div className="footer-top">

                    <div className="footer-brand">

                        <h3>
                            CodeSphere<span> AI</span>
                        </h3>

                        <p>
                            Learn. Build. Get Placed.
                        </p>

                    </div>


                    <div className="footer-links">

                        <div>

                            <span>PLATFORM</span>

                            <Link to="/learning">
                                Learning
                            </Link>

                            <Link to="/interview">
                                Mock Interview
                            </Link>

                            <Link to="/resume">
                                Resume Builder
                            </Link>

                        </div>


                        <div>

                            <span>CAREER</span>

                            <Link to="/placements">
                                Placements
                            </Link>

                            <Link to="/dashboard">
                                Dashboard
                            </Link>

                            <Link to="/learning/analytics">
                                Analytics
                            </Link>

                        </div>


                        <div>

                            <span>ACCOUNT</span>

                            <Link to="/login">
                                Login
                            </Link>

                            <Link to="/register">
                                Register
                            </Link>

                        </div>

                    </div>

                </div>


                <div className="footer-bottom">

                    <span>
                        © 2026 CodeSphere AI
                    </span>

                    <span>
                        Built for students. Built for the future.
                    </span>

                </div>

            </footer>

        </main>
    );
}

export default Home;