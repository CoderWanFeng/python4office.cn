import { Tool } from '@/lib/tools-registry';
import { Post } from '@/lib/posts-types';
import { TOOLS_DATA } from '@/lib/tools-data';
import { POSTS_DATA } from '@/lib/posts-data';

interface MCPRequest {
  name: string;
  arguments: Record<string, any>;
}

interface MCPResponse {
  content: Array<{
    type: 'text';
    text: string;
  }>;
  isError?: boolean;
}

export class Python4OfficeMCPServer {
  private tools = TOOLS_DATA;
  private posts = POSTS_DATA;

  async handleRequest(request: MCPRequest): Promise<MCPResponse> {
    const { name, arguments: args } = request;

    switch (name) {
      case 'search_python_tools':
        return this.searchTools(args);
      case 'get_tool_details':
        return this.getToolDetails(args);
      case 'get_blog_posts':
        return this.getPosts(args);
      case 'search_posts':
        return this.searchPosts(args);
      case 'get_post_details':
        return this.getPostDetails(args);
      case 'list_categories':
        return this.listCategories(args);
      default:
        return {
          content: [{
            type: 'text',
            text: `Unknown tool: ${name}. Available tools: search_python_tools, get_tool_details, get_blog_posts, search_posts, get_post_details, list_categories`
          }],
          isError: true
        };
    }
  }

  private searchTools(args: {
    query?: string;
    category?: string;
    free_only?: boolean;
  }): MCPResponse {
    let results = [...this.tools];

    if (args.query) {
      const q = args.query.toLowerCase();
      results = results.filter(tool =>
        tool.name.toLowerCase().includes(q) ||
        tool.description.toLowerCase().includes(q) ||
        tool.metadata.tags.some(tag => tag.toLowerCase().includes(q))
      );
    }

    if (args.category) {
      results = results.filter(tool => tool.category === args.category);
    }

    if (args.free_only) {
      results = results.filter(tool => tool.pricing.hasFreeTier);
    }

    const formatted = results.slice(0, 10).map(tool => ({
      id: tool.id,
      name: tool.name,
      description: tool.description,
      category: tool.category,
      capabilities: tool.capabilities.slice(0, 3),
      has_free_tier: tool.pricing.hasFreeTier,
      difficulty: tool.openclaw.difficulty,
      installation: `pip install ${tool.id.replace('-', '-')}`
    }));

    return {
      content: [{
        type: 'text',
        text: JSON.stringify({
          count: formatted.length,
          tools: formatted
        }, null, 2)
      }]
    };
  }

  private getToolDetails(args: Record<string, any>): MCPResponse {
    const toolId = args.tool_id || args.toolId;
    const tool = this.tools.find(t => t.id === toolId);

    if (!tool) {
      return {
        content: [{
          type: 'text',
          text: `Tool not found: ${toolId}`
        }],
        isError: true
      };
    }

    return {
      content: [{
        type: 'text',
        text: JSON.stringify({
          id: tool.id,
          name: tool.name,
          description: tool.descriptionForAI,
          category: tool.category,
          capabilities: tool.capabilities,
          use_cases: tool.metadata.useCases,
          pricing: {
            has_free_tier: tool.pricing.hasFreeTier,
            free_credits: tool.pricing.freeCredits,
            starting_price: tool.pricing.startingPrice
          },
          setup: {
            difficulty: tool.openclaw.difficulty,
            installation: `pip install ${tool.id.replace('-', '-')}`,
            guide: tool.openclaw.setupGuide
          },
          examples: tool.metadata.examples
        }, null, 2)
      }]
    };
  }

  private getPosts(args: {
    query?: string;
    tags?: string[];
    limit?: number;
  }): MCPResponse {
    let results = [...this.posts].filter(p => !p.draft);

    if (args.query) {
      const q = args.query.toLowerCase();
      results = results.filter(post =>
        post.title.toLowerCase().includes(q) ||
        post.description?.toLowerCase().includes(q) ||
        post.tags.some(tag => tag.toLowerCase().includes(q))
      );
    }

    if (args.tags && args.tags.length > 0) {
      results = results.filter(post =>
        args.tags!.some(tag => post.tags.includes(tag))
      );
    }

    const formatted = results.slice(0, args.limit || 10).map(post => ({
      slug: post.slug,
      title: post.title,
      description: post.description,
      tags: post.tags,
      date: post.date,
      reading_time: post.readingTime,
      url: `https://www.python4office.cn/${post.slug}`
    }));

    return {
      content: [{
        type: 'text',
        text: JSON.stringify({
          count: formatted.length,
          posts: formatted
        }, null, 2)
      }]
    };
  }

  private searchPosts(args: { query: string }): MCPResponse {
    const q = args.query.toLowerCase();

    const results = this.posts
      .filter(post => !post.draft)
      .filter(post =>
        post.title.toLowerCase().includes(q) ||
        post.description?.toLowerCase().includes(q) ||
        post.tags.some(tag => tag.toLowerCase().includes(q))
      )
      .map(post => ({
        slug: post.slug,
        title: post.title,
        description: post.description,
        match_reasons: [
          post.title.toLowerCase().includes(q) && '标题匹配',
          post.description?.toLowerCase().includes(q) && '描述匹配',
          post.tags.some(tag => tag.toLowerCase().includes(q)) && '标签匹配'
        ].filter(Boolean)
      }))
      .sort((a, b) => b.match_reasons.length - a.match_reasons.length)
      .slice(0, 10);

    return {
      content: [{
        type: 'text',
        text: JSON.stringify({
          query: args.query,
          results,
          total: results.length
        }, null, 2)
      }]
    };
  }

  private getPostDetails(args: Record<string, any>): MCPResponse {
    const slug = args.slug;
    const post = this.posts.find(p => p.slug === slug);

    if (!post) {
      return {
        content: [{
          type: 'text',
          text: `Post not found: ${slug}`
        }],
        isError: true
      };
    }

    return {
      content: [{
        type: 'text',
        text: JSON.stringify({
          slug: post.slug,
          title: post.title,
          date: post.date,
          tags: post.tags,
          description: post.description,
          author: post.author,
          reading_time: post.readingTime,
          url: `https://www.python4office.cn/${post.slug}`
        }, null, 2)
      }]
    };
  }

  private listCategories(_args: any): MCPResponse {
    const toolCategories = [...new Set(this.tools.map(t => t.category))];
    const postTags = [...new Set(this.posts.flatMap(p => p.tags))];

    return {
      content: [{
        type: 'text',
        text: JSON.stringify({
          tool_categories: toolCategories,
          post_tags: postTags.slice(0, 20)
        }, null, 2)
      }]
    };
  }
}

export const mcpServer = new Python4OfficeMCPServer();
