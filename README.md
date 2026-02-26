# 📸 Instagram Feed System Design

> Day 4 – High-Package Software Engineer Journey 🚀

---

## 📌 Problem Statement

Design Instagram's News Feed system where users see posts from accounts they follow.

The feed should:
- Show most recent posts
- Scale to millions of users
- Support likes and comments
- Handle high write and read traffic

---

# 🎯 Functional Requirements

- User can post photo/video
- User can follow/unfollow
- User sees feed of followed users
- Show posts in chronological order
- Support likes and comments

---

# ⚙️ Non-Functional Requirements

- High availability
- Low latency (<200ms feed load)
- Horizontally scalable
- Handle millions of posts per day
- Fault tolerant

---

# 🧠 Feed Generation Approaches

## 1️⃣ Pull Model (Fan-out on Read)

- Generate feed when user requests it
- Fetch posts from followed users
- Pros: Lower write cost
- Cons: Slower read for high follower count

## 2️⃣ Push Model (Fan-out on Write)

- When user posts → push to followers' feed
- Pros: Faster reads
- Cons: Heavy write cost

✔ Real systems use Hybrid approach.

---

# 🏗️ High-Level Architecture

User  
   ↓  
Load Balancer  
   ↓  
Feed Service  
   ↓  
Cache (Redis)  
   ↓  
Post Database  
   ↓  
Media Storage (S3)

---

# 📊 Capacity Estimation

Assume:
- 100M users
- 10M daily active users
- Avg 5 posts per user/day

50M posts/day  
Huge read traffic (more than writes)

Hence:
- Heavy read optimization required

---

# 🔐 Security Considerations

- Private accounts
- Access control
- Rate limiting
- Content moderation

---

# 🚀 Future Enhancements

- Ranking algorithm (ML based)
- Story integration
- Reels recommendation
- Geo-tag filtering

---

# 🎯 Concepts Demonstrated

- System Design at Scale
- Read vs Write optimization
- Distributed caching
- Database sharding
- Trade-off analysis

---

⭐ Part of Elite 30-Day Engineering Series
