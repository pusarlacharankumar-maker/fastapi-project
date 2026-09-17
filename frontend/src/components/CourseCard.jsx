import { Link } from "react-router-dom";

function CourseCard({
    course,
    progress,
    completedLessons,
    totalLessons,
}) {
    return (
        <article className="course-card">
            <div className="course-card-top">
                <div className="course-icon">
                    {course.title?.charAt(0)?.toUpperCase() || "C"}
                </div>

                <span className="course-label">
                    COURSE
                </span>
            </div>

            <div className="course-card-content">
                <h3>{course.title || "Untitled course"}</h3>

                <p>
                    {course.description || "Build practical skills through structured lessons."}
                </p>

                <div className="course-progress">
                    <div className="progress-meta">
                        <span>{progress}% complete</span>
                        <span>{completedLessons}/{totalLessons} lessons</span>
                    </div>

                    <div className="progress-track">
                        <div
                            className="progress-fill"
                            style={{ width: `${progress}%` }}
                        />
                    </div>
                </div>

                <Link
                    to={`/learning/course/${course.id}`}
                    className="course-link"
                >
                    View course
                </Link>
            </div>
        </article>
    );
}

export default CourseCard;