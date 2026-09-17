const API_BASE_URL =
    import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";


// ======================================================
// TOKEN
// ======================================================

export function getAuthToken() {
    return (
        localStorage.getItem("token") ||
        localStorage.getItem("access_token") ||
        localStorage.getItem("authToken")
    );
}


// ======================================================
// COMMON REQUEST
// ======================================================

async function apiRequest(endpoint, options = {}) {
    const token = getAuthToken();

    const headers = {
        "Content-Type": "application/json",
        ...(options.headers || {}),
    };

    if (token) {
        headers.Authorization = `Bearer ${token}`;
    }

    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            ...options,
            headers,
        }
    );

    let data;
    try {
        data = await response.json();
    } catch {
        data = undefined;
    }

    if (!response.ok) {
        const message =
            data?.detail ||
            data?.message ||
            `Request failed with status ${response.status}`;

        throw new Error(message);
    }

    return data;
}


// ======================================================
// COURSES
// ======================================================

export async function getCourses() {
    return apiRequest("/learning/courses");
}


export async function getCourse(courseId) {
    return apiRequest(`/learning/courses/${courseId}`);
}


// ======================================================
// LESSONS
// ======================================================

export async function getCourseLessons(courseId) {
    return apiRequest(
        `/learning/courses/${courseId}/lessons`
    );
}


export async function getLesson(lessonId) {
    return apiRequest(
        `/learning/lessons/${lessonId}`
    );
}


// ======================================================
// PROGRESS
// ======================================================

export async function getAllProgress() {
    return apiRequest("/progress");
}


export async function getLessonProgress(lessonId) {
    return apiRequest(
        `/progress/lesson/${lessonId}`
    );
}


export async function updateLessonProgress(
    lessonId,
    completionPercentage
) {
    return apiRequest(
        "/progress",
        {
            method: "POST",
            body: JSON.stringify({
                lesson_id: Number(lessonId),
                completion_percentage:
                    Number(completionPercentage),
            }),
        }
    );
}


// ======================================================
// HELPERS
// ======================================================

export function getProgressForLesson(
    progressList,
    lessonId
) {
    if (!Array.isArray(progressList)) {
        return 0;
    }

    const progress = progressList.find(
        (item) =>
            Number(item.lesson_id) ===
            Number(lessonId)
    );

    return progress
        ? Number(progress.completion_percentage || 0)
        : 0;
}


export function calculateCourseProgress(
    lessons,
    progressList
) {
    if (!Array.isArray(lessons) || lessons.length === 0) {
        return 0;
    }

    const total = lessons.reduce(
        (sum, lesson) => {
            const lessonProgress =
                getProgressForLesson(
                    progressList,
                    lesson.id
                );

            return sum + lessonProgress;
        },
        0
    );

    return Math.round(total / lessons.length);
}


export function getCompletedLessonCount(
    lessons,
    progressList
) {
    if (!Array.isArray(lessons)) {
        return 0;
    }

    return lessons.filter(
        (lesson) =>
            getProgressForLesson(
                progressList,
                lesson.id
            ) >= 100
    ).length;
}


export default {
    getCourses,
    getCourse,
    getCourseLessons,
    getLesson,
    getAllProgress,
    getLessonProgress,
    updateLessonProgress,
    getProgressForLesson,
    calculateCourseProgress,
    getCompletedLessonCount,
};