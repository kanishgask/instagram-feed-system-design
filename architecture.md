# 🏗️ Instagram Feed Architecture

Client  
   ↓  
Load Balancer  
   ↓  
Feed API Servers  
   ↓  
Redis Cache  
   ↓  
Post Database (Sharded)  
   ↓  
Media Stored in Object Storage (S3)  

---

# Scaling Techniques

- Read replicas
- Redis caching
- Fan-out strategy (hybrid)
- Database sharding by user_id
- CDN for media delivery

---

# Trade-off Analysis

Push Model:
- Fast reads
- Expensive writes

Pull Model:
- Cheap writes
- Slower reads

Hybrid:
- Optimized for celebrities & normal users
