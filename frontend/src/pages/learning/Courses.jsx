import { Link } from "react-router-dom";

function Courses() {
    const courses = [
        {
            id: 1,
            title: "Python Programming",
            description:
                "Learn Python fundamentals, functions, modules, packages, recursion, and more.",
        },
        {
            id: 2,
            title: "Web Development",
            description:
                "Learn HTML, CSS, JavaScript, React, and the fundamentals of modern web development.",
        },
        {
            id: 3,
            title: "Data Structures",
            description:
                "Understand arrays, linked lists, stacks, queues, trees, and other important data structures.",
        },
        {
            id: 4,
            title: "Database Management",
            description:
                "Learn SQL, relational databases, queries, relationships, and database concepts.",
        },
    ];

    return (
        <main className="learning-page">
            <div className="learning-container">

                <div className="learning-header">
                    <h1>Learning</h1>
                    <p>
                        Explore courses and build your technical skills step by step.
                    </p>
                </div>

                <div className="courses-grid">
                    {courses.map((course) => (
                        <div className="course-card" key={course.id}>

                            <div className="course-card-content">
                                <h2>{course.title}</h2>

                                <p>{course.description}</p>

                                <Link
                                    to={`/learning/course/${course.id}`}
                                    className="primary-button"
                                >
                                    View Course
                                </Link>
                            </div>

                        </div>
                    ))}
                </div>

            </div>
        </main>
    );
}

export default Courses;