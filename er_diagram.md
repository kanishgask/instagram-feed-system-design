# 📊 ER Diagram - Instagram Feed

USERS
- user_id (PK)
- username
- created_at

POSTS
- post_id (PK)
- user_id (FK)
- media_url
- caption
- created_at

FOLLOWS
- follower_id (FK)
- followee_id (FK)

LIKES
- user_id (FK)
- post_id (FK)

Relationships:

User 1:N Posts  
User N:N User (Follow)  
User N:N Posts (Likes)
