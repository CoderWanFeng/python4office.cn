import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "程序员晚枫 - API 服务",
  description: "为 AI Agents 提供的博客文章和工具推荐 API",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
