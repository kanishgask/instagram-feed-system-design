CREATE TABLE users (
    user_id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    post_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(user_id),
    media_url TEXT,
    caption TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE follows (
    follower_id BIGINT REFERENCES users(user_id),
    followee_id BIGINT REFERENCES users(user_id),
    PRIMARY KEY (follower_id, followee_id)
);

CREATE TABLE likes (
    user_id BIGINT REFERENCES users(user_id),
    post_id BIGINT REFERENCES posts(post_id),
    PRIMARY KEY (user_id, post_id)
);
