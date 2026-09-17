import { useEffect, useState } from "react";
import {
    Link,
    useNavigate,
    useParams,
} from "react-router-dom";

import {
    getCourse,
    getCourseLessons,
    getLesson,
    getLessonProgress,
    updateLessonProgress,
    getAuthToken,
} from "../../services/learningApi";

import "./Learning.css";


function LessonDetails() {

    const {
        courseId,
        lessonId,
    } = useParams();

    const navigate = useNavigate();


    const [course, setCourse] =
        useState(null);

    const [lesson, setLesson] =
        useState(null);

    const [lessons, setLessons] =
        useState([]);

    const [currentProgress, setCurrentProgress] =
        useState(0);

    const [loading, setLoading] =
        useState(true);

    const [saving, setSaving] =
        useState(false);

    const [error, setError] =
        useState("");


    async function loadLesson() {

        try {

            setLoading(true);
            setError("");

            const [
                courseData,
                lessonData,
                lessonsData,
            ] = await Promise.all([
                getCourse(courseId),
                getLesson(lessonId),
                getCourseLessons(courseId),
            ]);


            setCourse(courseData);

            setLesson(lessonData);

            setLessons(
                Array.isArray(lessonsData)
                    ? lessonsData
                    : []
            );


            if (getAuthToken()) {

                try {

                    const progressData =
                        await getLessonProgress(
                            lessonId
                        );

                    setCurrentProgress(
                        Number(
                            progressData
                                ?.completion_percentage ||
                            0
                        )
                    );

                } catch {

                    setCurrentProgress(0);

                }

            }

        } catch (err) {

            setError(
                err.message ||
                "Unable to load lesson."
            );

        } finally {

            setLoading(false);

        }
    }


    useEffect(() => {
        const load = window.setTimeout(() => {
            void loadLesson();
        }, 0);

        return () => window.clearTimeout(load);
    }, [courseId, lessonId]);


    async function markComplete() {

        if (!getAuthToken()) {

            alert(
                "Please login to save your progress."
            );

            navigate("/login");

            return;
        }


        try {

            setSaving(true);

            const result =
                await updateLessonProgress(
                    lessonId,
                    100
                );

            setCurrentProgress(
                Number(
                    result?.completion_percentage ||
                    100
                )
            );

        } catch (err) {

            alert(
                err.message ||
                "Unable to save progress."
            );

        } finally {

            setSaving(false);

        }
    }


    if (loading) {

        return (
            <main className="learning-page">

                <section className="learning-loading">

                    <div className="loading-spinner" />

                    <h2>
                        Loading lesson...
                    </h2>

                </section>

            </main>
        );
    }


    if (error || !lesson) {

        return (
            <main className="learning-page">

                <section className="learning-state">

                    <div className="state-icon">
                        !
                    </div>

                    <h2>
                        Unable to load lesson
                    </h2>

                    <p>
                        {error}
                    </p>

                    <Link
                        to={`/learning/course/${courseId}`}
                        className="retry-button"
                    >
                        Back to Course
                    </Link>

                </section>

            </main>
        );
    }


    const currentIndex =
        lessons.findIndex(
            (item) =>
                Number(item.id) ===
                Number(lessonId)
        );


    const previousLesson =
        currentIndex > 0
            ? lessons[currentIndex - 1]
            : null;


    const nextLesson =
        currentIndex >= 0 &&
            currentIndex < lessons.length - 1
            ? lessons[currentIndex + 1]
            : null;


    return (
        <main className="lesson-page">

            {/* =========================================
                TOP BAR
            ========================================== */}

            <div className="lesson-topbar">

                <Link
                    to={`/learning/course/${courseId}`}
                    className="back-link"
                >
                    ← {course?.title}
                </Link>

                <span>
                    Lesson{" "}
                    {currentIndex + 1} of{" "}
                    {lessons.length}
                </span>

            </div>


            {/* =========================================
                LESSON HEADER
            ========================================== */}

            <section className="lesson-header">

                <span className="eyebrow">
                    LESSON {String(
                        currentIndex + 1
                    ).padStart(2, "0")}
                </span>

                <h1>
                    {lesson.title}
                </h1>

                {lesson.important_concepts && (
                    <p className="lesson-concepts">
                        {lesson.important_concepts}
                    </p>
                )}

            </section>


            {/* =========================================
                VIDEO
            ========================================== */}

            {lesson.youtube_url && (

                <section className="lesson-video">

                    <iframe
                        src={getYoutubeEmbedUrl(
                            lesson.youtube_url
                        )}
                        title={lesson.title}
                        allowFullScreen
                    />

                </section>

            )}


            {/* =========================================
                NOTES
            ========================================== */}

            <section className="lesson-body">

                <div className="lesson-main-content">

                    <span className="eyebrow">
                        LESSON NOTES
                    </span>

                    <div className="lesson-notes">

                        {lesson.notes ? (
                            lesson.notes
                                .split("\n")
                                .map(
                                    (line, index) => (
                                        <p key={index}>
                                            {line}
                                        </p>
                                    )
                                )
                        ) : (
                            <p>
                                No notes have been
                                added for this lesson yet.
                            </p>
                        )}

                    </div>

                </div>


                {/* =====================================
                    PROGRESS PANEL
                ====================================== */}

                <aside className="lesson-sidebar">

                    <div className="progress-panel">

                        <span className="eyebrow">
                            YOUR PROGRESS
                        </span>

                        <strong>
                            {Math.round(
                                currentProgress
                            )}%
                        </strong>

                        <div className="progress-track">

                            <div
                                className="progress-fill"
                                style={{
                                    width: `${currentProgress}%`,
                                }}
                            />

                        </div>


                        {currentProgress >= 100 ? (

                            <div className="completed-message">
                                ✓ Lesson completed
                            </div>

                        ) : (

                            <button
                                className="complete-button"
                                onClick={
                                    markComplete
                                }
                                disabled={saving}
                            >
                                {saving
                                    ? "Saving..."
                                    : "Mark as Complete"}
                            </button>

                        )}

                    </div>

                </aside>

            </section>


            {/* =========================================
                NAVIGATION
            ========================================== */}

            <section className="lesson-navigation">

                {previousLesson ? (

                    <Link
                        to={`/learning/course/${courseId}/lesson/${previousLesson.id}`}
                        className="lesson-nav-button"
                    >
                        <span>
                            Previous
                        </span>

                        <strong>
                            ← {previousLesson.title}
                        </strong>
                    </Link>

                ) : (
                    <div />
                )}


                {nextLesson ? (

                    <Link
                        to={`/learning/course/${courseId}/lesson/${nextLesson.id}`}
                        className="lesson-nav-button next"
                    >
                        <span>
                            Next Lesson
                        </span>

                        <strong>
                            {nextLesson.title} →
                        </strong>
                    </Link>

                ) : (

                    <Link
                        to={`/learning/course/${courseId}`}
                        className="lesson-nav-button next"
                    >
                        <span>
                            Course
                        </span>

                        <strong>
                            Finish Course →
                        </strong>
                    </Link>

                )}

            </section>

        </main>
    );
}


// ======================================================
// YOUTUBE URL HELPER
// ======================================================

function getYoutubeEmbedUrl(url) {

    if (!url) {
        return "";
    }

    try {

        const parsed =
            new URL(url);

        let videoId = "";


        if (
            parsed.hostname.includes(
                "youtube.com"
            )
        ) {

            videoId =
                parsed.searchParams.get(
                    "v"
                ) || "";

        } else if (
            parsed.hostname.includes(
                "youtu.be"
            )
        ) {

            videoId =
                parsed.pathname
                    .replace("/", "");
        }


        if (!videoId) {
            return url;
        }


        return `https://www.youtube.com/embed/${videoId}`;

    } catch {

        return url;

    }
}


export default LessonDetails;