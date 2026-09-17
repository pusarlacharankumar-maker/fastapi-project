const API_BASE_URL =
    import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

async function authRequest(endpoint, options = {}) {
    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            ...options,
            headers: {
                "Content-Type": "application/json",
                ...(options.headers || {}),
            },
        }
    );

    let data;
    try {
        data = await response.json();
    } catch {
        data = undefined;
    }

    if (!response.ok) {
        throw new Error(
            data?.detail ||
            data?.message ||
            `Request failed with status ${response.status}`
        );
    }

    return data;
}

export function registerUser(user) {
    return authRequest(
        "/auth/register",
        {
            method: "POST",
            body: JSON.stringify(user),
        }
    );
}

export function loginUser(credentials) {
    return authRequest(
        "/auth/login",
        {
            method: "POST",
            body: JSON.stringify(credentials),
        }
    );
}