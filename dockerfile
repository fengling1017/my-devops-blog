# 阶段一：用 Python 运行构建脚本生成网页
FROM python:3.9-slim AS builder
WORKDIR /app
COPY . .
RUN python build.py

# 阶段二：用轻量级 Nginx 托管静态网页
FROM docker.m.daocloud.io/nginx:alpine
COPY --from=builder /app/index.html /usr/share/nginx/html/index.html
EXPOSE 80