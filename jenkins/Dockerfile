FROM jenkins/jenkins:lts-alpine

USER root

# 1. Cài đặt các công cụ cần thiết (Docker CLI, Compose, curl và jq)
RUN apk add --no-cache \
    docker-cli \
    docker-cli-compose \
    curl \
    jq

# 2. Tạo group docker và thêm user jenkins vào group đó
# Lưu ý: Group ID (GID) của docker trên host và container nên khớp nhau để tránh lỗi quyền hạn
RUN addgroup -S docker || true && \
    addgroup jenkins docker

USER jenkins

# 3. Kiểm tra cài đặt trong quá trình build (Tùy chọn)
RUN curl --version && jq --version