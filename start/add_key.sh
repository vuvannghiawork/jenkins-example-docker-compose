#!/bin/bash

# Thông tin Public Key của bạn
PUB_KEY="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIO1T+YZlZNT6EiOXbYL6hmB2Oc/qfT9deP3hDIuNL6T2 vuvannghia.work@gmail.com"

# Đường dẫn đến file authorized_keys
AUTH_FILE="$HOME/.ssh/authorized_keys"

# Tạo thư mục .ssh nếu chưa có và set quyền 700
mkdir -p "$HOME/.ssh"
chmod 700 "$HOME/.ssh"

# Kiểm tra xem key đã tồn tại trong file chưa để tránh trùng lặp
if ! grep -q "$PUB_KEY" "$AUTH_FILE" 2>/dev/null; then
    echo "$PUB_KEY" >> "$AUTH_FILE"
    chmod 600 "$AUTH_FILE"
    echo "✅ Đã thêm key thành công vào $AUTH_FILE"
else
    echo "ℹ️ Key này đã tồn tại sẵn trong authorized_keys."
fi