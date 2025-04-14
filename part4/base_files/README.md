# Simple Web Client Project

This project is the front-end part of a full-stack application. It focuses on building an interactive web client using **HTML5**, **CSS3**, and **JavaScript ES6**. The application connects seamlessly with the back-end services developed in earlier phases, allowing users to browse places, view details, and add reviews.

## 🚀 Project Overview

The goal of this project is to design and implement a user-friendly interface that interacts with the back-end API to manage places and reviews. It features modern web development practices to deliver a dynamic and responsive user experience.

## 🌟 Features

- **User Authentication**
  - Secure login using JWT token.
  - Session management with cookies.
  
- **Places Listing**
  - Dynamic fetching and display of places.
  - Client-side filtering by country.
  
- **Place Details**
  - Detailed information about each place.
  - Option to add reviews (for authenticated users).
  
- **Add Review**
  - Form to submit reviews, accessible only to logged-in users.

## 🎯 Objectives

- Develop a clean and responsive user interface.
- Implement efficient data fetching and handling with **Fetch API**.
- Use **client-side scripting** to improve user experience without page reloads.
- Ensure secure interactions with back-end services.
- Manage user sessions and authentication.

## 🧩 Tasks Breakdown

### Design
- Complete HTML and CSS to match provided design specs.
- Create pages:
  - **Login**
  - **List of Places**
  - **Place Details**
  - **Add Review**

### Login
- Implement login flow with API.
- Store JWT token in cookies for session persistence.

### List of Places
- Display all places from API.
- Implement filtering by country.
- Redirect unauthenticated users to the login page.

### Place Details
- Fetch and display detailed information of selected place.
- Display add review form for authenticated users only.

### Add Review
- Create and handle review form submission.
- Ensure access control to authenticated users only.

## 🛠️ Technologies Used

- **HTML5**
- **CSS3**
- **JavaScript ES6**
- **Fetch API**
- **JWT for authentication**

## 📚 Learning Goals

- Apply modern front-end technologies in a real-world project.
- Interact with APIs using **Fetch/AJAX**.
- Implement session management with cookies.
- Enhance UX with dynamic, script-driven behaviors.

## 🔐 Authentication & Session Management

- On successful login, the JWT token is stored in cookies.
- Protected routes (like adding a review) check for authentication before granting access.


## Contributors

Ahmed El Guindou