# Booking Data Pipeline — Project Blueprint

## 1. Problem Statement
Dữ liệu khách sạn và thông tin liên quan đến du lịch được phân tán trên các nguồn web khác nhau và có cấu trúc không đồng nhất. Việc thu thập dữ liệu bằng các script crawl đơn lẻ khó đảm bảo khả năng lưu trữ, kiểm tra, xử lý lại và sử dụng một cách ổn định.
Project này tập trung vào xây dựng data pipeline để thu thập dữ liệu khách sạn từ Booking.com, sau đó lưu trữ, kiểm tra, biến đổi và chuẩn hóa dữ liệu thành các dataset có cấu trúc.
Dữ liệu sau khi được xử lý có thể trở thành nền tảng cho các use case downstream như:
+ Hotel Analytics
+ Review analysis
+ Recommendation system
+ Reporting 
## 2. Goal
Mục tiêu chính của project là xây dựng một batch-oriented hotel data pipeline hướng tới việc tạo ra dữ liệu: 
+ Có cấu trúc
+ Có thể kiểm tra chất lượng 
+ Có thể xử lý lại 
+ Có thể mở rộng 
+ Có thể phục vụ các hệ thống phân tích hoặc machine learning downstream 

## 3. Scope
Tập trung xây dựng các thành phần:
+ Source Discovery
+ URL Discovery
+ Hotel Data Extraction
+ Raw Data Storage
+ Bronze Layer
+ Data Transformation
+ Silver Layer
+ Gold Layer
+ Data Quality
+ Logging
+ Testing
+ Incremental Processing
+ Idempotent Processing
+ Pipeline Documentation
Pipeline được thiết kế theo hướng batch processing.
## 4. Functional Requirements
### 4.1. Source Discovery 
Pipeline phải có khả năng xác định và discover các nguồn dữ liệu phù hợp từ Booking.com
### 4.2. URL Discovery
Pipeline phải discover và quản lý các URL cần được xử lý 
### 4.3. Data Extraction
- Pipeline phải có khả năng thu thập dữ liệu khách sạn từ các URL đã được xác định
- Các dữ liệu có thể bao gồm:
+ Hotel information
+ Location
+ Room information
+ Price
+ Review
+ Availability
### 4.4. Raw Data Storage
Pipeline phải lưu trữ dữ liệu raw trước khi transformation để dữ liệu có thể được: 
+ Reprocess
+ Debug
+ Audit
+ Reproduce'
Raw data không được overwrite một cách tùy tiện.
### 4.5. Bronze Layer
Pipeline phải tạo ra Bronze layer từ raw data để phục vụ các bước xử lý tiếp theo
### 4.6. Data Transformation
Pipeline phải transform dữ liệu từ raw/ Bronze thành dữ liệu có cấu trúc và chuẩn hóa hơn.
### 4.7. Silver Layer
Pipeline phải tạo Silver layer chứa dữ liệu đã được clean, normalize, validate, Deduplicate. 
### 4.8. Gold Layer
Pipeline phải tạo các dataset phục vụ các use case phân tích hoặc downstream systems
Pipeline phải có khả năng phát hiện dữ liệu mới hoặc dữ liệu đã thay đổi để tránh xử lý lại toàn bộ dữ liệu khi không cần thiết.
### 4.9. Incremental Processing 
Có thể sử dụng các metadata như:
+ Last_crawled_at
+ Last_seen_at
+ Content_hash
+ Source_updated_at
### 4.10. Deduplication
Pipeline phải hạn chế việc tạo duplicate data khi cùng một source hoặc entity được xử lý nhiều lần.
### 4.11. Data Quality 
Pipeline phải kiểm tra các điều kiện chất lượng dữ liệu trước hoặc trong quá trình đưa dữ liệu sang các layer tiếp theo.
### 4.12. Logging 
Pipeline phải ghi lại thông tin cần thiết để biết:
+ Pipeline đang chạy ở đâu
+ Bao nhiêu record được xử lý
+ Bao nhiêu record thất bại
+ Lỗi xảy ra ở component nào
+ Processing time
### 4.13. Retry 
Các lỗi có tính chất tạm thời trong quá trình extraction phải có cơ chế retry phù hợp.
### 4.14. Testing 
Các component quan trọng của pipeline phải có thể được kiểm thử độc lập.
## 5. Non-functional Requirements

## 6. Input
Dữ liệu ra crawl dudojc từ booking.com, pinterest ,...(chủ yếu là booking.com)

## 7. Output
Dữ liệu sạch có giá trị phục vụ cho Recommendation System

## 8. Success Criteria
