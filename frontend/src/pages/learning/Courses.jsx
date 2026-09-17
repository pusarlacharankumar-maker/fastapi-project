import { useEffect, useMemo, useState } from "react";
import CourseCard from "../../components/CourseCard";

import {
    getCourses,
    getAllProgress,
    getCourseLessons,
    calculateCourseProgress,
    getCompletedLessonCount,
    getAuthToken,
} from "../../services/learningApi";

import "./Learning.css";


function Courses() {

    const [courses, setCourses] = useState([]);
    const [progress, setProgress] = useState([]);

    const [courseLessons, setCourseLessons] =
        useState({});

    const [loading, setLoading] =
        useState(true);

    const [error, setError] =
        useState("");


    async function loadLearningData() {

        try {

            setLoading(true);
            setError("");

            const coursesData =
                await getCourses();

            setCourses(
                Array.isArray(coursesData)
                    ? coursesData
                    : []
            );


            // Progress requires authentication.
            if (getAuthToken()) {

                try {

                    const progressData =
                        await getAllProgress();

                    setProgress(
                        Array.isArray(progressData)
                            ? progressData
                            : []
                    );

                } catch (progressError) {

                    console.warn(
                        "Progress could not be loaded:",
                        progressError
                    );

                    setProgress([]);
                }

            } else {

                setProgress([]);

            }


            // Fetch lessons for every course.
            const lessonsMap = {};

            await Promise.all(
                coursesData.map(async (course) => {

                    try {

                        const lessons =
                            await getCourseLessons(
                                course.id
                            );

                        lessonsMap[course.id] =
                            Array.isArray(lessons)
                                ? lessons
                                : [];

                    } catch {

                        lessonsMap[course.id] = [];

                    }

                })
            );

            setCourseLessons(lessonsMap);

        } catch (err) {

            setError(
                err.message ||
                "Unable to load courses."
            );

        } finally {

            setLoading(false);

        }
    }


    useEffect(() => {
        const load = window.setTimeout(() => {
            void loadLearningData();
        }, 0);

        return () => window.clearTimeout(load);
    }, []);


    const totalLessons = useMemo(() => {

        return Object.values(courseLessons)
            .reduce(
                (total, lessons) =>
                    total + lessons.length,
                0
            );

    }, [courseLessons]);


    const completedLessons = useMemo(() => {

        return Object.values(courseLessons)
            .reduce(
                (total, lessons) =>
                    total +
                    getCompletedLessonCount(
                        lessons,
                        progress
                    ),
                0
            );

    }, [courseLessons, progress]);


    if (loading) {

        return (
            <main className="learning-page">

                <section className="learning-loading">

                    <div className="loading-spinner" />

                    <h2>
                        Loading your learning space...
                    </h2>

                    <p>
                        Fetching courses and progress.
                    </p>

                </section>

            </main>
        );
    }


    if (error) {

        return (
            <main className="learning-page">

                <section className="learning-state">

                    <div className="state-icon">
                        !
                    </div>

                    <h2>
                        Unable to load courses
                    </h2>

                    <p>
                        {error}
                    </p>

                    <button
                        className="retry-button"
                        onClick={loadLearningData}
                    >
                        Try Again
                    </button>

                </section>

            </main>
        );
    }


    return (
        <main className="learning-page">

            {/* =========================================
                HERO
            ========================================== */}

            <section className="learning-hero">

                <div className="learning-hero-content">

                    <span className="eyebrow">
                        CODESPHERE LEARNING
                    </span>

                    <h1>
                        Learn skills.
                        <br />
                        <span>Build your future.</span>
                    </h1>

                    <p>
                        Learn through structured courses,
                        practical lessons and continuous
                        progress tracking.
                    </p>

                </div>


                <div className="learning-orbit">

                    <div className="orbit-ring ring-one" />
                    <div className="orbit-ring ring-two" />

                    <div className="orbit-core">
                        AI
                    </div>

                </div>

            </section>


            {/* =========================================
                OVERVIEW
            ========================================== */}

            <section className="learning-overview">

                <div className="overview-item">

                    <span className="overview-number">
                        {courses.length}
                    </span>

                    <span className="overview-label">
                        Available Courses
                    </span>

                </div>


                <div className="overview-item">

                    <span className="overview-number">
                        {totalLessons}
                    </span>

                    <span className="overview-label">
                        Total Lessons
                    </span>

                </div>


                <div className="overview-item">

                    <span className="overview-number">
                        {completedLessons}
                    </span>

                    <span className="overview-label">
                        Completed Lessons
                    </span>

                </div>

            </section>


            {/* =========================================
                COURSES
            ========================================== */}

            <section className="courses-section">

                <div className="section-heading">

                    <div>

                        <span className="eyebrow">
                            YOUR LEARNING
                        </span>

                        <h2>
                            Explore courses
                        </h2>

                    </div>

                    <p>
                        Courses published by your
                        CodeSphere administrator appear here
                        automatically.
                    </p>

                </div>


                {courses.length === 0 ? (

                    <div className="empty-state">

                        <div className="empty-icon">
                            +
                        </div>

                        <h3>
                            No courses available yet
                        </h3>

                        <p>
                            New courses will appear here
                            when an administrator publishes them.
                        </p>

                    </div>

                ) : (

                    <div className="courses-grid">

                        {courses.map((course) => {

                            const lessons =
                                courseLessons[
                                course.id
                                ] || [];

                            const courseProgress =
                                calculateCourseProgress(
                                    lessons,
                                    progress
                                );

                            const completed =
                                getCompletedLessonCount(
                                    lessons,
                                    progress
                                );

                            return (
                                <CourseCard
                                    key={course.id}
                                    course={course}
                                    progress={
                                        courseProgress
                                    }
                                    completedLessons={
                                        completed
                                    }
                                    totalLessons={
                                        lessons.length
                                    }
                                />
                            );

                        })}

                    </div>

                )}

            </section>

        </main>
    );
}

export default Courses;