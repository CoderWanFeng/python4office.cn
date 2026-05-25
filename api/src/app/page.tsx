export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-3xl font-bold mb-4">程序员晚枫 - AI API 服务</h1>
      <p className="text-muted-foreground mb-6">
        为 AI Agents 提供博客文章和工具推荐的机器可读接口
      </p>
      
      <div className="space-y-4">
        <section className="border rounded-lg p-4">
          <h2 className="text-xl font-semibold mb-2">📚 博客文章 API</h2>
          <ul className="list-disc list-inside space-y-1 text-sm">
            <li><code className="bg-muted px-2 py-1 rounded">GET /api/posts</code> - 获取文章列表</li>
            <li><code className="bg-muted px-2 py-1 rounded">GET /api/posts/[slug]</code> - 获取文章详情</li>
            <li><code className="bg-muted px-2 py-1 rounded">GET /api/posts/search</code> - 搜索文章</li>
          </ul>
        </section>
        
        <section className="border rounded-lg p-4">
          <h2 className="text-xl font-semibold mb-2">🛠️ 工具推荐 API</h2>
          <ul className="list-disc list-inside space-y-1 text-sm">
            <li><code className="bg-muted px-2 py-1 rounded">GET /api/tools</code> - 获取工具列表</li>
            <li><code className="bg-muted px-2 py-1 rounded">GET /api/tools/[id]</code> - 获取工具详情</li>
            <li><code className="bg-muted px-2 py-1 rounded">GET /api/tools/ai-friendly</code> - AI 友好格式</li>
          </ul>
        </section>
        
        <section className="border rounded-lg p-4">
          <h2 className="text-xl font-semibold mb-2">🤖 MCP Tools</h2>
          <ul className="list-disc list-inside space-y-1 text-sm">
            <li><code className="bg-muted px-2 py-1 rounded">GET /api/mcp</code> - MCP 服务信息</li>
            <li><code className="bg-muted px-2 py-1 rounded">POST /api/mcp</code> - 调用 MCP 工具</li>
          </ul>
        </section>
      </div>
    </main>
  );
}
