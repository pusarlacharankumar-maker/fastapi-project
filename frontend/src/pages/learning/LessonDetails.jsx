import { Link, useParams } from "react-router-dom";

function LessonDetails() {
    const { courseId, lessonId } = useParams();

    const lesson = {
        title: "Introduction to Python",
        notes:
            "Python is a high-level, interpreted programming language known for its simple and readable syntax. It is widely used in web development, automation, data science, artificial intelligence, and software development.",
        importantConcepts: [
            "Python syntax",
            "Variables",
            "Data types",
            "Operators",
            "Input and output",
            "Type conversion",
        ],
        youtubeUrl: "https://www.youtube.com/",
    };

    return (
        <main className="lesson-details-page">
            <div className="lesson-details-container">

                <Link
                    to={`/learning/course/${courseId}`}
                    className="back-link"
                >
                    ← Back to Course
                </Link>

                <div className="lesson-header">
                    <span className="lesson-label">
                        Lesson {lessonId}
                    </span>

                    <h1>{lesson.title}</h1>
                </div>

                <section className="lesson-section">

                    <h2>Notes</h2>

                    <p>{lesson.notes}</p>

                </section>

                <section className="lesson-section">

                    <h2>Important Concepts</h2>

                    <ul className="concept-list">
                        {lesson.importantConcepts.map((concept, index) => (
                            <li key={index}>{concept}</li>
                        ))}
                    </ul>

                </section>

                <section className="lesson-section">

                    <h2>Video Lecture</h2>

                    <a
                        href={lesson.youtubeUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="primary-button"
                    >
                        Watch on YouTube
                    </a>

                </section>

            </div>
        </main>
    );
}

export default LessonDetails;