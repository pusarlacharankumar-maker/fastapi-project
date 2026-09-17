import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";

import Home from "./pages/Landingpage/Home";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import Dashboard from "./pages/dashboard/Dashboard";

import Courses from "./pages/learning/Courses";
import CourseDetails from "./pages/learning/CourseDetails";
import LessonDetails from "./pages/learning/LessonDetails";
import LearningAnalytics from "./pages/learning/learningAnalytics";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Home />} />

        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/learning"
          element={
            <ProtectedRoute>
              <Courses />
            </ProtectedRoute>
          }
        />

        <Route
          path="/learning/course/:courseId"
          element={
            <ProtectedRoute>
              <CourseDetails />
            </ProtectedRoute>
          }
        />

        <Route
          path="/learning/course/:courseId/lesson/:lessonId"
          element={
            <ProtectedRoute>
              <LessonDetails />
            </ProtectedRoute>
          }
        />

        <Route
          path="/learning/analytics"
          element={
            <ProtectedRoute>
              <LearningAnalytics />
            </ProtectedRoute>
          }
        />

        <Route path="/interview" element={<h1>Interview Preparation</h1>} />
        <Route path="/resume" element={<h1>Resume</h1>} />
        <Route path="/placements" element={<h1>Placements</h1>} />
        <Route path="/admin" element={<h1>Admin</h1>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;