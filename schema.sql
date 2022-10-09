CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE titles (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    posted_at TIMESTAMP,
    posted_by INTEGER REFERENCES users,
    topic_id INTEGER,
    visibility BOOLEAN
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    comment TEXT,
    title_id INTEGER REFERENCES titles,
    commentor TEXT
    sent_at TIMESTAMP,
    visibility BOOLEAN
);