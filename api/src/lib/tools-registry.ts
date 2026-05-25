export interface Tool {
  id: string;
  name: string;
  nameEn: string;
  description: string;
  descriptionForAI: string;
  category: ToolCategory;
  subcategory?: string;
  capabilities: string[];
  endpoints: {
    api: string;
    docs: string;
    playground?: string;
  };
  auth: {
    type: 'api-key' | 'oauth' | 'email' | 'none';
    registrationUrl: string;
    authDocs?: string;
  };
  pricing: {
    hasFreeTier: boolean;
    freeCredits?: number;
    startingPrice?: number;
    pricingModel: 'per-call' | 'per-month' | 'credits' | 'freemium';
  };
  metadata: {
    tags: string[];
    useCases: string[];
    examples: string[];
    limitations?: string[];
  };
  openclaw: {
    compatible: boolean;
    difficulty: 'easy' | 'medium' | 'hard';
    configTemplate?: Record<string, string>;
    setupGuide?: string;
  };
  stats?: {
    popularity: number;
    rating: number;
  };
  lastUpdated: string;
}

export type ToolCategory =
  | 'image-generation'
  | 'text-generation'
  | 'code-assistant'
  | 'video-generation'
  | 'audio-processing'
  | 'automation'
  | 'api-service'
  | 'python-library';

export interface AIFriendlyTool {
  id: string;
  name: string;
  description: string;
  usage_example: string;
  capabilities: string[];
  registration_required: boolean;
  free_tier: boolean;
  openclaw_config: Record<string, any>;
}
