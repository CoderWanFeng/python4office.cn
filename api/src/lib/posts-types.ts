export interface Post {
  slug: string;
  title: string;
  date: string;
  updated?: string;
  tags: string[];
  categories?: string[];
  description?: string;
  author?: string;
  content?: string;
  wordCount?: number;
  readingTime?: number;
  cover?: string;
  featured?: boolean;
  draft?: boolean;
}

export interface PostSearchParams {
  query?: string;
  tags?: string[];
  categories?: string[];
  limit?: number;
  page?: number;
}

export interface PostListResponse {
  success: boolean;
  data: {
    posts: Post[];
    total: number;
    page: number;
    perPage: number;
  };
  meta: {
    generatedAt: string;
  };
}

export interface PostDetailResponse {
  success: boolean;
  data: Post;
  related?: Post[];
  meta: {
    generatedAt: string;
  };
}

export interface AIFriendlyPost {
  slug: string;
  title: string;
  summary: string;
  tags: string[];
  date: string;
  url: string;
  reading_time_minutes: number;
}

export interface AIFriendlyPostsResponse {
  posts: AIFriendlyPost[];
  count: number;
  purpose: string;
  format_version: string;
}
