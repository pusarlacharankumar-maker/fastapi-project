import { Link, useParams } from "react-router-dom";

function CourseDetails() {
    const { courseId } = useParams();

    const course = {
        id: courseId,
        title: "Python Programming",
        description:
            "Learn Python programming from the fundamentals to important advanced concepts.",
        lessons: [
            {
                id: 1,
                title: "Introduction to Python",
                description:
                    "Learn Python basics, syntax, variables, data types, and operators.",
            },
            {
                id: 2,
                title: "Conditional Statements",
                description:
                    "Learn if, elif, else statements and decision-making in Python.",
            },
            {
                id: 3,
                title: "Loops",
                description:
                    "Understand for loops, while loops, break, continue, and pass.",
            },
            {
                id: 4,
                title: "Functions",
                description:
                    "Learn how to create and use functions, parameters, arguments, and return values.",
            },
            {
                id: 5,
                title: "Modules and Packages",
                description:
                    "Understand modules, packages, imports, and code organization.",
            },
        ],
    };

    return (
        <main className="course-details-page">
            <div className="course-details-container">

                <Link to="/learning" className="back-link">
                    ← Back to Courses
                </Link>

                <div className="course-details-header">
                    <h1>{course.title}</h1>

                    <p>{course.description}</p>
                </div>

                <section className="lessons-section">

                    <h2>Course Lessons</h2>

                    <div className="lessons-list">

                        {course.lessons.map((lesson, index) => (
                            <div className="lesson-card" key={lesson.id}>

                                <div className="lesson-number">
                                    {index + 1}
                                </div>

                                <div className="lesson-content">
                                    <h3>{lesson.title}</h3>
                                    <p>{lesson.description}</p>
                                </div>

                                <Link
                                    to={`/learning/course/${courseId}/lesson/${lesson.id}`}
                                    className="secondary-button"
                                >
                                    Open Lesson
                                </Link>

                            </div>
                        ))}

                    </div>

                </section>

            </div>
        </main>
    );
}

export default CourseDetails;