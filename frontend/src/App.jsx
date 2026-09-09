import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import Dashboard from "./pages/dashboard/Dashboard";

import Courses from "./pages/learning/Courses";
import CourseDetails from "./pages/learning/CourseDetails";
import LessonDetails from "./pages/learning/LessonDetails";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>

        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Home />} />

        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route path="/dashboard" element={<Dashboard />} />

        <Route path="/learning" element={<Courses />} />

        <Route
          path="/learning/course/:courseId"
          element={<CourseDetails />}
        />

        <Route
          path="/learning/course/:courseId/lesson/:lessonId"
          element={<LessonDetails />}
        />

        <Route
          path="/interview"
          element={<h1>Interview Preparation</h1>}
        />

        <Route
          path="/resume"
          element={<h1>Resume</h1>}
        />

        <Route
          path="/placements"
          element={<h1>Placements</h1>}
        />

        <Route
          path="/admin"
          element={<h1>Admin</h1>}
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App;